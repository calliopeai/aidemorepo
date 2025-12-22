"""
Calliope AI Magic Commands for Jupyter

This module provides %%calliope magic commands for interacting with the Calliope Data Agent API.

Usage:
    %%calliope ask-sql <datasource_id> [options]
    <natural language query>

    %%calliope run-sql <datasource_id> [options]
    <SQL query>

    %%calliope generate-sql <datasource_id> [options]
    <natural language description>

Installation:
    # In a Jupyter notebook:
    %load_ext calliope_magic

    # Or add to IPython startup:
    # ~/.ipython/profile_default/startup/load_calliope.py
"""

import os
import requests
import json
import pandas as pd
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.magic_arguments import (argument, magic_arguments, parse_argstring)
from IPython.display import display, HTML, Markdown
import argparse


@magics_class
class CalliopeMagics(Magics):
    """Calliope AI magic commands for Jupyter notebooks"""

    def __init__(self, shell):
        super(CalliopeMagics, self).__init__(shell)
        self.base_url = None

    def get_base_url(self):
        """Get the API base URL from environment or default"""
        if self.base_url:
            return self.base_url

        # Check environment variables
        base_url = os.environ.get('CALLIOPE_API_BASE_URL')
        if not base_url:
            base_url = os.environ.get('DATA_AGENT_URL')
        if not base_url:
            base_url = 'http://localhost:5000'

        self.base_url = base_url.rstrip('/')
        return self.base_url

    def parse_args(self, line):
        """Parse command line arguments"""
        parts = line.split()
        if not parts:
            raise ValueError("Missing subcommand. Use: ask-sql, run-sql, or generate-sql")

        subcommand = parts[0]
        if subcommand not in ['ask-sql', 'run-sql', 'generate-sql']:
            raise ValueError(f"Unknown subcommand: {subcommand}. Use: ask-sql, run-sql, or generate-sql")

        if len(parts) < 2:
            raise ValueError(f"Missing datasource_id for {subcommand}")

        datasource_id = parts[1]

        # Parse optional arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--sql-model', default='anthropic', help='SQL generation model')
        parser.add_argument('--model', default='claude3', help='AI analysis model')
        parser.add_argument('--to-ai', action='store_true', help='Send results to AI for analysis')
        parser.add_argument('--format', default='table', choices=['table', 'json', 'csv'], help='Output format')

        try:
            args, unknown = parser.parse_known_args(parts[2:])
        except SystemExit:
            args = argparse.Namespace(sql_model='anthropic', model='claude3', to_ai=False, format='table')

        return subcommand, datasource_id, args

    def make_request(self, endpoint, data):
        """Make HTTP request to Data Agent API"""
        base_url = self.get_base_url()
        url = f"{base_url}{endpoint}"

        try:
            response = requests.post(url, json=data, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            raise Exception(f"Could not connect to Calliope API at {base_url}. Is the Data Agent running?")
        except requests.exceptions.Timeout:
            raise Exception(f"Request to {url} timed out")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP Error: {e.response.status_code} - {e.response.text}")

    def display_results(self, result, format_type='table'):
        """Display query results"""
        if 'error' in result:
            display(HTML(f'<div style="color: red; padding: 10px; border: 1px solid red; border-radius: 5px;">'
                        f'<strong>Error:</strong> {result["error"]}'
                        f'</div>'))
            if 'details' in result:
                print(f"Details: {result['details']}")
            return

        # Display SQL if present
        if 'sql' in result:
            display(Markdown(f"**Generated SQL:**\n```sql\n{result['sql']}\n```"))

        # Display data if present
        if 'data' in result and result['data']:
            if format_type == 'json':
                display(HTML(f'<pre>{json.dumps(result["data"], indent=2)}</pre>'))
            elif format_type == 'csv':
                df = pd.DataFrame(result['data'])
                print(df.to_csv(index=False))
            else:  # table
                df = pd.DataFrame(result['data'])
                display(df)

        # Display metadata if present
        if 'metadata' in result:
            meta = result['metadata']
            info_parts = []
            if 'row_count' in meta:
                info_parts.append(f"Rows: {meta['row_count']}")
            if 'execution_time' in meta:
                info_parts.append(f"Time: {meta['execution_time']:.3f}s")

            if info_parts:
                display(HTML(f'<div style="color: gray; font-size: 0.9em; margin-top: 5px;">'
                            f'{" | ".join(info_parts)}'
                            f'</div>'))

        # Display AI analysis if present
        if 'analysis' in result:
            display(Markdown(f"**AI Analysis:**\n\n{result['analysis']}"))

    @cell_magic
    def calliope(self, line, cell):
        """
        Calliope AI magic command

        Usage:
            %%calliope ask-sql <datasource_id> [--sql-model MODEL] [--to-ai] [--model MODEL]
            What are the top 10 customers?

            %%calliope run-sql <datasource_id> [--format FORMAT]
            SELECT * FROM customers LIMIT 10

            %%calliope generate-sql <datasource_id> [--sql-model MODEL]
            Generate SQL to find top customers
        """
        try:
            subcommand, datasource_id, args = self.parse_args(line)
            query = cell.strip()

            if not query:
                raise ValueError("Query/SQL cannot be empty")

            # Route to appropriate endpoint
            if subcommand == 'ask-sql':
                endpoint = '/api/sql/ask'
                data = {
                    'datasource_id': datasource_id,
                    'question': query,
                    'sql_model': args.sql_model
                }

                result = self.make_request(endpoint, data)

                # Display results
                self.display_results(result, args.format)

                # If --to-ai flag is set, send to AI for analysis
                if args.to_ai and 'data' in result:
                    analysis_data = {
                        'question': query,
                        'sql': result.get('sql', ''),
                        'data': result['data'][:100],  # Limit to first 100 rows for analysis
                        'model': args.model
                    }
                    try:
                        analysis_result = self.make_request('/api/analyze', analysis_data)
                        if 'analysis' in analysis_result:
                            display(Markdown(f"### AI Analysis\n\n{analysis_result['analysis']}"))
                        else:
                            display(Markdown(f"*Analysis completed with model: {args.model}*"))
                    except Exception as e:
                        display(Markdown(f"*AI analysis unavailable: {str(e)}*"))

            elif subcommand == 'run-sql':
                endpoint = '/api/sql/run_sql'
                data = {
                    'datasource_id': datasource_id,
                    'sql': query
                }

                result = self.make_request(endpoint, data)
                self.display_results(result, args.format)

            elif subcommand == 'generate-sql':
                endpoint = '/api/sql/generate'
                data = {
                    'datasource_id': datasource_id,
                    'description': query,
                    'sql_model': args.sql_model
                }

                result = self.make_request(endpoint, data)
                self.display_results(result, args.format)

        except Exception as e:
            display(HTML(f'<div style="color: red; padding: 10px; border: 1px solid red; border-radius: 5px;">'
                        f'<strong>Calliope Magic Error:</strong> {str(e)}'
                        f'</div>'))
            import traceback
            traceback.print_exc()


def load_ipython_extension(ipython):
    """Load the extension in IPython"""
    ipython.register_magics(CalliopeMagics)
    print("✅ Calliope AI magic commands loaded!")
    print("   Usage: %%calliope ask-sql <datasource> | run-sql <datasource> | generate-sql <datasource>")

    # Set base URL if available
    base_url = os.environ.get('CALLIOPE_API_BASE_URL') or os.environ.get('DATA_AGENT_URL')
    if base_url:
        print(f"   API URL: {base_url}")
    else:
        print("   API URL: http://localhost:5000 (default)")


def unload_ipython_extension(ipython):
    """Unload the extension"""
    pass

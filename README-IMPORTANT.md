# ⚠️ IMPORTANT: Calliope Configuration Required

## Quick Fix for "Invalid URL 'None/api/sql/run_sql'" Error

The `%%calliope` magic commands need to know where the Data Agent API is running.

### Solution: Add This Cell to the TOP of Every Notebook

Before using any `%%calliope` commands, run this configuration cell:

```python
import os

# Configure Calliope API endpoint
# Option 1: Docker/JupyterHub environment (default)
API_BASE_URL = os.environ.get('DATA_AGENT_URL', 'http://data-agent:5000')

# Option 2: Local development (uncomment if running locally)
# API_BASE_URL = 'http://localhost:5000'

# Set for Calliope magic commands
os.environ['CALLIOPE_API_BASE_URL'] = API_BASE_URL
print(f"✅ Calliope API configured: {API_BASE_URL}")
```

### OR: Use the Setup Notebook

**Recommended**: Run `00-Setup-Calliope.ipynb` FIRST, then use any other notebook.

## How the Magic Commands Work

The `%%calliope` magic commands are wrappers around the Data Agent API that make HTTP requests to:

```
http://data-agent:5000/api/sql/run_sql
http://data-agent:5000/api/sql/ask_sql
http://data-agent:5000/api/datasources
```

Without the `CALLIOPE_API_BASE_URL` environment variable set, they don't know where to send requests.

## Alternative: Use Direct API Calls

If magic commands aren't working, you can use direct API calls instead:

```python
import requests

API_BASE_URL = 'http://data-agent:5000'  # or http://localhost:5000

# List datasources
response = requests.get(f'{API_BASE_URL}/api/datasources')
print(response.json())

# Run SQL
payload = {
    'datasource_id': 'sakila',
    'sql': 'SELECT * FROM film LIMIT 10'
}
response = requests.post(f'{API_BASE_URL}/api/sql/run_sql', json=payload)
print(response.json())

# Ask SQL (natural language)
payload = {
    'datasource_id': 'sakila',
    'question': 'What are the top 10 most rented films?',
    'model': 'anthropic'
}
response = requests.post(f'{API_BASE_URL}/api/sql/ask_sql', json=payload)
print(response.json())
```

## Verification

Test your configuration:

```python
import requests
import os

API_BASE_URL = os.environ.get('CALLIOPE_API_BASE_URL', 'http://data-agent:5000')

try:
    response = requests.get(f'{API_BASE_URL}/api/datasources', timeout=5)
    if response.status_code == 200:
        datasources = response.json()['datasources']
        print(f"✅ Connected! Found {len(datasources)} datasources:")
        for ds in datasources:
            print(f"  • {ds['id']}: {ds['name']} ({ds['dialect']})")
    else:
        print(f"❌ API returned status {response.status_code}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print("\nTroubleshooting:")
    print("1. Check if data-agent is running: docker-compose ps data-agent")
    print("2. Check logs: docker logs data-agent")
    print("3. Verify API_BASE_URL is correct")
```

## Updated Notebook Template

Here's what each notebook should look like:

```python
# Cell 1: Configuration (ADD THIS!)
import os
API_BASE_URL = os.environ.get('DATA_AGENT_URL', 'http://data-agent:5000')
os.environ['CALLIOPE_API_BASE_URL'] = API_BASE_URL

# Cell 2: Verify connection
import requests
response = requests.get(f'{API_BASE_URL}/api/datasources')
datasources = response.json()['datasources']
sakila_ds = [ds for ds in datasources if ds['id'] == 'sakila'][0]
print(f"✅ Connected to {sakila_ds['name']}")

# Cell 3: Now you can use magic commands
%%calliope run-sql sakila
SELECT * FROM film LIMIT 5
```

## Why This Happens

The Calliope magic commands (from jupyter-ai or similar) expect the API endpoint to be configured via environment variables. When it's not set, the code tries to use `None` as the base URL, resulting in the error:

```
Invalid URL 'None/api/sql/run_sql': No scheme supplied
```

## Quick Start Checklist

- [ ] Data agent is running (`docker-compose ps data-agent`)
- [ ] Run `00-Setup-Calliope.ipynb` to configure
- [ ] OR add configuration cell to top of each notebook
- [ ] Verify connection before using magic commands
- [ ] Start querying!

## Need Help?

1. Check `00-Setup-Calliope.ipynb` for complete setup guide
2. See `REAL-DATASOURCES.md` for datasource details
3. Review logs: `docker logs data-agent`
4. Test API: `curl http://localhost:5000/api/datasources`
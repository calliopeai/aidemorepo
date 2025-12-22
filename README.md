# Calliope AI Lab - JupyterLab AI Demo Repository

A comprehensive collection of 55+ Jupyter notebooks demonstrating AI-powered data analysis, natural language database queries, and AI-assisted development using Calliope AI and Jupyter AI.

**55+ Notebooks | 6 Pre-configured Databases | 15 Categories | Multiple AI Models**

---

## What is Calliope AI?

Calliope AI is a powerful Jupyter magic extension that enables natural language database queries with automatic SQL generation, execution, and visualization. It wraps and extends Jupyter AI, giving you access to multiple AI providers while specializing in database operations.

### Key Features
- **Natural Language SQL**: Ask questions in plain English, get SQL + results + charts
- **Multi-Model Support**: OpenAI, Anthropic, Google Gemini, Cohere, Mistral, and more
- **Automatic Visualizations**: Smart chart generation based on your data
- **RAG Training**: Teach Calliope your business logic and schema
- **Multiple Databases**: Connect to PostgreSQL, MySQL, SQLite, and more
- **Direct SQL**: Generate and execute SQL with full control

---

## Quick Start

### Start Here: `00-INDEX-Calliope-Examples.ipynb`
Complete navigation guide with learning paths, quick reference, and all 55+ notebooks!

### 5-Minute Quick Start
1. Open `05-Database/datasources/Datasource-Sakila.ipynb`
2. Run the first query cell
3. You're analyzing data with AI!

---

## Repository Structure

```
Calliope-AI-Lab-Demo/
├── 00-Getting-Started/      # Setup, configuration, quickstart
│   └── 00-model-config.ipynb    # Central model aliases
├── 01-Code-Generation/      # AI code assistant, refactoring
├── 02-Data-Exploration/     # EDA, profiling, data cleaning
├── 03-Visualization/        # Matplotlib, Seaborn, Plotly, dashboards
├── 04-RAG-Documents/        # PDF Q&A, semantic search
├── 05-Database/             # SQL generation, datasources
│   └── datasources/         # Sakila, Chinook, Employees, etc.
├── 06-AI-ML/                # Classification, forecasting, ML
├── 07-DevOps/               # Infrastructure, monitoring
├── 08-InfoSec/              # Security analysis, log analysis
├── 09-FinOps-Cloud/         # AWS cost analysis, optimization
├── 10-Scientific/           # Physics, chemistry, bioinformatics
├── 11-Financial/            # Quant analysis, options pricing
├── 12-Time-Series/          # Forecasting, anomaly detection
├── 13-NLP/                  # Text generation, sentiment
├── 14-Advanced/             # Complex examples
├── 15-Reference/            # Documentation, API guides
└── CalliopeLabExamples/     # Additional real-world examples
    ├── AI-Data-Analysis/    # 15 advanced analysis notebooks
    └── InfoSec/             # Penetration testing
```

---

## Model Configuration

This repository uses model aliases for easy updates when models are deprecated:

```python
# Current recommended models (December 2025)
CLAUDE = "anthropic-chat:claude-sonnet-4-5-20250929"
CLAUDE_FAST = "anthropic-chat:claude-haiku-4-5-20251001"
GPT = "openai-chat:gpt-5"
GEMINI = "gemini:gemini-2.5-flash"

# Usage with Calliope
%calliope -d sakila --sql-model $CLAUDE "Show top customers"

# Usage with Jupyter AI
%%ai $CLAUDE
Explain SQL window functions
```

**See `00-Getting-Started/00-model-config.ipynb` for full configuration.**

---

## Pre-configured Databases

| Database | Type | Tables | Use Case |
|----------|------|--------|----------|
| Sakila | MySQL | film, customer, rental, payment | Retail, inventory |
| Chinook | PostgreSQL | artist, album, track, invoice | E-commerce, music |
| Employees | MySQL | employees, salaries, departments | HR, compensation |
| Northwind | PostgreSQL | products, orders, customers | Supply chain, B2B |
| World | MySQL | country, city, countrylanguage | Geography, demographics |
| AirportDB | MySQL | flights, airports, airlines | Transportation, logistics |

**No setup required!** These databases are pre-configured and ready to use.

---

## Learning Paths

### Path 1: Data Analyst
1. `00-Getting-Started/00-model-config.ipynb`
2. `05-Database/datasources/Datasource-Sakila.ipynb`
3. `03-Visualization/Calliope-Visualizations.ipynb`
4. `05-Database/Calliope-AdvancedQueries.ipynb`

### Path 2: Data Scientist
1. `00-Getting-Started/00-model-config.ipynb`
2. `02-Data-Exploration/CSV_Column_Normalizer.ipynb`
3. `06-AI-ML/01-classification-diabetes.ipynb`
4. `12-Time-Series/01-forecasting-sales.ipynb`

### Path 3: Developer
1. `00-Getting-Started/00-model-config.ipynb`
2. `01-Code-Generation/01-ai-code-assistant.ipynb`
3. `05-Database/Calliope-DirectSQL.ipynb`
4. `04-RAG-Documents/Calliope-RAGTraining.ipynb`

### Path 4: Cloud/DevOps
1. `00-Getting-Started/00-model-config.ipynb`
2. `09-FinOps-Cloud/01-aws-cost-analysis.ipynb`
3. `08-InfoSec/01-security-analysis.ipynb`
4. `07-DevOps/Dual Webservice with Graphing.ipynb`

---

## Quick Reference

### Calliope Commands
```python
%calliope                         # Show help
%calliope list                    # List datasources
%calliope list-models             # List AI models
%calliope -d sakila "query"       # Natural language query
%calliope -d sakila schema        # Show database schema
%calliope -d sakila --sql-model $MODEL "query"  # Specify model
%calliope -d sakila --to-ai $MODEL "query"      # Get AI analysis
```

### Jupyter AI Magic
```python
%%ai $MODEL                       # General AI query
%%ai $MODEL -f code               # Generate code
```

---

## Available Data

### CSV Datasets (~/lab/data/CSVs/)
| Dataset | Size | Use Case |
|---------|------|----------|
| Crime_Data | 244MB | Spatiotemporal analysis |
| EPA_SmartLocation | 193MB | Urban analytics |
| Electric_Vehicle | 57MB | Transportation, geospatial |
| Chronic_Disease | 85MB | Healthcare analytics |
| Warehouse_Sales | 27MB | Time series, forecasting |
| Baby_Names | 2.7MB | Trend analysis |
| Diabetes | 16KB | ML classification |

### PDF Documents (~/lab/data/PDFs/)
- Google Borg, Autopilot papers
- O'Reilly Observability Engineering
- SRE Incident Metrics
- Control Systems Theory
- ML Exercises

---

## Supported AI Providers

- **Anthropic**: Claude Sonnet 4.5, Claude Opus 4.1, Claude Haiku 4.5
- **OpenAI**: GPT-5, GPT-4o
- **Google**: Gemini 2.5 Pro/Flash
- **Mistral**: Mistral Large, Codestral
- **Cohere**: Command A
- **AWS Bedrock**: Claude, Llama, and more
- **Ollama**: Local deployment

---

## Installation

```bash
pip install jupyter-ai calliope-magic
```

---

## Contributing

Have examples to share? Please contribute!

1. Create a new notebook following the existing format
2. Use model aliases from `00-model-config.ipynb`
3. Include clear explanations and use cases
4. Self-install dependencies with `%pip install -q`
5. Test all code cells
6. Submit a pull request

---

## License

This repository contains example notebooks for educational purposes.

---

**Happy querying!**

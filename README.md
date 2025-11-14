# 🔮 Calliope AI & Jupyter Magic Examples Repository

A comprehensive collection of Jupyter notebooks demonstrating Calliope AI magic commands for natural language database queries and AI-powered data analysis.

## 📚 What is Calliope AI?

Calliope AI is a powerful Jupyter magic extension that enables natural language database queries with automatic SQL generation, execution, and visualization. It wraps and extends Jupyter AI, giving you access to multiple AI providers while specializing in database operations.

### Key Features
- 🗣️ **Natural Language SQL**: Ask questions in plain English, get SQL + results + charts
- 🤖 **Multi-Model Support**: OpenAI, Anthropic, Google Gemini, Cohere, and more
- 📊 **Automatic Visualizations**: Smart chart generation based on your data
- 🎓 **RAG Training**: Teach Calliope your business logic and schema
- 🔗 **Multiple Databases**: Connect to PostgreSQL, MySQL, SQLite, and more
- ⚡ **Direct SQL**: Generate and execute SQL with full control

## 🚀 Quick Start

### 📑 NEW! Start Here → `00-INDEX-Calliope-Examples.ipynb`
**Complete navigation guide** to all 28+ notebooks with learning paths, quick reference, and examples!

### Installation
```bash
pip install jupyter-ai calliope-magic
```

### Basic Usage
```python
# Add a database
%%calliope add-database
{
    "datasource_id": "my_db",
    "name": "My Database",
    "dialect": "postgresql",
    "connection_details": {
        "host": "localhost",
        "port": 5432,
        "database": "mydb",
        "user": "user",
        "password": "password"
    }
}

# Ask a question
%%calliope ask-sql my_db
What were our top products last quarter?
```

## 📖 Notebook Examples

### 🔌 Real Datasource Examples (Use Pre-configured Databases!)

These notebooks connect to **real, pre-configured sample databases** via the Calliope API server on port 5000. **No setup required!**

#### 🎬 Sakila DVD Rental Store
**File**: `Calliope-RealData-Sakila.ipynb` | **Datasource**: `sakila` (MySQL)

Analyze a DVD rental business with:
- Film catalog and actor analysis
- Rental revenue and customer behavior
- Inventory optimization
- Time-series trends

**Perfect for**: Retail analytics, inventory management

#### 🎵 Chinook Music Store
**File**: `Calliope-RealData-Chinook.ipynb` | **Datasource**: `chinook` (PostgreSQL)

Digital music store analytics:
- Artist and album performance
- Customer segmentation
- Genre preferences by geography
- Sales trends and employee performance

**Perfect for**: E-commerce analytics, music industry insights

#### 📦 Northwind Traders
**File**: `Calliope-RealData-Northwind.ipynb` | **Datasource**: `northwind` (PostgreSQL)

Classic business operations database:
- Product catalog and suppliers
- Order analysis and shipping
- Customer lifetime value
- Geographic market analysis

**Perfect for**: Business operations, supply chain analytics

**See [REAL-DATASOURCES.md](REAL-DATASOURCES.md) for complete details on all 6 available datasources!**

---

### 📚 Tutorial Notebooks (Create Your Own Databases)

#### 1. 🎯 Getting Started
**File**: `Calliope-GettingStarted.ipynb`

Perfect for beginners! Learn:
- Basic Calliope commands
- Database connection setup
- Your first natural language queries
- Model selection

**Start here if you're new to Calliope!**

### 2. 🚀 Advanced Queries
**File**: `Calliope-AdvancedQueries.ipynb`

Master complex analytical queries:
- Multi-table joins
- Window functions and ranking
- Time-series analysis
- Statistical aggregations
- Cohort analysis

**Prerequisites**: Basic SQL knowledge helpful but not required

### 3. 🎓 RAG Training
**File**: `Calliope-RAGTraining.ipynb`

Improve query accuracy with training:
- Schema documentation
- Business metric definitions
- Custom calculations
- Domain-specific terminology
- Query examples library

**When to use**: After you're comfortable with basics, want better results

### 4. 💻 Direct SQL Operations
**File**: `Calliope-DirectSQL.ipynb`

For developers who want control:
- Generate SQL without execution
- Run custom SQL queries
- Debug and optimize queries
- Iterative query development
- Combine NL and SQL

**Best for**: Developers, SQL practitioners, debugging

### 5. 📊 Visualizations
**File**: `Calliope-Visualizations.ipynb`

Master automatic chart generation:
- Time-series plots
- Bar and pie charts
- Scatter plots and correlations
- Heatmaps and distributions
- Multi-dimensional analysis

**Best for**: Data analysts, presentation preparation

#### 6. 🔗 Jupyter AI Integration
**File**: `Calliope-JupyterAI-Integration.ipynb`

Combine Calliope with Jupyter AI:
- Query → AI analysis workflows
- Multi-model analysis
- Automated reporting pipelines
- Statistical analysis with AI
- Model comparison

**Advanced**: Leverage multiple AI models for comprehensive analysis

---

## 🎯 Quick Reference

### Common Commands

```python
# Get help
%%calliope help

# List available AI models
%%calliope list-models

# Ask a question (generates SQL, executes, visualizes)
%%calliope ask-sql datasource_id
What are the sales trends?

# Generate SQL only (no execution)
%%calliope generate-sql datasource_id
Show top customers by revenue

# Run SQL directly
%%calliope run-sql datasource_id
SELECT * FROM customers WHERE signup_date > '2024-01-01'

# Train with business logic
%%calliope rag-train datasource_id
{
    "documentation": ["MRR = Monthly Recurring Revenue"],
    "sql": ["SELECT SUM(revenue) FROM subscriptions WHERE status='active'"]
}

# General AI assistant
%%calliope ask datasource_id --model gpt4
Explain customer churn analysis

# Generate follow-up questions
%%calliope followup-questions datasource_id
```

### Model Selection

```python
# Specify SQL generation model
%%calliope ask-sql my_db --sql-model anthropic
Complex analytical query here

# Specify post-processing model
%%calliope ask-sql my_db --model openai --to-ai
Analyze and explain the results

# Best model for each task:
# - anthropic: Complex analytical SQL
# - openai: General purpose, reliable
# - gemini: Fast, simple queries
# - cohere: Structured data analysis
```

## 🗄️ Database Support

### Pre-configured Sample Databases (Ready to Use!)
Access these databases instantly via the Calliope API (port 5000):
- **sakila** (MySQL) - DVD rental store
- **chinook** (PostgreSQL) - Music store
- **northwind** (PostgreSQL) - Business operations
- **employees** (MySQL) - HR database
- **world** (MySQL) - Geographic data
- **airportdb** (MySQL) - Airport operations

**No setup required!** See [REAL-DATASOURCES.md](REAL-DATASOURCES.md) for details.

### Supported Database Dialects
Connect your own databases:
- PostgreSQL
- MySQL
- SQLite
- Microsoft SQL Server
- Oracle
- Snowflake
- BigQuery
- Redshift
- And more!

## 🎓 Learning Path

**Absolute Beginner** ⭐ Start Here!
1. Open `Calliope-RealData-Sakila.ipynb` (no setup required!)
2. Run your first natural language query
3. Try `Calliope-RealData-Chinook.ipynb` for variety

**Beginner**
1. Start with `Calliope-GettingStarted.ipynb` (learn setup)
2. Try `Calliope-Visualizations.ipynb` (chart generation)
3. Experiment with all real datasources

**Intermediate**
1. Work through `Calliope-AdvancedQueries.ipynb` (complex SQL)
2. Learn `Calliope-DirectSQL.ipynb` (SQL control)
3. Practice with `Calliope-RealData-Northwind.ipynb` (business analytics)

**Advanced**
1. Master `Calliope-RAGTraining.ipynb` (custom training)
2. Explore `Calliope-JupyterAI-Integration.ipynb` (multi-model)
3. Build automated analysis pipelines with real data

## 🤖 Supported AI Providers

- **OpenAI**: GPT-4o, GPT-4, GPT-3.5
- **Anthropic**: Claude 3.5 Sonnet, Claude 3 Opus/Haiku
- **Google**: Gemini 2.5 Pro/Flash
- **Cohere**: Command R+, Command R
- **Mistral**: Mistral Large, Mixtral
- **AI21**: Jurassic models
- **AWS Bedrock**: Multiple models
- **Ollama**: Local deployment
- And many more!

## 💡 Use Cases

### Business Analytics
- Sales performance analysis
- Customer segmentation
- Revenue forecasting
- Churn analysis

### Marketing
- Campaign performance
- Attribution analysis
- ROI calculations
- A/B test analysis

### Product Analytics
- User behavior analysis
- Feature usage metrics
- Engagement tracking
- Conversion funnels

### Operations
- Inventory analysis
- Supply chain metrics
- Process optimization
- Resource allocation

## 🛠️ Tips & Best Practices

### 1. Start Simple
Begin with straightforward questions, then build complexity.

### 2. Use RAG Training
Train Calliope on your schema and business logic for better results.

### 3. Choose the Right Model
- Complex queries → `anthropic`
- Speed → `gemini`
- General purpose → `openai`

### 4. Iterate
Use `generate-sql` to review queries before execution.

### 5. Combine Approaches
Mix natural language with direct SQL for optimal results.

### 6. Document Your Work
Use AI to generate explanations and documentation.

## 🔧 Troubleshooting

### Connection Issues
```python
# Test your connection
%%calliope run-sql my_db
SELECT 1
```

### Query Not Working?
1. Check your question clarity
2. Try a different model (--sql-model anthropic)
3. Use RAG training to provide context
4. Generate SQL first to review

### Model Errors?
```python
# Check available models
%%calliope list-models

# Ensure API keys are set
```

## 📚 Additional Resources

- [Calliope Documentation](https://docs.calliopeai.com)
- [Jupyter AI Documentation](https://jupyter-ai.readthedocs.io)
- [API Reference](https://docs.calliopeai.com/api)

## 🤝 Contributing

Have examples to share? Please contribute!

1. Create a new notebook following the existing format
2. Include clear explanations and use cases
3. Test all code cells
4. Submit a pull request

## 📜 License

This repository contains example notebooks for educational purposes.

## 🆘 Getting Help

- Check the notebook examples
- Review command help: `%%calliope help`
- Consult the official documentation
- Open an issue for bugs or questions

## 🎉 Other Examples in This Repository

This repository also contains other Jupyter AI examples:

### 🎨 NEW! **AI-Visualization-Showcase.ipynb**
**Featured notebook** demonstrating how to create stunning visualizations with natural language!
- 10+ examples comparing different AI models
- Interactive Plotly charts, 3D plots, animations
- Real-world data analysis patterns
- Model comparison guide

### Classic Visualization Examples:
- **MathPlotLib.ipynb** - Visualization examples with matplotlib
- **TextGeneration.ipynb** - AI text generation examples
- **SeabornVizDemo.ipynb** - Statistical visualizations
- **Combined Plotly.ipynb** - Interactive Plotly charts
- **Lorenz Attractor Demo.ipynb** - Scientific computing example
- **Integrating GPT Prompts in Jupyter.ipynb** - GPT integration guide

---

## 🚀 Getting Started Checklist

### 🆕 Best Way to Start (Recommended!)
- [ ] Open **`00-INDEX-Calliope-Examples.ipynb`** - Master navigation guide
- [ ] Choose your learning path based on your role
- [ ] Follow the structured tutorial sequence
- [ ] 🎉 You're on your way!

### Quick Start (No Setup!)
- [ ] Verify API is running: `curl http://localhost:5000/api/datasources`
- [ ] Open `Datasource-Sakila.ipynb` (formerly Calliope-RealData-Sakila)
- [ ] Run your first cell to verify connection
- [ ] Execute a natural language query
- [ ] 🎉 You're analyzing data with AI!

### Full Setup
- [ ] Install Calliope AI: `pip install jupyter-ai calliope-magic`
- [ ] Set up API keys for your chosen AI provider
- [ ] Try real datasource notebooks first
- [ ] Then open `Calliope-GettingStarted.ipynb` to learn database setup
- [ ] Check out `AI-Visualization-Showcase.ipynb` for viz inspiration
- [ ] Explore advanced features in other notebooks
- [ ] Connect your own databases
- [ ] Build something amazing!

## 🔗 Quick Links

- **Start with real data**: [REAL-DATASOURCES.md](REAL-DATASOURCES.md)
- **API reference**: Check available datasources at `http://localhost:5000/api/datasources`
- **Beginner notebook**: `Calliope-RealData-Sakila.ipynb`
- **Advanced analytics**: `Calliope-AdvancedQueries.ipynb`

**Happy querying! 🎉**
# ✅ Ready to Test!

## 🎉 Calliope Magic Command Implementation

**IMPORTANT UPDATE**: The `%%calliope` magic command has been implemented as a custom IPython extension!

### ✅ What Was Done

1. **Created calliope_magic.py** - IPython extension that implements `%%calliope` commands
2. **Added extension loading** to all notebooks
3. **Verified all 6 datasources** have dedicated notebooks
4. **Created Test-Calliope-Magic.ipynb** - Test all magic commands
5. **Pre-wired Jupyter config** for future sessions

### 📊 Datasource Notebooks (6 total)

Each notebook is dedicated to ONE datasource with 20-35 example queries:

| Notebook | Datasource ID | Database | Description |
|----------|--------------|----------|-------------|
| `Datasource-Sakila.ipynb` | `sakila` | MySQL | 🎬 DVD rental store |
| `Datasource-Chinook.ipynb` | `chinook` | PostgreSQL | 🎵 Music store |
| `Datasource-Northwind.ipynb` | `northwind` | PostgreSQL | 📦 Business operations |
| `Datasource-Employees.ipynb` | `employees` | MySQL | 👔 HR database |
| `Datasource-World.ipynb` | `world` | MySQL | 🌍 Geographic data |
| `Datasource-AirportDB.ipynb` | `airportdb` | MySQL | ✈️ Aviation data |

### 🗄️ Feature Showcase Notebooks (2 total)

| Notebook | Covers | Examples |
|----------|--------|----------|
| `MySQL-Features-Showcase.ipynb` | All 4 MySQL databases | 20+ advanced MySQL features |
| `PostgreSQL-Features-Showcase.ipynb` | Both PostgreSQL databases | 25+ advanced PostgreSQL features |

## 🚀 How to Test

### Quick Start - Test the Magic Command First!

1. **Start with the test notebook**:
   ```bash
   jupyter notebook Test-Calliope-Magic.ipynb
   ```

2. **Run the first 3 cells**:
   - Cell 1: Loads the `calliope_magic` extension
   - Cell 2: Sets `CALLIOPE_API_BASE_URL`
   - Cell 3: Verifies connection to Data Agent

3. **Run any test cell**:
   ```python
   %%calliope run-sql sakila
   SELECT * FROM film LIMIT 5
   ```

Should work immediately! ✅

### How the Magic Command Works

The `%%calliope` magic command supports 3 subcommands:

1. **ask-sql** - Natural language to SQL + execution:
   ```python
   %%calliope ask-sql <datasource> [--sql-model MODEL] [--to-ai] [--model MODEL]
   What are the top 10 customers by total spend?
   ```

2. **run-sql** - Execute SQL directly:
   ```python
   %%calliope run-sql <datasource> [--format table|json|csv]
   SELECT * FROM customers LIMIT 10
   ```

3. **generate-sql** - Generate SQL without executing:
   ```python
   %%calliope generate-sql <datasource> [--sql-model MODEL]
   Create a query to find top customers
   ```

### Load the Extension in Any Notebook

Add these cells at the beginning of any notebook:

```python
# Cell 1: Load the calliope magic extension
import sys
sys.path.insert(0, '/mnt/efs/users/lmata/lab/aidemorepo')
%load_ext calliope_magic
```

```python
# Cell 2: Configure the API endpoint
import os
os.environ['CALLIOPE_API_BASE_URL'] = 'http://localhost:5000'
print(f"✅ Calliope API configured")
```

### Test Each Datasource

Try one example from each:

#### Test Sakila (MySQL)
```python
%%calliope ask-sql sakila
What are the top 10 most rented films?
```

#### Test Chinook (PostgreSQL)
```python
%%calliope ask-sql chinook
Show the top 10 best-selling artists by revenue
```

#### Test Northwind (PostgreSQL)
```python
%%calliope ask-sql northwind
What are our top 10 customers by total spending?
```

#### Test Employees (MySQL)
```python
%%calliope ask-sql employees
Show average salary by department
```

#### Test World (MySQL)
```python
%%calliope ask-sql world
What are the 20 most populous countries?
```

#### Test AirportDB (MySQL)
```python
%%calliope ask-sql airportdb
Which airports have the most flights?
```

## 📋 Configuration Cell Format

Every notebook now starts with this configuration:

```python
import os

# Configure Calliope Data Agent API endpoint
API_BASE_URL = 'http://localhost:5000'  # Local development
# API_BASE_URL = 'http://data-agent:5000'  # Docker/JupyterHub

os.environ['CALLIOPE_API_BASE_URL'] = API_BASE_URL
print(f"✅ Calliope API configured: {API_BASE_URL}")
```

**To change for Docker/JupyterHub**: Just comment/uncomment the appropriate line!

## 🔍 Verification Checklist

Before testing, verify:

- [ ] Data Agent is running: `docker-compose ps data-agent`
- [ ] API is responding: `curl http://localhost:5000/api/datasources`
- [ ] Datasources are available (should show 6)

## 🐛 Troubleshooting

### Error: "Invalid URL 'None/api/sql/run_sql'"
**Fix**: Make sure you ran the configuration cell (Cell 2) first!

### Error: "Connection refused"
**Fix**:
```bash
# Check if data-agent is running
docker-compose ps data-agent

# Check logs
docker logs data-agent

# Restart if needed
docker-compose restart data-agent
```

### Error: "Datasource not found"
**Fix**: Check the datasource ID matches exactly (case-sensitive):
- `sakila` ✅
- `Sakila` ❌

## 📊 What's in Each Notebook

### Datasource Notebooks
Each contains:
- ✅ Configuration cell (runs first)
- ✅ Connection verification
- ✅ Schema exploration
- ✅ 20-35 example queries
- ✅ Natural language queries (`ask-sql`)
- ✅ Direct SQL queries (`run-sql`)
- ✅ AI-enhanced analysis (`--to-ai`)
- ✅ Complex analytics examples

### Feature Showcase Notebooks
Each contains:
- ✅ Configuration cell
- ✅ Database-specific features
- ✅ String/Date/Time functions
- ✅ Window functions
- ✅ CTEs and recursive queries
- ✅ Advanced aggregates
- ✅ Performance optimization
- ✅ 20-25 working examples

## 🎯 Quick Start Commands

```bash
# Start in the notebook directory
cd /mnt/efs/users/lmata/lab/aidemorepo

# List all notebooks
ls -1 *.ipynb

# Start with any datasource
jupyter notebook Datasource-Sakila.ipynb

# Or start with feature showcase
jupyter notebook MySQL-Features-Showcase.ipynb
```

## ✨ Success Indicators

You'll know it's working when you see:

1. **After config cell runs**:
   ```
   ✅ Calliope API configured: http://localhost:5000
   ```

2. **After a query runs**:
   - Results table appears
   - Optional: Chart/visualization
   - No error messages

3. **Natural language queries work**:
   ```python
   %%calliope ask-sql sakila
   What are the top films?
   ```
   Should generate SQL, execute it, and show results!

## 📦 Complete Repository Structure

```
aidemorepo/
├── 00-Setup-Calliope.ipynb          (Optional setup guide)
├── README.md                         (Main documentation)
├── README-IMPORTANT.md               (Troubleshooting)
├── REAL-DATASOURCES.md              (Datasource details)
├── PRE-WIRED-SETUP.md               (Config explanation)
├── READY-TO-TEST.md                 ⭐ THIS FILE
│
├── Datasource Notebooks (6): ⭐ ALL CONFIGURED
│   ├── Datasource-Sakila.ipynb
│   ├── Datasource-Chinook.ipynb
│   ├── Datasource-Northwind.ipynb
│   ├── Datasource-Employees.ipynb
│   ├── Datasource-World.ipynb
│   └── Datasource-AirportDB.ipynb
│
├── Feature Showcases (2): ⭐ ALL CONFIGURED
│   ├── MySQL-Features-Showcase.ipynb
│   └── PostgreSQL-Features-Showcase.ipynb
│
└── Tutorial Notebooks (6):
    ├── Calliope-GettingStarted.ipynb
    ├── Calliope-AdvancedQueries.ipynb
    ├── Calliope-RAGTraining.ipynb
    ├── Calliope-DirectSQL.ipynb
    ├── Calliope-Visualizations.ipynb
    └── Calliope-JupyterAI-Integration.ipynb
```

## 🎉 You're Ready!

All notebooks are configured and ready to test. Pick any notebook and start querying!

**Recommended first test**: `Datasource-Sakila.ipynb` (familiar DVD rental domain)
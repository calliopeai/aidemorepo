# 🔌 Using Real Calliope Datasources

This repository includes notebooks that connect to **real, pre-configured sample databases** via the Calliope API server running on port 5000.

## 🚀 Available Datasources

The following sample databases are available and ready to use:

### 1. 🎬 Sakila (MySQL)
**Datasource ID**: `sakila`
**Type**: DVD Rental Store
**Notebook**: `Calliope-RealData-Sakila.ipynb`

**Contains**:
- Films, actors, and categories
- Customer rentals and returns
- Inventory management
- Payment transactions
- Store locations

**Best for**: Retail analytics, inventory management, customer behavior analysis

---

### 2. 🎵 Chinook (PostgreSQL)
**Datasource ID**: `chinook`
**Type**: Digital Music Store
**Notebook**: `Calliope-RealData-Chinook.ipynb`

**Contains**:
- Artists, albums, and tracks
- Customers and invoices
- Playlists
- Employees (sales support)
- Genre and media type data

**Best for**: E-commerce analytics, customer segmentation, music industry analysis

---

### 3. 📦 Northwind (PostgreSQL)
**Datasource ID**: `northwind`
**Type**: Import/Export Business
**Notebook**: `Calliope-RealData-Northwind.ipynb`

**Contains**:
- Products and categories
- Orders and order details
- Customers and suppliers
- Employees and territories
- Shipping companies

**Best for**: Business operations, supply chain analysis, sales performance

---

### 4. 👔 Employees (MySQL)
**Datasource ID**: `employees`
**Type**: HR Database
**Notebook**: Coming soon!

**Contains**:
- Employee records
- Salaries and titles
- Department assignments
- Manager relationships

**Best for**: HR analytics, organizational analysis, compensation studies

---

### 5. 🌍 World (MySQL)
**Datasource ID**: `world`
**Type**: Geographic Data
**Notebook**: Coming soon!

**Contains**:
- Countries and cities
- Population data
- Languages
- Geographic information

**Best for**: Geographic analysis, demographic studies

---

### 6. ✈️ AirportDB (MySQL)
**Datasource ID**: `airportdb`
**Type**: Airport Operations
**Notebook**: Coming soon!

**Contains**:
- Flight information
- Airport data
- Booking records
- Passenger data

**Best for**: Travel analytics, operations analysis

---

## 🔗 How to Connect

### Method 1: Use Pre-built Notebooks
Simply open any of the `Calliope-RealData-*.ipynb` notebooks and start running queries!

### Method 2: API Connection
Check available datasources programmatically:

```python
import requests

response = requests.get('http://localhost:5000/api/datasources')
datasources = response.json()['datasources']

for ds in datasources:
    print(f"{ds['id']}: {ds['name']} ({ds['dialect']})")
```

### Method 3: Direct Calliope Magic
Use any datasource directly in your notebooks:

```python
%%calliope ask-sql sakila
What are the top 10 most rented films?
```

```python
%%calliope ask-sql chinook
Show me the top-selling music genres
```

```python
%%calliope ask-sql northwind
Which products are our bestsellers?
```

## 📊 API Endpoints

### Public Endpoint (No Auth Required)
```bash
GET http://localhost:5000/api/datasources
```

Returns list of all available datasources with:
- `id`: Datasource identifier
- `name`: Display name
- `dialect`: Database type (mysql, postgres, etc.)
- `description`: Brief description

### Admin Endpoint (Requires Auth)
```bash
GET http://localhost:5000/api/admin/datasources
Authorization: Bearer <admin_token>
```

Returns detailed configuration including connection details.

## 🎯 Quick Start

1. **Verify API is Running**
```bash
curl http://localhost:5000/api/datasources
```

2. **Open a Real Data Notebook**
   - Start with `Calliope-RealData-Sakila.ipynb` for retail analytics
   - Or `Calliope-RealData-Chinook.ipynb` for e-commerce
   - Or `Calliope-RealData-Northwind.ipynb` for business operations

3. **Run Your First Query**
```python
%%calliope ask-sql sakila
How many films are in the catalog?
```

## 💡 Benefits of Real Datasources

### No Setup Required
- Databases are pre-configured
- No need to install MySQL or PostgreSQL locally
- No connection string management

### Rich, Realistic Data
- Thousands of real records
- Complex relationships between tables
- Industry-standard schemas

### Learn Best Practices
- See how professional databases are structured
- Practice with real-world queries
- Understand common data patterns

### Immediate Results
- Start querying instantly
- No sample data generation needed
- Focus on learning, not setup

## 🔧 Configuration

Datasources are configured in two ways:

### 1. Database Storage (Primary)
Stored in the `datasources` table via SQLAlchemy ORM

### 2. Environment Variables (Fallback)
Defined in `env.example` under `sql_datasources`

The system automatically:
- Tries database first
- Falls back to config if database unavailable
- Merges both sources in the public API endpoint

## 🎓 Learning Path with Real Data

### Beginner
1. Start with `Calliope-GettingStarted.ipynb` (uses SQLite)
2. Move to `Calliope-RealData-Sakila.ipynb` (simple retail data)
3. Try basic queries on all datasources

### Intermediate
1. Explore `Calliope-RealData-Chinook.ipynb` (more complex relationships)
2. Work through `Calliope-RealData-Northwind.ipynb` (business operations)
3. Practice complex joins and aggregations

### Advanced
1. Combine multiple datasources for comparative analysis
2. Use RAG training with real schema information
3. Build automated reporting pipelines

## 🚨 Important Notes

- **Read-Only Access**: Sample databases are read-only for safety
- **Shared Resource**: Multiple users may access these databases
- **Performance**: Queries are optimized but may vary based on load
- **Data Persistence**: Data is reset periodically to maintain consistency

## 🔒 Security

- Public API endpoint requires no authentication
- Only read operations are permitted
- Connection details are hidden from clients
- Admin operations require authentication

## 📚 Example Queries

### Sakila (DVD Rental)
```python
%%calliope ask-sql sakila --sql-model anthropic
What are the most rented film categories and their total revenue?
```

### Chinook (Music Store)
```python
%%calliope ask-sql chinook --sql-model anthropic
Which artists generate the most revenue and from which countries?
```

### Northwind (Business)
```python
%%calliope ask-sql northwind --sql-model anthropic
Analyze customer lifetime value and identify our most valuable customer segments
```

## 🎯 Pro Tips

1. **Use Model Selection**: Add `--sql-model anthropic` for complex queries
2. **Enable AI Analysis**: Use `--to-ai --model claude3` for deeper insights
3. **Compare Approaches**: Try the same question on different datasources
4. **Learn SQL**: Use `generate-sql` to see the SQL before execution
5. **Direct Control**: Use `run-sql` for your own custom queries

## 🤝 Contributing

Want to add more example queries? Please contribute:
1. Create queries for existing datasources
2. Document interesting patterns you discover
3. Share your notebooks with the community

## 🆘 Troubleshooting

### Can't Connect to API?
```bash
# Check if API is running
curl http://localhost:5000/api/datasources

# Should return JSON with datasource list
```

### Datasource Not Found?
```python
# List all available datasources
import requests
response = requests.get('http://localhost:5000/api/datasources')
print(response.json())
```

### Query Timeout?
- Try a simpler query first
- Use LIMIT to reduce result set
- Consider the shared resource load

## 📖 Additional Resources

- [Calliope Documentation](https://docs.calliopeai.com)
- [Sakila Database Documentation](https://dev.mysql.com/doc/sakila/en/)
- [Chinook Database Schema](https://github.com/lerocha/chinook-database)
- [Northwind Database Guide](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases)

---

**Ready to start?** Open `Calliope-RealData-Sakila.ipynb` and run your first query! 🚀
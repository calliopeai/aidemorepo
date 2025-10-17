# ✅ Pre-Wired Configuration Complete!

## What Was Done

The Calliope API endpoint has been **pre-configured** in your Jupyter environment!

### Configuration Added To:
**File**: `~/.jupyter/jupyter_server_config.py`

```python
# Calliope Data Agent Configuration
os.environ['CALLIOPE_API_BASE_URL'] = os.environ.get('DATA_AGENT_URL', 'http://localhost:5000')

# Also set for notebook subprocesses
c.ServerApp.terminado_settings = {
    'shell_command': [os.environ.get('SHELL', 'bash')],
    'extra_env': {
        'CALLIOPE_API_BASE_URL': os.environ.get('DATA_AGENT_URL', 'http://localhost:5000')
    }
}
```

## What This Means

✅ **The `%%calliope` magic commands will automatically work!**

No need to configure each notebook - the environment variable is set when Jupyter starts.

## Activation

The configuration will be active after you **restart Jupyter**:

```bash
# Restart your Jupyter server
# The config will automatically load on startup
```

## Verification

Test that it's working:

```python
import os
print(f"CALLIOPE_API_BASE_URL: {os.environ.get('CALLIOPE_API_BASE_URL')}")
# Should print: http://localhost:5000 (or http://data-agent:5000 if in Docker)
```

## How It Works

1. When Jupyter Server starts, it loads `jupyter_server_config.py`
2. The config sets `CALLIOPE_API_BASE_URL` environment variable
3. All notebooks inherit this environment variable
4. The `%%calliope` magic commands automatically use this URL
5. **No per-notebook configuration needed!**

## Environment Variable Priority

The configuration uses this priority order:

1. **Docker/JupyterHub**: Uses `DATA_AGENT_URL` env var if set (e.g., `http://data-agent:5000`)
2. **Local Development**: Falls back to `http://localhost:5000`
3. **Custom**: Set `DATA_AGENT_URL` in your shell/docker-compose to override

### For Docker Users
```yaml
# In docker-compose.yml or similar
environment:
  DATA_AGENT_URL: http://data-agent:5000
```

### For Local Users
```bash
# In your shell before starting Jupyter
export DATA_AGENT_URL=http://localhost:5000
jupyter notebook
```

## Testing

After restarting Jupyter, try any datasource notebook:

```python
%%calliope run-sql sakila
SHOW TABLES
```

Should work immediately without any configuration cells!

## Troubleshooting

If magic commands still don't work:

### 1. Check if Variable is Set
```python
import os
print(os.environ.get('CALLIOPE_API_BASE_URL', 'NOT SET'))
```

### 2. Verify Data Agent is Running
```bash
curl http://localhost:5000/api/datasources
```

### 3. Check Jupyter Config Was Loaded
Look for this message when Jupyter starts:
```
✅ Calliope pre-configured: http://localhost:5000
```

### 4. Manual Override (if needed)
Add to top of any notebook:
```python
import os
os.environ['CALLIOPE_API_BASE_URL'] = 'http://localhost:5000'
```

## Files Updated

1. **`~/.jupyter/jupyter_server_config.py`** - Pre-configuration added (lines 670-685)
2. **`00-Setup-Calliope.ipynb`** - Setup notebook (optional, for testing)
3. **`README-IMPORTANT.md`** - Troubleshooting guide
4. **This file** - Documentation of pre-wiring

## Next Steps

1. **Restart Jupyter** to activate the configuration
2. **Open any datasource notebook** (e.g., `Datasource-Sakila.ipynb`)
3. **Run cells** - magic commands should work immediately!

## Alternative: Manual Configuration (Not Needed!)

If you prefer manual control, you can still add configuration to individual notebooks:

```python
import os
os.environ['CALLIOPE_API_BASE_URL'] = 'http://your-custom-url:5000'
```

But with pre-wiring, **this is no longer necessary**!

---

**🎉 Your Calliope environment is now pre-wired and ready to use!**
#!/usr/bin/env python3
"""
Test script to understand the calliope magic command
"""

import os
import sys

# Check environment variables
print("="*60)
print("ENVIRONMENT VARIABLES")
print("="*60)
calliope_url = os.environ.get('CALLIOPE_API_BASE_URL')
data_agent_url = os.environ.get('DATA_AGENT_URL')
print(f"CALLIOPE_API_BASE_URL: {calliope_url}")
print(f"DATA_AGENT_URL: {data_agent_url}")
print()

# Check if IPython/Jupyter is available
try:
    from IPython import get_ipython
    ip = get_ipython()
    if ip:
        print("="*60)
        print("AVAILABLE MAGIC COMMANDS")
        print("="*60)
        magics = ip.magics_manager.magics
        line_magics = list(magics.get('line', {}).keys())
        cell_magics = list(magics.get('cell', {}).keys())

        print(f"\nLine magics ({len(line_magics)}):")
        print([m for m in line_magics if 'ai' in m.lower() or 'calliope' in m.lower()])

        print(f"\nCell magics ({len(cell_magics)}):")
        print([m for m in cell_magics if 'ai' in m.lower() or 'calliope' in m.lower()])

        # Check if 'calliope' magic exists
        if 'calliope' in cell_magics:
            print("\n✅ 'calliope' cell magic is available!")
            # Try to get its docstring
            try:
                magic_func = magics['cell']['calliope']
                print(f"\nDocstring: {magic_func.__doc__}")
            except Exception as e:
                print(f"Could not get docstring: {e}")
        else:
            print("\n❌ 'calliope' cell magic is NOT available")
            print("Available cell magics:", cell_magics[:20])
    else:
        print("Not running in IPython environment")
except ImportError:
    print("IPython not available")

# Check if calliope package/module exists
print("\n" + "="*60)
print("CALLIOPE PACKAGE CHECK")
print("="*60)

try:
    import calliope
    print(f"✅ calliope module found at: {calliope.__file__}")
except ImportError:
    print("❌ No 'calliope' module found")

try:
    import calliope_magic
    print(f"✅ calliope_magic module found at: {calliope_magic.__file__}")
except ImportError:
    print("❌ No 'calliope_magic' module found")

try:
    import calliope_lab_proxy
    print(f"✅ calliope_lab_proxy module found at: {calliope_lab_proxy.__file__}")
except ImportError:
    print("❌ No 'calliope_lab_proxy' module found")

# Check jupyter_ai_magics
try:
    import jupyter_ai_magics
    print(f"✅ jupyter_ai_magics found at: {jupyter_ai_magics.__file__}")

    # Check for any calliope-related attributes
    calliope_attrs = [attr for attr in dir(jupyter_ai_magics) if 'calliope' in attr.lower()]
    if calliope_attrs:
        print(f"  Calliope-related attributes: {calliope_attrs}")
except ImportError:
    print("❌ jupyter_ai_magics not found")

print("\n" + "="*60)

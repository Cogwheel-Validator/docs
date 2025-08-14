# Quick Start: Generate MDX Files with Jinja2

This guide shows you the essential steps to generate MDX files correctly using Jinja2 templates.

## 🚀 The 5-Step Process

### 1. **Setup Jinja2 Environment** (Critical!)
```python
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(),
    trim_blocks=True,      # ⚠️ ESSENTIAL for clean output
    lstrip_blocks=True,    # ⚠️ ESSENTIAL for clean output
)
```

### 2. **Load Template**
```python
template = env.get_template("networks/network_index.j2")
```

### 3. **Prepare Data Context**
```python
context = {
    "network": {
        "name": "Network Name",
        "chain_id": "chain-id-1",
        # ... all required variables
    }
}
```

### 4. **Render Template**
```python
rendered_content = template.render(**context)
```

### 5. **Write to File**
```python
with output_file.open("w", encoding="utf-8") as f:
    f.write(rendered_content)
```

## ⚠️ Common Mistakes to Avoid

### ❌ **Wrong Environment Setup**
```python
# DON'T DO THIS - will cause whitespace issues
env = Environment(loader=FileSystemLoader(template_dir))

# DO THIS INSTEAD
env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True,      # ← This is crucial!
    lstrip_blocks=True,    # ← This is crucial!
)
```

### ❌ **Wrong File Paths**
```python
# DON'T DO THIS - will cause template not found errors
env = Environment(loader=FileSystemLoader("./templates"))

# DO THIS INSTEAD
env = Environment(loader=FileSystemLoader(Path("./templates")))
```

### ❌ **Missing Template Variables**
```python
# DON'T DO THIS - will cause UndefinedError
template.render()  # Missing context

# DO THIS INSTEAD
template.render(network=network_data)
```

### ❌ **Wrong File Encoding**
```python
# DON'T DO THIS - may cause encoding issues
with open("file.mdx", "w") as f:
    f.write(content)

# DO THIS INSTEAD
with open("file.mdx", "w", encoding="utf-8") as f:
    f.write(content)
```

## ✅ **Correct Complete Example**

```python
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_mdx_file():
    # 1. Setup environment CORRECTLY
    template_dir = Path("./templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(),
        trim_blocks=True,      # ← Essential!
        lstrip_blocks=True,    # ← Essential!
    )
    
    # 2. Load template
    template = env.get_template("networks/network_index.j2")
    
    # 3. Prepare context
    context = {
        "network": {
            "name": "My Network",
            "description": "Network description",
            "chain_id": "my-chain-1",
            "image": "mynetwork",
            "chain_version": "v1.0.0",
            "network_type": "Mainnet",
            "rest_api": "https://api.example.com",
            "rpc": "https://rpc.example.com",
            "grpc": "https://grpc.example.com",
            "wss": "wss://rpc.example.com"
        }
    }
    
    # 4. Render template
    rendered_content = template.render(**context)
    
    # 5. Write to file CORRECTLY
    output_file = Path("./output/network.mdx")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open("w", encoding="utf-8") as f:
        f.write(rendered_content)
    
    print(f"Generated: {output_file}")
```

## 🧪 **Test Your Setup**

Before generating real files, test your templates:

```bash
# Test if templates work correctly
uv run test_templates.py

# Run examples to see output
uv run example_usage.py
```

## 📁 **Template Structure**

Your templates should be organized like this:
```
templates/
└── networks/
    ├── network_index.j2      # Main network page
    ├── node_setup.j2         # Setup guide
    ├── validator_setup.j2    # Validator guide
    └── node_commands.j2      # Commands reference
```

## 🔍 **Debugging Tips**

### Check Template Variables
```python
# See what variables template expects
try:
    template.render()  # This will fail but show missing variables
except Exception as e:
    print(f"Missing variables: {e}")
```

### Verify Template Loading
```python
# Check if template loads
try:
    template = env.get_template("path/to/template.j2")
    print("✓ Template loaded")
except Exception as e:
    print(f"✗ Template error: {e}")
```

### Check Output
```python
# Always preview generated content
print("Generated content:")
print("-" * 50)
print(rendered_content)
print("-" * 50)
```

## 🎯 **Key Takeaways**

1. **Always use `trim_blocks=True` and `lstrip_blocks=True`**
2. **Use `Path` objects for file operations**
3. **Always specify `encoding="utf-8"` when writing files**
4. **Test templates before using them in production**
5. **Provide all required template variables**

## 🚨 **If Something Goes Wrong**

1. **Run `test_templates.py`** - identifies template issues
2. **Check file paths** - ensure templates exist
3. **Verify template variables** - ensure all required data is provided
4. **Check Jinja2 environment** - ensure proper settings
5. **Test with simple data** - start with minimal context

## 📚 **Next Steps**

- Read the full `README.md` for detailed information
- Check `JINJA2_MDX_GUIDE.md` for advanced usage
- Run examples to see working code
- Customize templates for your needs

---

**Remember**: The key to success is proper Jinja2 environment setup with `trim_blocks=True` and `lstrip_blocks=True`!

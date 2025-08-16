# Jinja2 MDX Generation Guide

This guide explains how to correctly generate MDX files using Jinja2 templates in this project.

## Overview

The project uses Jinja2 templates to generate MDX documentation files for different blockchain networks. Each network gets its own set of documentation files generated from templates and configuration data.

## Key Components

### 1. Jinja2 Environment Setup

```python
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(),
    trim_blocks=True,      # Remove leading/trailing whitespace from blocks
    lstrip_blocks=True,    # Remove leading whitespace from blocks
)
```

**Important settings:**
- `trim_blocks=True`: Removes whitespace around Jinja2 blocks
- `lstrip_blocks=True`: Removes leading whitespace from blocks
- `autoescape=select_autoescape()`: Automatically escapes HTML content

### 2. Template Structure

Templates are stored in `templates/networks/` and use the `.j2` extension:

- `network_index.j2` - Main network overview page
- `node_setup.j2` - Node installation and setup guide
- `validator_setup.j2` - Validator setup guide
- `node_commands.j2` - Common node commands

### 3. Template Variables

Templates expect a specific data structure. Here's the main pattern:

```python
template_context = {
    "network": {
        "name": "Network Name",
        "description": "Network description",
        "chain_id": "chain-id-1",
        "binary_name": "binaryd",
        "home_dir": "homedir",
        # ... other fields
    }
}
```

## Template Rendering Process

### Step 1: Load Template
```python
template = env.get_template("networks/network_index.j2")
```

### Step 2: Prepare Data Context
```python
context = {
    "network": {
        "name": network.name,
        "chain_id": network.chain_id,
        # ... map all required fields
    }
}
```

### Step 3: Render Template
```python
rendered_content = template.render(**context)
```

### Step 4: Write to File
```python
with output_file.open("w", encoding="utf-8") as f:
    f.write(rendered_content)
```

## Template Syntax Examples

### Basic Variable Usage
```jinja2
---
title: "{{ network.name }}"
description: "{{ network.description }}"
---

# {{ network.name }}

Chain ID: {{ network.chain_id }}
```

### Conditional Logic
```jinja2
{% if network.network_type == "Mainnet" %}
This is a mainnet network
{% else %}
This is a testnet network
{% endif %}
```

### Loops
```jinja2
{% for endpoint in network.endpoints %}
- {{ endpoint.name }}: {{ endpoint.url }}
{% endfor %}
```

### Include Other Templates
```jinja2
{% include "partials/network_info.j2" %}
```

## Common Issues and Solutions

### 1. Template Not Found
**Problem:** `TemplateNotFound` error
**Solution:** Check template path and ensure `FileSystemLoader` points to correct directory

```python
# Correct
template_dir = Path("./templates")
env = Environment(loader=FileSystemLoader(template_dir))

# Wrong
env = Environment(loader=FileSystemLoader("./templates"))
```

### 2. Variable Not Defined
**Problem:** `UndefinedError` for template variables
**Solution:** Ensure all template variables are provided in context

```python
# Check what variables template expects
template = env.get_template("template.j2")
print(template.module.__annotations__)  # Shows required variables
```

### 3. Whitespace Issues
**Problem:** Extra whitespace in output
**Solution:** Use `trim_blocks=True` and `lstrip_blocks=True`

```python
env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True,
    lstrip_blocks=True,
)
```

### 4. Encoding Issues
**Problem:** Special characters not rendering correctly
**Solution:** Always specify encoding when writing files

```python
with file.open("w", encoding="utf-8") as f:
    f.write(content)
```

## Best Practices

### 1. Template Organization
- Keep templates in logical subdirectories
- Use descriptive names for templates
- Separate reusable components into partial templates

### 2. Data Validation
- Validate data before passing to templates
- Provide default values for optional fields
- Handle missing data gracefully

### 3. Error Handling
- Wrap template rendering in try-catch blocks
- Log errors for debugging
- Provide fallback content when possible

### 4. Performance
- Reuse Jinja2 Environment instances
- Pre-compile frequently used templates
- Cache rendered content when appropriate

## Example Usage

See `example_usage.py` for complete working examples of:
- Single file generation
- Multiple network file generation
- Template context preparation
- File output handling

## Running the Generator

```bash
# From the mdx_gen directory
cd mdx_gen

# Run the main generator
python main.py

# Run examples
python example_usage.py
```

## Template Development Tips

1. **Test templates incrementally** - Start with simple variables
2. **Use template inheritance** - Create base templates for common layouts
3. **Validate output** - Check generated MDX files render correctly
4. **Keep templates focused** - Each template should have a single responsibility
5. **Document template requirements** - List all required variables in template comments

## Troubleshooting

### Debug Template Variables
```python
# Print all available variables
print("Available variables:", list(context.keys()))
print("Network data:", context.get("network", {}))
```

### Check Template Syntax
```python
# Validate template syntax
try:
    template = env.get_template("template.j2")
    print("Template loaded successfully")
except Exception as e:
    print(f"Template error: {e}")
```

### Verify Output
```python
# Check generated content
print("Generated content:")
print("-" * 50)
print(rendered_content)
print("-" * 50)
```

This guide should help you generate MDX files correctly using Jinja2 templates. For specific issues, check the example files and error messages for guidance.

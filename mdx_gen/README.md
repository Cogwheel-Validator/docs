# MDX Generator

A Python-based tool for generating MDX documentation files using Jinja2 templates.

## Overview

This tool generates MDX documentation files for blockchain networks by combining:
- Configuration data from YAML files
- Network information from REST API calls
- Jinja2 templates for consistent formatting

## Features

- **Template-based generation**: Uses Jinja2 templates for consistent MDX output
- **Multi-network support**: Generates documentation for both mainnets and testnets
- **Dynamic content**: Fetches live network data via REST APIs
- **Structured output**: Creates organized directory structures for each network
- **Multiple document types**: Generates index, setup, and command documentation

## Quick Start

### 1. Install Dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

### 2. Run the Generator

```bash
# Generate all MDX files
uv run main.py

# Test templates first
uv run test_templates.py

# Run examples
uv run example_usage.py
```

## How to Generate MDX Files Correctly

### 1. Jinja2 Environment Setup

```python
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(),
    trim_blocks=True,      # Remove whitespace around blocks
    lstrip_blocks=True,    # Remove leading whitespace from blocks
)
```

**Key Settings:**
- `trim_blocks=True`: Removes whitespace around Jinja2 blocks
- `lstrip_blocks=True`: Removes leading whitespace from blocks
- `autoescape=select_autoescape()`: Automatically escapes HTML content

### 2. Template Loading

```python
# Load a specific template
template = env.get_template("networks/network_index.j2")

# Template paths are relative to the template directory
template = env.get_template("networks/node_setup.j2")
```

### 3. Data Context Preparation

```python
# Prepare the data context that matches template expectations
context = {
    "network": {
        "name": "Network Name",
        "description": "Network description",
        "chain_id": "chain-id-1",
        "binary_name": "binaryd",
        "home_dir": "homedir",
        "go_version": "1.21.0",
        # ... other required fields
    }
}
```

### 4. Template Rendering

```python
# Render the template with data
rendered_content = template.render(**context)

# Or render with specific variables
rendered_content = template.render(network=network_data)
```

### 5. File Output

```python
# Write rendered content to file
output_file = Path("./output/network.mdx")
output_file.parent.mkdir(parents=True, exist_ok=True)

with output_file.open("w", encoding="utf-8") as f:
    f.write(rendered_content)
```

## Template Structure

### Available Templates

- `networks/network_index.j2` - Main network overview page
- `networks/node_setup.j2` - Node installation and setup guide
- `networks/validator_setup.j2` - Validator setup guide
- `networks/node_commands.j2` - Common node commands

### Template Variables

Each template expects specific variables. Here's the main pattern:

```jinja2
---
title: "{{ network.name }}"
description: "{{ network.description }}"
---

# {{ network.name }}

Chain ID: {{ network.chain_id }}
Binary: {{ network.binary_name }}
```

### Template Features

- **Frontmatter**: YAML metadata at the top of MDX files
- **Markdown**: Standard markdown syntax with Jinja2 variables
- **Conditionals**: `{% if %}` statements for dynamic content
- **Loops**: `{% for %}` loops for repeated content
- **Includes**: `{% include %}` for reusable components

## Configuration

### YAML Config Files

The generator reads from two configuration files:

- `data/mainnets.yml` - Mainnet network configurations
- `data/testnets.yml` - Testnet network configurations

### Config Structure

```yaml
networks:
  - name: "Network Name"
    binary_name: "binaryd"
    home_dir: "homedir"
    chain_id: "chain-id-1"
    minimum_gas_prices: "0.1utoken"
    validator_amount: "1000000utoken"
    path: "network-path"
```

## Usage Examples

### Basic Template Rendering

```python
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Setup environment
env = Environment(
    loader=FileSystemLoader("./templates"),
    trim_blocks=True,
    lstrip_blocks=True,
)

# Load and render template
template = env.get_template("networks/network_index.j2")
content = template.render(network=network_data)

# Write to file
with open("output.mdx", "w") as f:
    f.write(content)
```

### Multiple Network Generation

```python
# Generate files for multiple networks
for network in networks:
    # Create network directory
    network_dir = Path(f"./output/{network['path']}")
    network_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate index file
    index_content = index_template.render(network=network)
    with (network_dir / "index.mdx").open("w") as f:
        f.write(index_content)
    
    # Generate setup file
    setup_content = setup_template.render(network=network)
    with (network_dir / "setup.mdx").open("w") as f:
        f.write(setup_content)
```

## Common Issues and Solutions

### Template Not Found

**Problem:** `TemplateNotFound` error
**Solution:** Check template path and ensure `FileSystemLoader` points to correct directory

```python
# Correct
template_dir = Path("./templates")
env = Environment(loader=FileSystemLoader(template_dir))

# Wrong
env = Environment(loader=FileSystemLoader("./templates"))
```

### Variable Not Defined

**Problem:** `UndefinedError` for template variables
**Solution:** Ensure all template variables are provided in context

```python
# Check what variables template expects
template = env.get_template("template.j2")
print(template.module.__annotations__)  # Shows required variables
```

### Whitespace Issues

**Problem:** Extra whitespace in output
**Solution:** Use `trim_blocks=True` and `lstrip_blocks=True`

```python
env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True,
    lstrip_blocks=True,
)
```

### Encoding Issues

**Problem:** Special characters not rendering correctly
**Solution:** Always specify encoding when writing files

```python
with file.open("w", encoding="utf-8") as f:
    f.write(content)
```

## Best Practices

1. **Template Organization**
   - Keep templates in logical subdirectories
   - Use descriptive names for templates
   - Separate reusable components into partial templates

2. **Data Validation**
   - Validate data before passing to templates
   - Provide default values for optional fields
   - Handle missing data gracefully

3. **Error Handling**
   - Wrap template rendering in try-catch blocks
   - Log errors for debugging
   - Provide fallback content when possible

4. **Performance**
   - Reuse Jinja2 Environment instances
   - Pre-compile frequently used templates
   - Cache rendered content when appropriate

## Testing

### Run Template Tests

```bash
uv run test_templates.py
```

This will:
- Test template loading
- Test template rendering with sample data
- Analyze template variable requirements
- Provide detailed feedback on any issues

### Test Individual Templates

```python
# Test a specific template
template = env.get_template("networks/network_index.j2")
test_data = {"network": {...}}
rendered = template.render(**test_data)
print(rendered)
```

## File Structure

```
mdx_gen/
├── src/                    # Source code
│   ├── main_operator.py   # Main generator class
│   ├── config_loader/     # Configuration loading
│   ├── context.py         # Data context classes
│   └── query_endpoints/   # API querying
├── templates/              # Jinja2 templates
│   └── networks/          # Network-specific templates
├── data/                   # Configuration files
│   ├── mainnets.yml       # Mainnet configurations
│   └── testnets.yml       # Testnet configurations
├── main.py                # Main entry point
├── test_templates.py      # Template testing
├── example_usage.py       # Usage examples
└── README.md              # This file
```

## Contributing

1. **Template Development**
   - Test templates with `test_templates.py`
   - Follow the established variable naming conventions
   - Document any new template variables

2. **Code Changes**
   - Update tests when modifying templates
   - Follow Python type hints and docstrings
   - Test with multiple network configurations

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

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Run `test_templates.py` to identify template issues
3. Review the example files for usage patterns
4. Check the Jinja2 documentation for advanced features

## License

This project is part of the documentation generation system for blockchain networks.

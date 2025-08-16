#!/usr/bin/env python3
"""
Test script to verify Jinja2 templates render correctly.
This helps debug template issues before running the full generator.
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape


def test_network_index_template():
    """Test the network_index.j2 template."""
    print("Testing network_index.j2 template...")
    
    # Set up Jinja2 environment
    template_dir = Path("./templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    
    try:
        template = env.get_template("networks/network_index.j2")
        print("✓ Template loaded successfully")
    except Exception as e:
        print(f"✗ Failed to load template: {e}")
        return False
    
    # Test data
    test_context = {
        "network": {
            "name": "Test Network",
            "description": "A test network for validation",
            "image": "test",
            "chain_id": "test-1",
            "chain_version": "v1.0.0",
            "network_type": "Mainnet",
            "rest_api": "https://test-api.cogwheel.zone",
            "rpc": "https://test-rpc.cogwheel.zone",
            "grpc": "https://test-grpc.cogwheel.zone",
            "wss": "wss://test-rpc.cogwheel.zone"
        }
    }
    
    try:
        rendered = template.render(**test_context)
        print("✓ Template rendered successfully")
        print("Generated content preview:")
        print("-" * 50)
        print(rendered[:300] + "..." if len(rendered) > 300 else rendered)
        print("-" * 50)
        return True
    except Exception as e:
        print(f"✗ Failed to render template: {e}")
        return False


def test_node_setup_template():
    """Test the node_setup.j2 template."""
    print("\nTesting node_setup.j2 template...")
    
    template_dir = Path("./templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    
    try:
        template = env.get_template("networks/node_setup.j2")
        print("✓ Template loaded successfully")
    except Exception as e:
        print(f"✗ Failed to load template: {e}")
        return False
    
    # Test data
    test_context = {
        "network": {
            "name": "Test Network",
            "binary_name": "testd",
            "home_dir": "test",
            "chain_id": "test-1",
            "go_version": "1.21.0",
            "repo_url": "https://github.com/test/network",
            "repo_name": "test",
            "version": "v1.0.0",
            "genesis_url": "https://files.cogwheel.zone/test/genesis.json",
            "genesis_file": "test_genesis.tar.xz",
            "addrbook_url": "https://files.cogwheel.zone/test/addrbook.json"
        },
        "cosmovisor_recommended_version": "latest"
    }
    
    try:
        rendered = template.render(**test_context)
        print("✓ Template rendered successfully")
        print("Generated content preview:")
        print("-" * 50)
        print(rendered[:300] + "..." if len(rendered) > 300 else rendered)
        print("-" * 50)
        return True
    except Exception as e:
        print(f"✗ Failed to render template: {e}")
        return False


def test_template_variables():
    """Test what variables each template expects."""
    print("\nAnalyzing template variables...")
    
    template_dir = Path("./templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    
    templates_to_test = [
        "networks/network_index.j2",
        "networks/node_setup.j2",
        "networks/validator_setup.j2",
        "networks/node_commands.j2"
    ]
    
    for template_name in templates_to_test:
        try:
            template = env.get_template(template_name)
            print(f"\n{template_name}:")
            print(f"  ✓ Template loaded")
            
            # Try to get template info (this might not work in all Jinja2 versions)
            try:
                # This is a simple way to check if template has required variables
                # by trying to render with empty context
                template.render()
                print(f"  ✓ Template renders with empty context")
            except Exception as e:
                # This is expected - templates need variables
                print(f"  ℹ Template requires variables (expected): {str(e)[:100]}...")
                
        except Exception as e:
            print(f"  ✗ Failed to load: {e}")


def main():
    """Run all template tests."""
    print("Jinja2 Template Test Suite")
    print("=" * 40)
    
    # Test individual templates
    success1 = test_network_index_template()
    success2 = test_node_setup_template()
    
    # Analyze template variables
    test_template_variables()
    
    # Summary
    print("\n" + "=" * 40)
    print("Test Summary:")
    print(f"Network Index Template: {'✓ PASS' if success1 else '✗ FAIL'}")
    print(f"Node Setup Template: {'✓ PASS' if success2 else '✗ FAIL'}")
    
    if success1 and success2:
        print("\n🎉 All template tests passed! Templates are working correctly.")
    else:
        print("\n❌ Some template tests failed. Check the errors above.")


if __name__ == "__main__":
    main()

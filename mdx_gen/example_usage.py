#!/usr/bin/env python3
"""
Example script demonstrating how to use Jinja2 templates to generate MDX files correctly.
This shows the basic pattern for template rendering and file generation.
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape


def generate_simple_mdx_example():
    """Generate a simple MDX file using Jinja2 templates."""
    
    # 1. Set up Jinja2 environment
    template_dir = Path("./templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(),
        trim_blocks=True,  # Remove leading/trailing whitespace from blocks
        lstrip_blocks=True,  # Remove leading whitespace from blocks
    )
    
    # 2. Get the template
    template = env.get_template("networks/network_index.j2")
    
    # 3. Prepare the data context
    network_data = {
        "network": {
            "name": "Example Network",
            "description": "This is an example network for demonstration",
            "image": "example",
            "chain_id": "example-1",
            "chain_version": "v1.0.0",
            "network_type": "Mainnet",
            "rest_api": "https://example-api.cogwheel.zone",
            "rpc": "https://example-rpc.cogwheel.zone",
            "grpc": "https://example-grpc.cogwheel.zone",
            "wss": "wss://example-rpc.cogwheel.zone"
        }
    }
    
    # 4. Render the template
    rendered_content = template.render(**network_data)
    
    # 5. Write to file
    output_file = Path("./example_output.mdx")
    with output_file.open("w", encoding="utf-8") as f:
        f.write(rendered_content)
    
    print(f"Generated MDX file: {output_file}")
    print("Content preview:")
    print("-" * 50)
    print(rendered_content[:200] + "..." if len(rendered_content) > 200 else rendered_content)


def generate_multiple_networks_example():
    """Generate MDX files for multiple networks."""
    
    # Set up Jinja2 environment
    template_dir = Path("./templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    
    # Get templates
    network_index_template = env.get_template("networks/network_index.j2")
    node_setup_template = env.get_template("networks/node_setup.j2")
    
    # Sample network data
    networks = [
        {
            "name": "Juno Network",
            "path": "juno",
            "chain_id": "juno-1",
            "binary_name": "junod",
            "home_dir": "juno",
            "go_version": "1.21.0",
            "denom_version": "v1.0.0"
        },
        {
            "name": "Nibiru Chain",
            "path": "nibiru",
            "chain_id": "nibiru-1",
            "binary_name": "nibid",
            "home_dir": "nibid",
            "go_version": "1.21.0",
            "denom_version": "v1.0.0"
        }
    ]
    
    # Generate files for each network
    for network in networks:
        # Create network directory
        network_dir = Path(f"./example_output/{network['path']}")
        network_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate network index
        network_context = {
            "network": {
                "name": network["name"],
                "description": f"Documentation for {network['name']}",
                "image": network["path"],
                "chain_id": network["chain_id"],
                "chain_version": network["denom_version"],
                "network_type": "Mainnet",
                "rest_api": f"https://{network['path']}-api.cogwheel.zone",
                "rpc": f"https://{network['path']}-rpc.cogwheel.zone",
                "grpc": f"https://{network['path']}-grpc.cogwheel.zone",
                "wss": f"wss://{network['path']}-rpc.cogwheel.zone"
            }
        }
        
        index_content = network_index_template.render(**network_context)
        index_file = network_dir / "index.mdx"
        with index_file.open("w", encoding="utf-8") as f:
            f.write(index_content)
        
        # Generate node setup
        setup_context = {
            "network": {
                "name": network["name"],
                "binary_name": network["binary_name"],
                "home_dir": network["home_dir"],
                "chain_id": network["chain_id"],
                "go_version": network["go_version"],
                "repo_url": f"https://github.com/{network['path']}/network",
                "repo_name": network["path"],
                "version": network["denom_version"],
                "genesis_url": f"https://files.cogwheel.zone/{network['path']}/genesis.json",
                "genesis_file": f"{network['path']}_genesis.tar.xz",
                "addrbook_url": f"https://files.cogwheel.zone/{network['path']}/addrbook.json"
            },
            "cosmovisor_recommended_version": "latest"
        }
        
        setup_content = node_setup_template.render(**setup_context)
        setup_file = network_dir / "node-setup.mdx"
        with setup_file.open("w", encoding="utf-8") as f:
            f.write(setup_content)
        
        print(f"Generated files for {network['name']} in {network_dir}")


if __name__ == "__main__":
    print("Jinja2 MDX Generation Examples")
    print("=" * 40)
    
    # Example 1: Simple single file generation
    print("\n1. Simple MDX generation:")
    generate_simple_mdx_example()
    
    # Example 2: Multiple network files
    print("\n2. Multiple network files generation:")
    generate_multiple_networks_example()
    
    print("\nExamples completed! Check the 'example_output' directory for generated files.")

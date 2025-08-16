from pathlib import Path

from src.main_operator import MdxNetworkGenerator


def main():
    print("Starting MDX generation for networks...")

    # Define paths
    template_dir = Path("./templates")
    output_dir = Path("../content/networks")
    config_path = Path("./data/")

    # Create generator instance
    generator = MdxNetworkGenerator(
        template_dir=template_dir,
        output_dir=output_dir,
        config_path=config_path
    )

    # Generate all MDX files
    generator.generate_all()

    print("MDX generation completed!")


if __name__ == "__main__":
    main()

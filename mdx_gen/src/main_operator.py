from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from dataclasses import dataclass
from .config_loader import ConfigList
from .query_endpoints import query_node_info, NodeInfo

@dataclass
class MdxGenerator:
    """MdxGenerator class to generate the mdx files."""
    config_list: ConfigList
    output_dir: Path

    def generate_mdx(self) -> None:
        """Generate the mdx files."""
        for config in self.config_list.configs:
            self.generate_mdx_file(config)
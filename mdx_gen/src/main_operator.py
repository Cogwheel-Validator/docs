import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .config_loader import Config, ConfigList
from .context import NetworkContext
from .query_endpoints import NodeInfo, query_node_info


class MdxNetworkGenerator:
    def __init__(
        self,
        template_dir: Path,
        output_dir: Path = "./content/networks",
        config_path: Path = "./mdx_gen/data/",
    ):
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.config_list = ConfigList(config_path)
        self.mainnets, self.testnets = self.config_list.load_configs()

        self.mainnet_contexts: list[NetworkContext] = []
        self.testnet_contexts: list[NetworkContext] = []

    def _check_output(self) -> tuple[bool, bool, bool]:
        main, mainnet, testnet = False, False, False
        """Check if the output directory exists."""
        if not self.output_dir.exists():
            return main, mainnet, testnet
        if self.output_dir.joinpath("mainnets").exists():
            mainnet = True
        if self.output_dir.joinpath("testnets").exists():
            testnet = True
        if mainnet and testnet:
            main = True
        return main, mainnet, testnet

    def _solve_dirs(self) -> None:
        """It creates new dirs, backups and/or clears the output directory."""
        main_dir, mainnet_dir, testnet_dir = self._check_output()
        # If the dirs do not exist at all, create them
        match main_dir:
            case False:
                self.output_dir.mkdir(parents=True, exist_ok=True)
            case True:
                if not mainnet_dir:
                    self.output_dir.joinpath("mainnets").mkdir(parents=True, exist_ok=True)
                if not testnet_dir:
                    self.output_dir.joinpath("testnets").mkdir(parents=True, exist_ok=True)
                if mainnet_dir and testnet_dir:
                    # It means we are overwriting the existing dirs backup untill
                    # the process is compleate, backup the main dir
                    # if backup exists, remove it
                    if self.output_dir.with_suffix(".bak").exists():
                        shutil.rmtree(self.output_dir.with_suffix(".bak"))
                    self.output_dir.rename(self.output_dir.with_suffix(".bak"))
                    # Call the function again
                    self._solve_dirs()

        match mainnet_dir:
            case False:
                self.output_dir.joinpath("mainnets").mkdir(parents=True, exist_ok=True)
        match testnet_dir:
            case False:
                self.output_dir.joinpath("testnets").mkdir(parents=True, exist_ok=True)
    
    def _fill_network_contexts(self) -> None:
        """Fill the network contexts."""
        for config in self.mainnets.values():
            # make a REST API call to gather the node data
            # subdomain format is always identical hence this is a simple call
            api_url = f"https://{config.path}-api.cogwheel.zone"
            node_info: NodeInfo | None = query_node_info(api_url)
            if node_info is None:
                error_msg: Exception = Exception(
                    f"Failed to query REST endpoint: {api_url}")
                raise error_msg
            self.mainnet_contexts.append(
                NetworkContext(
                    name=config.name, binary_name=config.binary_name,
                    home_dir=config.home_dir, chain_id=config.chain_id,
                    minimum_gas_prices=config.minimum_gas_prices,
                    validator_amount=config.validator_amount, path=config.path,
                    denom_version=node_info.denom_version,
                    go_version=node_info.go_version,
                    cosmos_sdk_version=node_info.cosmos_sdk_version))
        for config in self.testnets.values():
            # make a REST API call to gather the node data
            # subdomain format is always identical hence this is a simple call
            api_url = f"https://{config.path}-testnet-api.cogwheel.zone"
            node_info: NodeInfo | None = query_node_info(api_url)
            if node_info is None:
                error_msg: Exception = Exception(
                    f"Failed to query REST endpoint: {api_url}")
                raise error_msg
            self.testnet_contexts.append(
                NetworkContext(
                    name=config.name, binary_name=config.binary_name,
                    home_dir=config.home_dir, chain_id=config.chain_id,
                    minimum_gas_prices=config.minimum_gas_prices,
                    validator_amount=config.validator_amount, path=config.path,
                    denom_version=node_info.denom_version,
                    go_version=node_info.go_version,
                    cosmos_sdk_version=node_info.cosmos_sdk_version))

    def _generate_network_mdx(self) -> None:
        """Generate the network_index mdx file.

        This function generates the network index page.
        It should populate the file under name index.mdx.
        """
        template = self.env.get_template("networks/main_index.j2")

        # Generate mainnet index
        mainnet_output = self.output_dir.joinpath("mainnets/index.mdx")
        mainnet_output.parent.mkdir(parents=True, exist_ok=True)

        # Create a context for the mainnet index template
        mainnet_data = {
            "networks": [
                {
                    "name": context.name,
                    "image": context.path.lower()+"Icon",
                    "chainId": context.chain_id,
                    "networkType": "mainnet",
                    "path": context.path,
                }
                for context in self.mainnet_contexts
            ],
            "network_type": "Mainnets",
        }

        with mainnet_output.open("w", encoding="utf-8") as f:
            f.write(template.render(**mainnet_data))

        # Generate testnet index
        testnet_output = self.output_dir.joinpath("testnets/index.mdx")
        testnet_output.parent.mkdir(parents=True, exist_ok=True)

        testnet_data = {
            "networks": [
                {
                    "name": context.name,
                    "image": context.path.lower()+"Icon",
                    "chainId": context.chain_id,
                    "networkType": "testnet",
                    "path": context.path,
                }
                for context in self.testnet_contexts
            ],
            "network_type": "Testnets",
        }

        with testnet_output.open("w", encoding="utf-8") as f:
            f.write(template.render(**testnet_data))

    def _generate_individual_network_files(self) -> None:
        """Generate individual network MDX files for each network."""

        # Generate mainnet files
        for context in self.mainnet_contexts:
            self._generate_network_files(context, "mainnets")

        # Generate testnet files
        for context in self.testnet_contexts:
            self._generate_network_files(context, "testnets")

    def _generate_network_files(self, context: NetworkContext, network_type: str) -> None:
        """Generate all MDX files for a specific network."""

        # Create network directory
        network_dir = self.output_dir.joinpath(network_type, context.path)
        network_dir.mkdir(parents=True, exist_ok=True)

        # Generate network index
        self._generate_network_index(context, network_dir)

        # Generate node setup
        self._generate_node_setup(context, network_dir)

        # Generate validator setup
        self._generate_validator_setup(context, network_dir)

        # Generate node commands
        self._generate_node_commands(context, network_dir)

    def _generate_network_index(self, context: NetworkContext, network_dir: Path) -> None:
        """Generate the network index MDX file."""
        template = self.env.get_template("networks/network_index.j2")
        network_type = "mainnets" if "mainnets" in str(network_dir) else "testnets"
        rest_api = f"https://{context.path.lower()}{'-testnet' if network_type == 'testnet' else ''}-api.cogwheel.zone"
        rpc = f"https://{context.path.lower()}{'-testnet' if network_type == 'testnet' else ''}-rpc.cogwheel.zone"
        grpc = f"{context.path.lower()}{'-testnet' if network_type == 'testnet' else ''}-grpc.cogwheel.zone:443"
        wss = f"wss://{context.path.lower()}{'-testnet' if network_type == 'testnet' else ''}-rpc.cogwheel.zone"
        # Create template context with all necessary data
        template_context = {
            "network": {
                "name": context.name,
                "description": f"Documentation for {context.name} {context.chain_id}",
                "image": context.path.lower()+"Icon",
                "chain_id": context.chain_id,
                "chain_version": context.denom_version,
                "network_type": network_type,
                "rest_api": rest_api,
                "rpc": rpc,
                "grpc": grpc,
                "wss": wss,
            },
        }

        output_file = network_dir.joinpath("index.mdx")
        with output_file.open("w", encoding="utf-8") as f:
            f.write(template.render(**template_context))

    def _generate_node_setup(self, context: NetworkContext, network_dir: Path) -> None:
        """Generate the node setup MDX file."""
        template = self.env.get_template("networks/node_setup.j2")

        # Create template context
        template_context = {
            "network": {
                "name": context.name,
                "binary_name": context.binary_name,
                "home_dir": context.home_dir,
                "chain_id": context.chain_id,
                "go_version": context.go_version,
                "repo_url": f"https://github.com/{context.path.lower()}/network",
                "repo_name": context.path.lower(),
                "version": context.denom_version,
                "genesis_url": f"https://files.cogwheel.zone/{context.path.lower()}/genesis.json",
                "genesis_file": f"{context.path.lower()}_genesis.tar.xz",
                "addrbook_url": f"https://files.cogwheel.zone/{context.path.lower()}/addrbook.json",
                "cosmos_sdk_version": context.cosmos_sdk_version,
            },
            "cosmovisor_recommended_version": "latest",
        }
        
        output_file = network_dir.joinpath("node-setup.mdx")
        with output_file.open("w", encoding="utf-8") as f:
            f.write(template.render(**template_context))
    
    def _generate_validator_setup(self, context: NetworkContext, network_dir: Path) -> None:
        """Generate the validator setup MDX file."""
        template = self.env.get_template("networks/validator_setup.j2")
        
        template_context = {
            "network": {
                "name": context.name,
                "binary_name": context.binary_name,
                "home_dir": context.home_dir,
                "chain_id": context.chain_id,
                "validator_amount": context.validator_amount,
                "minimum_gas_prices": context.minimum_gas_prices,
                "cosmos_sdk_version": context.cosmos_sdk_version,
            },
        }
        
        output_file = network_dir.joinpath("validator-setup.mdx")
        with output_file.open("w", encoding="utf-8") as f:
            f.write(template.render(**template_context))
    
    def _generate_node_commands(self, context: NetworkContext, network_dir: Path) -> None:
        """Generate the node commands MDX file."""
        template = self.env.get_template("networks/node_commands.j2")
        
        template_context = {
            "network": {
                "name": context.name,
                "binary_name": context.binary_name,
                "home_dir": context.home_dir,
                "chain_id": context.chain_id,
                "cosmos_sdk_version": context.cosmos_sdk_version,
            },
        }
        
        output_file = network_dir.joinpath("node-commands.mdx")
        with output_file.open("w", encoding="utf-8") as f:
            f.write(template.render(**template_context))
    
    def generate_all(self) -> None:
        """Generate all MDX files."""
        print("Starting MDX generation...")
        
        # Create output directories
        self._solve_dirs()
        
        # Fill network contexts with data
        print("Gathering network information...")
        self._fill_network_contexts()
        
        # Generate network index files
        print("Generating network index files...")
        self._generate_network_mdx()
        
        # Generate individual network files
        print("Generating individual network files...")
        self._generate_individual_network_files()
        
        print("MDX generation completed successfully!")
        
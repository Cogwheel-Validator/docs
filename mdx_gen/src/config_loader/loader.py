"""Loader for the configs."""
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class Config:
    """Config class to store the config.

    Args:
        name: Name of the network
        binary_name: Name of the binary
        home_dir: Home directory of the network
        chain_id: Chain ID of the network
        minimum_gas_prices: Minimum gas prices of the network
        validator_amount: Amount of validator of the network
        path: Path of the network

    """

    name: str
    binary_name: str
    home_dir: str
    chain_id: str
    minimum_gas_prices: str
    validator_amount: str
    path: str

@dataclass
class ConfigList:
    """ConfigList class to store the config list.

    Args:
        configs_path: Path to the configs file

    """

    configs_path: Path

    def load_configs(self) -> tuple[dict[str, Config], dict[str, Config]]:
        """Load the configs from the configs file.

        Returns:
            tuple[dict[str, Config], dict[str, Config]]: A tuple of dictionaries containing the mainnets and testnets configs.

        """  # noqa: E501
        with Path(self.configs_path).open("r") as files:
            # there should be 2 files in the configs path
            # mainnets.yml and testnets.yml
            mainnets = yaml.safe_load(files[0])
            testnets = yaml.safe_load(files[1])
        mainnets_dict: dict[str, Config] = {}
        testnets_dict: dict[str, Config] = {}
        for config in mainnets["networks"]:
            mainnets_dict[config["name"]] = Config(**config)
        for config in testnets["networks"]:
            testnets_dict[config["name"]] = Config(**config)
        validity, error = validate_config(mainnets_dict)
        if not validity:
            raise ValueError(error)
        validity, error = validate_config(testnets_dict)
        if not validity:
            raise ValueError(error)
        return mainnets_dict, testnets_dict

def validate_config(configs: dict[str, Config]) -> tuple[bool, Exception | None]:
    """Validate the configs.

    Args:
        configs: The configs to validate

    Returns:
        tuple[bool, Exception | None]: A tuple of a boolean indicating the validity of the config and an exception if the config is invalid.

    """  # noqa: E501
    # Empty configs dictionary is invalid
    if not configs:
        return False, Exception("No configs provided")

    needed_elements: list[str] = [
        "name",
        "binary_name",
        "home_dir",
        "chain_id",
        "minimum_gas_prices",
        "validator_amount",
        "path",
    ]
    error_msg: str = ""
    for name, config in configs.items():
        missing_elements = [
            ml for ml in needed_elements if not hasattr(config, ml)
        ]
        if missing_elements:
            error_msg += f"Config {name} is missing the following elements: {missing_elements}\n"  # noqa: E501
    if error_msg:
        return False, Exception(error_msg)
    return True, None

from dataclasses import dataclass


@dataclass
class NetworkContext:
    """NetworkContext class to store the context."""

    # From the Config class
    name: str
    binary_name: str
    home_dir: str
    chain_id: str
    minimum_gas_prices: str
    validator_amount: str
    path: str

    # From the REST API query
    denom_version: str
    go_version: str
    cosmos_sdk_version: float

    # Snapshots list
    snapshots: list[dict[str, str]]

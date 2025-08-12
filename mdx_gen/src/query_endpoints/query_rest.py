"""Query the REST endpoints for the node info."""
from dataclasses import dataclass
from http import HTTPStatus

import aiohttp


@dataclass
class NodeInfo:
    """NodeInfo class to store the node info."""

    denom_version: str
    go_version: str

async def query_node_info(api: str, params: dict | None = None) -> NodeInfo:
    """Query the REST endpoint for the node info.

    This function queries the REST API to gather the node info.
    Use case is to get the chain denom version and go version.

    Args:
        api: The API endpoint to query
        params: The parameters to pass to the API

    Returns:
        NodeInfo: The node info

    """
    url: str = "/cosmos/base/tendermint/v1beta1/node_info"
    with aiohttp.ClientSession() as session:
        async with session.get(api + url, params=params) as response:
            if response.status == HTTPStatus.OK:
                data = await response.json()
                return NodeInfo(
                    denom_version=data["node_info"]["version"],
                    go_version=data["node_info"]["go_version"].split(" ")[2],
                )
            error_msg: Exception = Exception(
                f"Failed to query REST endpoint: {response.status} {response.text}")
            raise error_msg

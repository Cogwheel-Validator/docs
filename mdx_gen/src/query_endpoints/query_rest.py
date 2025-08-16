"""Query the REST endpoints for the node info."""
from dataclasses import dataclass
from http import HTTPStatus

import httpx


@dataclass
class NodeInfo:
    """NodeInfo class to store the node info."""

    denom_version: str
    go_version: str
    cosmos_sdk_version: str

def query_node_info(api: str, params: dict | None = None) -> NodeInfo | None:
    """Query the REST endpoint for the node info.

    This function queries the REST API to gather the node info.
    Use case is to get the chain denom version and go version.

    Args:
        api: The API endpoint to query
        params: The parameters to pass to the API

    Returns:
        NodeInfo: The node info or None if the query failed

    """
    url: str = f"{api}/cosmos/base/tendermint/v1beta1/node_info"
    try:
        response = httpx.get(url, params=params, timeout=30)
        if response.status_code == HTTPStatus.OK:
            data = response.json()
            return NodeInfo(
                denom_version=data["application_version"]["version"],
                go_version=data["application_version"]["go_version"].split(" ")[2],
                cosmos_sdk_version = float(
                    str(data["application_version"]["cosmos_sdk_version"]).split("v")[1][:4]),
            )
    except httpx.HTTPStatusError as e:
        error_msg: Exception = Exception(
            f"Failed to query REST endpoint: {api} {e.response.status_code} {e.response.text}")
        raise error_msg from e
    except httpx.RequestError as e:
        error_msg: Exception = Exception(
            f"Failed to query REST endpoint: {api} {e}")
        raise error_msg from e
    except Exception as e:
        error_msg: Exception = Exception(
            f"Failed to query REST endpoint: {api} {e}")
        raise error_msg from e


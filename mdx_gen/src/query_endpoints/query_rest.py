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

def query_node_info(api: str, params: dict | None = None, timeout: int = 10) -> NodeInfo | None:
    """Query the REST endpoint for the node info.

    This function queries the REST API to gather the node info.
    Use case is to get the chain denom version and go version.

    Args:
        api: The API endpoint to query
        params: The parameters to pass to the API
        timeout: Timeout in seconds for the request (default: 10)

    Returns:
        NodeInfo: The node info or None if the query failed

    """
    url: str = f"{api}/cosmos/base/tendermint/v1beta1/node_info"
    print(f"Querying: {url} (timeout: {timeout}s)")

    try:
        # Use a more aggressive timeout configuration
        timeout_config = httpx.Timeout(timeout=timeout, connect=5.0)

        with httpx.Client(timeout=timeout_config) as client:
            response = client.get(url, params=params)

        if response.status_code == HTTPStatus.OK:
            data = response.json()
            print("  ✓ Query successful")
            return NodeInfo(
                denom_version=data["application_version"]["version"],
                go_version=data["application_version"]["go_version"].split(" ")[2],
                cosmos_sdk_version = float(
                    str(data["application_version"]["cosmos_sdk_version"]).split("v")[1][:4]),
            )
        else:
            print(f"✗ HTTP {response.status_code}: {response.text[:100]}...")
            return None

    except httpx.TimeoutException:
        print(f"✗ Request timed out after {timeout}s")
        return None
    except httpx.HTTPStatusError as e:
        print(f"✗ HTTP Status Error: {e.response.status_code}")
        return None
    except httpx.RequestError as e:
        print(f"✗ Request Error: {str(e)[:100]}...")
        return None
    except Exception as e:
        print(f"✗ Unexpected Error: {str(e)[:100]}...")
        return None


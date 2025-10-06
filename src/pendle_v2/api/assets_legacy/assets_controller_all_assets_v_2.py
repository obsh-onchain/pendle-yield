from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_csv_response import AssetCSVResponse
from ...types import Response


def _get_kwargs(
    chain_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/{chain_id}/assets/all",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AssetCSVResponse]:
    if response.status_code == 200:
        response_200 = AssetCSVResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssetCSVResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AssetCSVResponse]:
    """Get all assets in CSV

    Args:
        chain_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetCSVResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AssetCSVResponse]:
    """Get all assets in CSV

    Args:
        chain_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetCSVResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AssetCSVResponse]:
    """Get all assets in CSV

    Args:
        chain_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetCSVResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AssetCSVResponse]:
    """Get all assets in CSV

    Args:
        chain_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetCSVResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
        )
    ).parsed

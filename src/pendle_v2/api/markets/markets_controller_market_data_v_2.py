import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.market_data_response import MarketDataResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    address: str,
    *,
    timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_timestamp: Union[Unset, str] = UNSET
    if not isinstance(timestamp, Unset):
        json_timestamp = timestamp.isoformat()
    params["timestamp"] = json_timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/{chain_id}/markets/{address}/data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MarketDataResponse]:
    if response.status_code == 200:
        response_200 = MarketDataResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MarketDataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Response[MarketDataResponse]:
    """Get market latest detailed data by address

    Args:
        chain_id (float):
        address (str):
        timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketDataResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        timestamp=timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[MarketDataResponse]:
    """Get market latest detailed data by address

    Args:
        chain_id (float):
        address (str):
        timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketDataResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        address=address,
        client=client,
        timestamp=timestamp,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Response[MarketDataResponse]:
    """Get market latest detailed data by address

    Args:
        chain_id (float):
        address (str):
        timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketDataResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        timestamp=timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[MarketDataResponse]:
    """Get market latest detailed data by address

    Args:
        chain_id (float):
        address (str):
        timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketDataResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            address=address,
            client=client,
            timestamp=timestamp,
        )
    ).parsed

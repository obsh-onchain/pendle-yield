import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.market_implied_apy_response_entity import MarketImpliedApyResponseEntity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    address: str,
    *,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_timestamp_start: Union[Unset, str] = UNSET
    if not isinstance(timestamp_start, Unset):
        json_timestamp_start = timestamp_start.isoformat()
    params["timestamp_start"] = json_timestamp_start

    json_timestamp_end: Union[Unset, str] = UNSET
    if not isinstance(timestamp_end, Unset):
        json_timestamp_end = timestamp_end.isoformat()
    params["timestamp_end"] = json_timestamp_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/markets/{address}/implied-apy-chart",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MarketImpliedApyResponseEntity]:
    if response.status_code == 200:
        response_200 = MarketImpliedApyResponseEntity.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MarketImpliedApyResponseEntity]:
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
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[MarketImpliedApyResponseEntity]:
    """Get market implied apy chart

     Return implied APY chart of a market. Data is sampled every one minutes. The endpoint only support
    last 2 days of data

    Args:
        chain_id (float):
        address (str):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketImpliedApyResponseEntity]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
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
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[MarketImpliedApyResponseEntity]:
    """Get market implied apy chart

     Return implied APY chart of a market. Data is sampled every one minutes. The endpoint only support
    last 2 days of data

    Args:
        chain_id (float):
        address (str):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketImpliedApyResponseEntity
    """

    return sync_detailed(
        chain_id=chain_id,
        address=address,
        client=client,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[MarketImpliedApyResponseEntity]:
    """Get market implied apy chart

     Return implied APY chart of a market. Data is sampled every one minutes. The endpoint only support
    last 2 days of data

    Args:
        chain_id (float):
        address (str):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketImpliedApyResponseEntity]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[MarketImpliedApyResponseEntity]:
    """Get market implied apy chart

     Return implied APY chart of a market. Data is sampled every one minutes. The endpoint only support
    last 2 days of data

    Args:
        chain_id (float):
        address (str):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketImpliedApyResponseEntity
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            address=address,
            client=client,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
        )
    ).parsed

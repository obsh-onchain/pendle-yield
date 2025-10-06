import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transactions_response import TransactionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    *,
    market: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["market"] = market

    params["skip"] = skip

    params["limit"] = limit

    params["action"] = action

    params["origin"] = origin

    json_timestamp_start: Union[Unset, str] = UNSET
    if not isinstance(timestamp_start, Unset):
        json_timestamp_start = timestamp_start.isoformat()
    params["timestamp_start"] = json_timestamp_start

    json_timestamp_end: Union[Unset, str] = UNSET
    if not isinstance(timestamp_end, Unset):
        json_timestamp_end = timestamp_end.isoformat()
    params["timestamp_end"] = json_timestamp_end

    params["user"] = user

    params["minValue"] = min_value

    params["maxValue"] = max_value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v3/{chain_id}/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TransactionsResponse]:
    if response.status_code == 200:
        response_200 = TransactionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TransactionsResponse]:
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
    market: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
) -> Response[TransactionsResponse]:
    """Get user transactions

    Args:
        chain_id (float):
        market (str):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        action (Union[Unset, str]):
        origin (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]):
        min_value (Union[Unset, float]):
        max_value (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionsResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        market=market,
        skip=skip,
        limit=limit,
        action=action,
        origin=origin,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        user=user,
        min_value=min_value,
        max_value=max_value,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    market: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
) -> Optional[TransactionsResponse]:
    """Get user transactions

    Args:
        chain_id (float):
        market (str):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        action (Union[Unset, str]):
        origin (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]):
        min_value (Union[Unset, float]):
        max_value (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionsResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
        market=market,
        skip=skip,
        limit=limit,
        action=action,
        origin=origin,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        user=user,
        min_value=min_value,
        max_value=max_value,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    market: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
) -> Response[TransactionsResponse]:
    """Get user transactions

    Args:
        chain_id (float):
        market (str):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        action (Union[Unset, str]):
        origin (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]):
        min_value (Union[Unset, float]):
        max_value (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionsResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        market=market,
        skip=skip,
        limit=limit,
        action=action,
        origin=origin,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        user=user,
        min_value=min_value,
        max_value=max_value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    market: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
) -> Optional[TransactionsResponse]:
    """Get user transactions

    Args:
        chain_id (float):
        market (str):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        action (Union[Unset, str]):
        origin (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]):
        min_value (Union[Unset, float]):
        max_value (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionsResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
            market=market,
            skip=skip,
            limit=limit,
            action=action,
            origin=origin,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
            user=user,
            min_value=min_value,
            max_value=max_value,
        )
    ).parsed

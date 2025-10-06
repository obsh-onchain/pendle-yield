import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transactions_v4_response import TransactionsV4Response
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    *,
    market: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
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

    params["resumeToken"] = resume_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v4/{chain_id}/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TransactionsV4Response]:
    if response.status_code == 200:
        response_200 = TransactionsV4Response.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TransactionsV4Response]:
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
    market: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
) -> Response[TransactionsV4Response]:
    """Get raw transactions

    Args:
        chain_id (float):
        market (Union[Unset, str]):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        action (Union[Unset, str]):
        origin (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]):
        min_value (Union[Unset, float]):
        max_value (Union[Unset, float]):
        resume_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionsV4Response]
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
        resume_token=resume_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    market: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
) -> Optional[TransactionsV4Response]:
    """Get raw transactions

    Args:
        chain_id (float):
        market (Union[Unset, str]):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        action (Union[Unset, str]):
        origin (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]):
        min_value (Union[Unset, float]):
        max_value (Union[Unset, float]):
        resume_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionsV4Response
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
        resume_token=resume_token,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    market: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
) -> Response[TransactionsV4Response]:
    """Get raw transactions

    Args:
        chain_id (float):
        market (Union[Unset, str]):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        action (Union[Unset, str]):
        origin (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]):
        min_value (Union[Unset, float]):
        max_value (Union[Unset, float]):
        resume_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionsV4Response]
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
        resume_token=resume_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    market: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    action: Union[Unset, str] = UNSET,
    origin: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, str] = UNSET,
    min_value: Union[Unset, float] = UNSET,
    max_value: Union[Unset, float] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
) -> Optional[TransactionsV4Response]:
    """Get raw transactions

    Args:
        chain_id (float):
        market (Union[Unset, str]):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        action (Union[Unset, str]):
        origin (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]):
        min_value (Union[Unset, float]):
        max_value (Union[Unset, float]):
        resume_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionsV4Response
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
            resume_token=resume_token,
        )
    ).parsed

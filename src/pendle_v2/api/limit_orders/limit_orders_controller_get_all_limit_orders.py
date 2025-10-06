import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.limit_orders_v2_response import LimitOrdersV2Response
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    chain_id: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = 100.0,
    maker: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chainId"] = chain_id

    params["limit"] = limit

    params["maker"] = maker

    params["yt"] = yt

    json_timestamp_start: Union[Unset, str] = UNSET
    if not isinstance(timestamp_start, Unset):
        json_timestamp_start = timestamp_start.isoformat()
    params["timestamp_start"] = json_timestamp_start

    json_timestamp_end: Union[Unset, str] = UNSET
    if not isinstance(timestamp_end, Unset):
        json_timestamp_end = timestamp_end.isoformat()
    params["timestamp_end"] = json_timestamp_end

    params["resumeToken"] = resume_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/limit-orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LimitOrdersV2Response]:
    if response.status_code == 200:
        response_200 = LimitOrdersV2Response.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LimitOrdersV2Response]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = 100.0,
    maker: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
) -> Response[LimitOrdersV2Response]:
    """Get all limit orders with resume token

    Args:
        chain_id (Union[Unset, float]):
        limit (Union[Unset, float]):  Default: 100.0.
        maker (Union[Unset, str]):
        yt (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        resume_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LimitOrdersV2Response]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        limit=limit,
        maker=maker,
        yt=yt,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        resume_token=resume_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = 100.0,
    maker: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
) -> Optional[LimitOrdersV2Response]:
    """Get all limit orders with resume token

    Args:
        chain_id (Union[Unset, float]):
        limit (Union[Unset, float]):  Default: 100.0.
        maker (Union[Unset, str]):
        yt (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        resume_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LimitOrdersV2Response
    """

    return sync_detailed(
        client=client,
        chain_id=chain_id,
        limit=limit,
        maker=maker,
        yt=yt,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        resume_token=resume_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = 100.0,
    maker: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
) -> Response[LimitOrdersV2Response]:
    """Get all limit orders with resume token

    Args:
        chain_id (Union[Unset, float]):
        limit (Union[Unset, float]):  Default: 100.0.
        maker (Union[Unset, str]):
        yt (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        resume_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LimitOrdersV2Response]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        limit=limit,
        maker=maker,
        yt=yt,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        resume_token=resume_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = 100.0,
    maker: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    resume_token: Union[Unset, str] = UNSET,
) -> Optional[LimitOrdersV2Response]:
    """Get all limit orders with resume token

    Args:
        chain_id (Union[Unset, float]):
        limit (Union[Unset, float]):  Default: 100.0.
        maker (Union[Unset, str]):
        yt (Union[Unset, str]):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        resume_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LimitOrdersV2Response
    """

    return (
        await asyncio_detailed(
            client=client,
            chain_id=chain_id,
            limit=limit,
            maker=maker,
            yt=yt,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
            resume_token=resume_token,
        )
    ).parsed

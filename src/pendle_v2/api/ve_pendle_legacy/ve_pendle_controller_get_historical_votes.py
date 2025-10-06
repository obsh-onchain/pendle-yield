import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_historical_votes_response import GetHistoricalVotesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": f"/v1/ve-pendle/{address}/historical-votes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetHistoricalVotesResponse]:
    if response.status_code == 200:
        response_200 = GetHistoricalVotesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetHistoricalVotesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetHistoricalVotesResponse]:
    """Get user historical votes

    Args:
        address (str):
        timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHistoricalVotesResponse]
    """

    kwargs = _get_kwargs(
        address=address,
        timestamp=timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetHistoricalVotesResponse]:
    """Get user historical votes

    Args:
        address (str):
        timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHistoricalVotesResponse
    """

    return sync_detailed(
        address=address,
        client=client,
        timestamp=timestamp,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetHistoricalVotesResponse]:
    """Get user historical votes

    Args:
        address (str):
        timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHistoricalVotesResponse]
    """

    kwargs = _get_kwargs(
        address=address,
        timestamp=timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetHistoricalVotesResponse]:
    """Get user historical votes

    Args:
        address (str):
        timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHistoricalVotesResponse
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
            timestamp=timestamp,
        )
    ).parsed

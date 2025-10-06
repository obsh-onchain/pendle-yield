from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    *,
    receiver: str,
    sys: Union[Unset, str] = UNSET,
    yts: Union[Unset, str] = UNSET,
    markets: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["receiver"] = receiver

    params["sys"] = sys

    params["yts"] = yts

    params["markets"] = markets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/sdk/{chain_id}/redeem-interests-and-rewards",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    receiver: str,
    sys: Union[Unset, str] = UNSET,
    yts: Union[Unset, str] = UNSET,
    markets: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Redeem rewards and interests from positions

     Redeem rewards and interests from positions

    Args:
        chain_id (float):
        receiver (str):
        sys (Union[Unset, str]):
        yts (Union[Unset, str]):
        markets (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        receiver=receiver,
        sys=sys,
        yts=yts,
        markets=markets,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    receiver: str,
    sys: Union[Unset, str] = UNSET,
    yts: Union[Unset, str] = UNSET,
    markets: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Redeem rewards and interests from positions

     Redeem rewards and interests from positions

    Args:
        chain_id (float):
        receiver (str):
        sys (Union[Unset, str]):
        yts (Union[Unset, str]):
        markets (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        receiver=receiver,
        sys=sys,
        yts=yts,
        markets=markets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

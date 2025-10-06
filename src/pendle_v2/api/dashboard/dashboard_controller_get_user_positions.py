from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_positions_cross_chain_response import UserPositionsCrossChainResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user: str,
    *,
    filter_usd: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterUsd"] = filter_usd

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/dashboard/positions/database/{user}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UserPositionsCrossChainResponse]:
    if response.status_code == 200:
        response_200 = UserPositionsCrossChainResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UserPositionsCrossChainResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_usd: Union[Unset, float] = UNSET,
) -> Response[UserPositionsCrossChainResponse]:
    """Get user positions across all chains

    Args:
        user (str):
        filter_usd (Union[Unset, float]):  Example: 0.1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserPositionsCrossChainResponse]
    """

    kwargs = _get_kwargs(
        user=user,
        filter_usd=filter_usd,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_usd: Union[Unset, float] = UNSET,
) -> Optional[UserPositionsCrossChainResponse]:
    """Get user positions across all chains

    Args:
        user (str):
        filter_usd (Union[Unset, float]):  Example: 0.1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserPositionsCrossChainResponse
    """

    return sync_detailed(
        user=user,
        client=client,
        filter_usd=filter_usd,
    ).parsed


async def asyncio_detailed(
    user: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_usd: Union[Unset, float] = UNSET,
) -> Response[UserPositionsCrossChainResponse]:
    """Get user positions across all chains

    Args:
        user (str):
        filter_usd (Union[Unset, float]):  Example: 0.1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserPositionsCrossChainResponse]
    """

    kwargs = _get_kwargs(
        user=user,
        filter_usd=filter_usd,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_usd: Union[Unset, float] = UNSET,
) -> Optional[UserPositionsCrossChainResponse]:
    """Get user positions across all chains

    Args:
        user (str):
        filter_usd (Union[Unset, float]):  Example: 0.1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserPositionsCrossChainResponse
    """

    return (
        await asyncio_detailed(
            user=user,
            client=client,
            filter_usd=filter_usd,
        )
    ).parsed

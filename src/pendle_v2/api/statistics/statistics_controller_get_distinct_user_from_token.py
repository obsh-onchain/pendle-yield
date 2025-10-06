from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_distinct_users_from_token_entity import GetDistinctUsersFromTokenEntity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    token: str,
    chain_id: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params["chainId"] = chain_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/statistics/get-distinct-user-from-token",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetDistinctUsersFromTokenEntity]:
    if response.status_code == 200:
        response_200 = GetDistinctUsersFromTokenEntity.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetDistinctUsersFromTokenEntity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    chain_id: Union[Unset, float] = UNSET,
) -> Response[GetDistinctUsersFromTokenEntity]:
    """Get unique users for token

    Args:
        token (str):
        chain_id (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDistinctUsersFromTokenEntity]
    """

    kwargs = _get_kwargs(
        token=token,
        chain_id=chain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    chain_id: Union[Unset, float] = UNSET,
) -> Optional[GetDistinctUsersFromTokenEntity]:
    """Get unique users for token

    Args:
        token (str):
        chain_id (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDistinctUsersFromTokenEntity
    """

    return sync_detailed(
        client=client,
        token=token,
        chain_id=chain_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    chain_id: Union[Unset, float] = UNSET,
) -> Response[GetDistinctUsersFromTokenEntity]:
    """Get unique users for token

    Args:
        token (str):
        chain_id (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDistinctUsersFromTokenEntity]
    """

    kwargs = _get_kwargs(
        token=token,
        chain_id=chain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    chain_id: Union[Unset, float] = UNSET,
) -> Optional[GetDistinctUsersFromTokenEntity]:
    """Get unique users for token

    Args:
        token (str):
        chain_id (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDistinctUsersFromTokenEntity
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
            chain_id=chain_id,
        )
    ).parsed

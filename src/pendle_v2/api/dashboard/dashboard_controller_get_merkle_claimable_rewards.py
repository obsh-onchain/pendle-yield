from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.merkle_claimable_rewards_response import MerkleClaimableRewardsResponse
from ...types import Response


def _get_kwargs(
    user: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/dashboard/merkle-claimable-rewards/{user}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MerkleClaimableRewardsResponse]:
    if response.status_code == 200:
        response_200 = MerkleClaimableRewardsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MerkleClaimableRewardsResponse]:
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
) -> Response[MerkleClaimableRewardsResponse]:
    """Get all merkle claimable rewards for a user

    Args:
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MerkleClaimableRewardsResponse]
    """

    kwargs = _get_kwargs(
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MerkleClaimableRewardsResponse]:
    """Get all merkle claimable rewards for a user

    Args:
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MerkleClaimableRewardsResponse
    """

    return sync_detailed(
        user=user,
        client=client,
    ).parsed


async def asyncio_detailed(
    user: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MerkleClaimableRewardsResponse]:
    """Get all merkle claimable rewards for a user

    Args:
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MerkleClaimableRewardsResponse]
    """

    kwargs = _get_kwargs(
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MerkleClaimableRewardsResponse]:
    """Get all merkle claimable rewards for a user

    Args:
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MerkleClaimableRewardsResponse
    """

    return (
        await asyncio_detailed(
            user=user,
            client=client,
        )
    ).parsed

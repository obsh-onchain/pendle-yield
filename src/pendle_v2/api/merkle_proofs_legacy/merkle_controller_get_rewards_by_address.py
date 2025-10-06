from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.merkle_controller_get_rewards_by_address_campaign import MerkleControllerGetRewardsByAddressCampaign
from ...models.merkle_rewards_response import MerkleRewardsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    campaign: MerkleControllerGetRewardsByAddressCampaign,
    address: str,
    *,
    chain_id: Union[Unset, float] = 1.0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chainId"] = chain_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/merkle/{campaign}/{address}/rewards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MerkleRewardsResponse]:
    if response.status_code == 200:
        response_200 = MerkleRewardsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MerkleRewardsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign: MerkleControllerGetRewardsByAddressCampaign,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = 1.0,
) -> Response[MerkleRewardsResponse]:
    """Get user rewards detail

    Args:
        campaign (MerkleControllerGetRewardsByAddressCampaign):
        address (str):
        chain_id (Union[Unset, float]):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MerkleRewardsResponse]
    """

    kwargs = _get_kwargs(
        campaign=campaign,
        address=address,
        chain_id=chain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign: MerkleControllerGetRewardsByAddressCampaign,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = 1.0,
) -> Optional[MerkleRewardsResponse]:
    """Get user rewards detail

    Args:
        campaign (MerkleControllerGetRewardsByAddressCampaign):
        address (str):
        chain_id (Union[Unset, float]):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MerkleRewardsResponse
    """

    return sync_detailed(
        campaign=campaign,
        address=address,
        client=client,
        chain_id=chain_id,
    ).parsed


async def asyncio_detailed(
    campaign: MerkleControllerGetRewardsByAddressCampaign,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = 1.0,
) -> Response[MerkleRewardsResponse]:
    """Get user rewards detail

    Args:
        campaign (MerkleControllerGetRewardsByAddressCampaign):
        address (str):
        chain_id (Union[Unset, float]):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MerkleRewardsResponse]
    """

    kwargs = _get_kwargs(
        campaign=campaign,
        address=address,
        chain_id=chain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign: MerkleControllerGetRewardsByAddressCampaign,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = 1.0,
) -> Optional[MerkleRewardsResponse]:
    """Get user rewards detail

    Args:
        campaign (MerkleControllerGetRewardsByAddressCampaign):
        address (str):
        chain_id (Union[Unset, float]):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MerkleRewardsResponse
    """

    return (
        await asyncio_detailed(
            campaign=campaign,
            address=address,
            client=client,
            chain_id=chain_id,
        )
    ).parsed

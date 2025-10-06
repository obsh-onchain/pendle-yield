from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.merkle_controller_get_proof_by_address_campaign import MerkleControllerGetProofByAddressCampaign
from ...models.merkle_proof_response import MerkleProofResponse
from ...models.not_found_response import NotFoundResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    campaign: MerkleControllerGetProofByAddressCampaign,
    address: str,
    *,
    generate_verify_data: Union[Unset, bool] = False,
    chain_id: Union[Unset, float] = 1.0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["generateVerifyData"] = generate_verify_data

    params["chainId"] = chain_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/merkle/{campaign}/{address}/proof",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[MerkleProofResponse, NotFoundResponse]]:
    if response.status_code == 200:
        response_200 = MerkleProofResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = NotFoundResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[MerkleProofResponse, NotFoundResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign: MerkleControllerGetProofByAddressCampaign,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    generate_verify_data: Union[Unset, bool] = False,
    chain_id: Union[Unset, float] = 1.0,
) -> Response[Union[MerkleProofResponse, NotFoundResponse]]:
    """Get user merkle proof

    Args:
        campaign (MerkleControllerGetProofByAddressCampaign):
        address (str):
        generate_verify_data (Union[Unset, bool]):  Default: False.
        chain_id (Union[Unset, float]):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MerkleProofResponse, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        campaign=campaign,
        address=address,
        generate_verify_data=generate_verify_data,
        chain_id=chain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign: MerkleControllerGetProofByAddressCampaign,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    generate_verify_data: Union[Unset, bool] = False,
    chain_id: Union[Unset, float] = 1.0,
) -> Optional[Union[MerkleProofResponse, NotFoundResponse]]:
    """Get user merkle proof

    Args:
        campaign (MerkleControllerGetProofByAddressCampaign):
        address (str):
        generate_verify_data (Union[Unset, bool]):  Default: False.
        chain_id (Union[Unset, float]):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MerkleProofResponse, NotFoundResponse]
    """

    return sync_detailed(
        campaign=campaign,
        address=address,
        client=client,
        generate_verify_data=generate_verify_data,
        chain_id=chain_id,
    ).parsed


async def asyncio_detailed(
    campaign: MerkleControllerGetProofByAddressCampaign,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    generate_verify_data: Union[Unset, bool] = False,
    chain_id: Union[Unset, float] = 1.0,
) -> Response[Union[MerkleProofResponse, NotFoundResponse]]:
    """Get user merkle proof

    Args:
        campaign (MerkleControllerGetProofByAddressCampaign):
        address (str):
        generate_verify_data (Union[Unset, bool]):  Default: False.
        chain_id (Union[Unset, float]):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MerkleProofResponse, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        campaign=campaign,
        address=address,
        generate_verify_data=generate_verify_data,
        chain_id=chain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign: MerkleControllerGetProofByAddressCampaign,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    generate_verify_data: Union[Unset, bool] = False,
    chain_id: Union[Unset, float] = 1.0,
) -> Optional[Union[MerkleProofResponse, NotFoundResponse]]:
    """Get user merkle proof

    Args:
        campaign (MerkleControllerGetProofByAddressCampaign):
        address (str):
        generate_verify_data (Union[Unset, bool]):  Default: False.
        chain_id (Union[Unset, float]):  Default: 1.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MerkleProofResponse, NotFoundResponse]
    """

    return (
        await asyncio_detailed(
            campaign=campaign,
            address=address,
            client=client,
            generate_verify_data=generate_verify_data,
            chain_id=chain_id,
        )
    ).parsed

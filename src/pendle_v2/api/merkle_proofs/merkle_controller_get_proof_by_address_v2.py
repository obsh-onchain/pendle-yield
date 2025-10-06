from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.merkle_proof_v2_response import MerkleProofV2Response
from ...models.not_found_response import NotFoundResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    address: str,
    *,
    generate_verify_data: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["generateVerifyData"] = generate_verify_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/merkle/{address}/proof",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[MerkleProofV2Response, NotFoundResponse]]:
    if response.status_code == 200:
        response_200 = MerkleProofV2Response.from_dict(response.json())

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
) -> Response[Union[MerkleProofV2Response, NotFoundResponse]]:
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
    generate_verify_data: Union[Unset, bool] = False,
) -> Response[Union[MerkleProofV2Response, NotFoundResponse]]:
    """Get user merkle proof v2

    Args:
        address (str):
        generate_verify_data (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MerkleProofV2Response, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        address=address,
        generate_verify_data=generate_verify_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    generate_verify_data: Union[Unset, bool] = False,
) -> Optional[Union[MerkleProofV2Response, NotFoundResponse]]:
    """Get user merkle proof v2

    Args:
        address (str):
        generate_verify_data (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MerkleProofV2Response, NotFoundResponse]
    """

    return sync_detailed(
        address=address,
        client=client,
        generate_verify_data=generate_verify_data,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    generate_verify_data: Union[Unset, bool] = False,
) -> Response[Union[MerkleProofV2Response, NotFoundResponse]]:
    """Get user merkle proof v2

    Args:
        address (str):
        generate_verify_data (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MerkleProofV2Response, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        address=address,
        generate_verify_data=generate_verify_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    generate_verify_data: Union[Unset, bool] = False,
) -> Optional[Union[MerkleProofV2Response, NotFoundResponse]]:
    """Get user merkle proof v2

    Args:
        address (str):
        generate_verify_data (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MerkleProofV2Response, NotFoundResponse]
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
            generate_verify_data=generate_verify_data,
        )
    ).parsed

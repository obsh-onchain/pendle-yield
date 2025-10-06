from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transaction_response import TransactionResponse
from ...types import Response


def _get_kwargs(
    chain_id: float,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/transactions/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TransactionResponse]:
    if response.status_code == 200:
        response_200 = TransactionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TransactionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[TransactionResponse]:
    """Get transaction details

    Args:
        chain_id (float):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[TransactionResponse]:
    """Get transaction details

    Args:
        chain_id (float):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[TransactionResponse]:
    """Get transaction details

    Args:
        chain_id (float):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[TransactionResponse]:
    """Get transaction details

    Args:
        chain_id (float):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            id=id,
            client=client,
        )
    ).parsed

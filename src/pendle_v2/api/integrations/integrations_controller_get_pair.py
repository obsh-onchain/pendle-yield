from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.integration_pair_response import IntegrationPairResponse
from ...types import UNSET, Response


def _get_kwargs(
    chain_id: float,
    *,
    id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/integrations/pair",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IntegrationPairResponse]:
    if response.status_code == 200:
        response_200 = IntegrationPairResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IntegrationPairResponse]:
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
    id: str,
) -> Response[IntegrationPairResponse]:
    """Get PT - SY pair by Pendle LP address

    Args:
        chain_id (float):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationPairResponse]
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
    *,
    client: Union[AuthenticatedClient, Client],
    id: str,
) -> Optional[IntegrationPairResponse]:
    """Get PT - SY pair by Pendle LP address

    Args:
        chain_id (float):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationPairResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    id: str,
) -> Response[IntegrationPairResponse]:
    """Get PT - SY pair by Pendle LP address

    Args:
        chain_id (float):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationPairResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    id: str,
) -> Optional[IntegrationPairResponse]:
    """Get PT - SY pair by Pendle LP address

    Args:
        chain_id (float):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationPairResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
            id=id,
        )
    ).parsed

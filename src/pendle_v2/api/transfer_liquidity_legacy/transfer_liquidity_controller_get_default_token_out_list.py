from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sy_token_out_route_list_response import SyTokenOutRouteListResponse
from ...types import Response


def _get_kwargs(
    chain_id: float,
    from_sy_address: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/transfer-liquidity/{from_sy_address}/token-out",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SyTokenOutRouteListResponse]:
    if response.status_code == 200:
        response_200 = SyTokenOutRouteListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SyTokenOutRouteListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    from_sy_address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SyTokenOutRouteListResponse]:
    """Get default transfer tokens

    Args:
        chain_id (float):
        from_sy_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyTokenOutRouteListResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        from_sy_address=from_sy_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    from_sy_address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SyTokenOutRouteListResponse]:
    """Get default transfer tokens

    Args:
        chain_id (float):
        from_sy_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyTokenOutRouteListResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        from_sy_address=from_sy_address,
        client=client,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    from_sy_address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SyTokenOutRouteListResponse]:
    """Get default transfer tokens

    Args:
        chain_id (float):
        from_sy_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyTokenOutRouteListResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        from_sy_address=from_sy_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    from_sy_address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SyTokenOutRouteListResponse]:
    """Get default transfer tokens

    Args:
        chain_id (float):
        from_sy_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyTokenOutRouteListResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            from_sy_address=from_sy_address,
            client=client,
        )
    ).parsed

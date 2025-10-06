from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.liquid_locker_pools_response import LiquidLockerPoolsResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    chain_id: float,
    lp_address: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chainId"] = chain_id

    params["lpAddress"] = lp_address

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/statistics/liquid-locker-pools",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LiquidLockerPoolsResponse]:
    if response.status_code == 200:
        response_200 = LiquidLockerPoolsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LiquidLockerPoolsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: float,
    lp_address: str,
) -> Response[LiquidLockerPoolsResponse]:
    """Get liquid locker pools

    Args:
        chain_id (float):  Example: 1.
        lp_address (str):  Example: 0x1234....

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiquidLockerPoolsResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        lp_address=lp_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: float,
    lp_address: str,
) -> Optional[LiquidLockerPoolsResponse]:
    """Get liquid locker pools

    Args:
        chain_id (float):  Example: 1.
        lp_address (str):  Example: 0x1234....

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiquidLockerPoolsResponse
    """

    return sync_detailed(
        client=client,
        chain_id=chain_id,
        lp_address=lp_address,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: float,
    lp_address: str,
) -> Response[LiquidLockerPoolsResponse]:
    """Get liquid locker pools

    Args:
        chain_id (float):  Example: 1.
        lp_address (str):  Example: 0x1234....

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiquidLockerPoolsResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        lp_address=lp_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: float,
    lp_address: str,
) -> Optional[LiquidLockerPoolsResponse]:
    """Get liquid locker pools

    Args:
        chain_id (float):  Example: 1.
        lp_address (str):  Example: 0x1234....

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiquidLockerPoolsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            chain_id=chain_id,
            lp_address=lp_address,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pool_voter_aprs_swap_fees_response import PoolVoterAprsSwapFeesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order_by: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["order_by"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ve-pendle/pool-voter-apr-swap-fee",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PoolVoterAprsSwapFeesResponse]:
    if response.status_code == 200:
        response_200 = PoolVoterAprsSwapFeesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PoolVoterAprsSwapFeesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
) -> Response[PoolVoterAprsSwapFeesResponse]:
    """Get pool voter APR and fees

    Args:
        order_by (Union[Unset, str]):  Example: voterApr:-1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PoolVoterAprsSwapFeesResponse]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
) -> Optional[PoolVoterAprsSwapFeesResponse]:
    """Get pool voter APR and fees

    Args:
        order_by (Union[Unset, str]):  Example: voterApr:-1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PoolVoterAprsSwapFeesResponse
    """

    return sync_detailed(
        client=client,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
) -> Response[PoolVoterAprsSwapFeesResponse]:
    """Get pool voter APR and fees

    Args:
        order_by (Union[Unset, str]):  Example: voterApr:-1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PoolVoterAprsSwapFeesResponse]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
) -> Optional[PoolVoterAprsSwapFeesResponse]:
    """Get pool voter APR and fees

    Args:
        order_by (Union[Unset, str]):  Example: voterApr:-1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PoolVoterAprsSwapFeesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            order_by=order_by,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transactions_v5_response import TransactionsV5Response
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    address: str,
    *,
    type_: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    min_value: Union[Unset, float] = UNSET,
    tx_origin: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["type"] = type_

    params["skip"] = skip

    params["limit"] = limit

    params["minValue"] = min_value

    params["txOrigin"] = tx_origin

    params["action"] = action

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v5/{chain_id}/transactions/{address}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TransactionsV5Response]:
    if response.status_code == 200:
        response_200 = TransactionsV5Response.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TransactionsV5Response]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    min_value: Union[Unset, float] = UNSET,
    tx_origin: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
) -> Response[TransactionsV5Response]:
    """Get market transactions by address

     Return transactions with: user action (long or short yield, add or remove liquidity), valuation,
    implied apy.

    Args:
        chain_id (float):
        address (str):
        type_ (str):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        min_value (Union[Unset, float]):
        tx_origin (Union[Unset, str]):
        action (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionsV5Response]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        type_=type_,
        skip=skip,
        limit=limit,
        min_value=min_value,
        tx_origin=tx_origin,
        action=action,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    min_value: Union[Unset, float] = UNSET,
    tx_origin: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
) -> Optional[TransactionsV5Response]:
    """Get market transactions by address

     Return transactions with: user action (long or short yield, add or remove liquidity), valuation,
    implied apy.

    Args:
        chain_id (float):
        address (str):
        type_ (str):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        min_value (Union[Unset, float]):
        tx_origin (Union[Unset, str]):
        action (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionsV5Response
    """

    return sync_detailed(
        chain_id=chain_id,
        address=address,
        client=client,
        type_=type_,
        skip=skip,
        limit=limit,
        min_value=min_value,
        tx_origin=tx_origin,
        action=action,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    min_value: Union[Unset, float] = UNSET,
    tx_origin: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
) -> Response[TransactionsV5Response]:
    """Get market transactions by address

     Return transactions with: user action (long or short yield, add or remove liquidity), valuation,
    implied apy.

    Args:
        chain_id (float):
        address (str):
        type_ (str):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        min_value (Union[Unset, float]):
        tx_origin (Union[Unset, str]):
        action (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionsV5Response]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        type_=type_,
        skip=skip,
        limit=limit,
        min_value=min_value,
        tx_origin=tx_origin,
        action=action,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: str,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    min_value: Union[Unset, float] = UNSET,
    tx_origin: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
) -> Optional[TransactionsV5Response]:
    """Get market transactions by address

     Return transactions with: user action (long or short yield, add or remove liquidity), valuation,
    implied apy.

    Args:
        chain_id (float):
        address (str):
        type_ (str):
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        min_value (Union[Unset, float]):
        tx_origin (Union[Unset, str]):
        action (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionsV5Response
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            address=address,
            client=client,
            type_=type_,
            skip=skip,
            limit=limit,
            min_value=min_value,
            tx_origin=tx_origin,
            action=action,
        )
    ).parsed

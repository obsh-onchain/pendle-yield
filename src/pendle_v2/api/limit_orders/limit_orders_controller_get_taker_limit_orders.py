from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_error_response import HttpErrorResponse
from ...models.limit_orders_controller_get_taker_limit_orders_sort_by import (
    LimitOrdersControllerGetTakerLimitOrdersSortBy,
)
from ...models.limit_orders_controller_get_taker_limit_orders_sort_order import (
    LimitOrdersControllerGetTakerLimitOrdersSortOrder,
)
from ...models.limit_orders_controller_get_taker_limit_orders_type import LimitOrdersControllerGetTakerLimitOrdersType
from ...models.limit_orders_taker_response import LimitOrdersTakerResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    yt: str,
    type_: LimitOrdersControllerGetTakerLimitOrdersType,
    sort_by: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortBy] = UNSET,
    sort_order: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortOrder] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    params["chainId"] = chain_id

    params["yt"] = yt

    json_type_ = type_.value
    params["type"] = json_type_

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_sort_order: Union[Unset, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/limit-orders/takers/limit-orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpErrorResponse, LimitOrdersTakerResponse]]:
    if response.status_code == 200:
        response_200 = LimitOrdersTakerResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HttpErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HttpErrorResponse, LimitOrdersTakerResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    yt: str,
    type_: LimitOrdersControllerGetTakerLimitOrdersType,
    sort_by: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortBy] = UNSET,
    sort_order: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortOrder] = UNSET,
) -> Response[Union[HttpErrorResponse, LimitOrdersTakerResponse]]:
    """Get limit orders to match by YT address

     This endpoint returns best matching limit orders for a given YT address.

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        chain_id (float):
        yt (str):
        type_ (LimitOrdersControllerGetTakerLimitOrdersType):
        sort_by (Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortBy]):
        sort_order (Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpErrorResponse, LimitOrdersTakerResponse]]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        chain_id=chain_id,
        yt=yt,
        type_=type_,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    yt: str,
    type_: LimitOrdersControllerGetTakerLimitOrdersType,
    sort_by: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortBy] = UNSET,
    sort_order: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortOrder] = UNSET,
) -> Optional[Union[HttpErrorResponse, LimitOrdersTakerResponse]]:
    """Get limit orders to match by YT address

     This endpoint returns best matching limit orders for a given YT address.

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        chain_id (float):
        yt (str):
        type_ (LimitOrdersControllerGetTakerLimitOrdersType):
        sort_by (Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortBy]):
        sort_order (Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpErrorResponse, LimitOrdersTakerResponse]
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
        chain_id=chain_id,
        yt=yt,
        type_=type_,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    yt: str,
    type_: LimitOrdersControllerGetTakerLimitOrdersType,
    sort_by: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortBy] = UNSET,
    sort_order: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortOrder] = UNSET,
) -> Response[Union[HttpErrorResponse, LimitOrdersTakerResponse]]:
    """Get limit orders to match by YT address

     This endpoint returns best matching limit orders for a given YT address.

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        chain_id (float):
        yt (str):
        type_ (LimitOrdersControllerGetTakerLimitOrdersType):
        sort_by (Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortBy]):
        sort_order (Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpErrorResponse, LimitOrdersTakerResponse]]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        chain_id=chain_id,
        yt=yt,
        type_=type_,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    yt: str,
    type_: LimitOrdersControllerGetTakerLimitOrdersType,
    sort_by: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortBy] = UNSET,
    sort_order: Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortOrder] = UNSET,
) -> Optional[Union[HttpErrorResponse, LimitOrdersTakerResponse]]:
    """Get limit orders to match by YT address

     This endpoint returns best matching limit orders for a given YT address.

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        chain_id (float):
        yt (str):
        type_ (LimitOrdersControllerGetTakerLimitOrdersType):
        sort_by (Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortBy]):
        sort_order (Union[Unset, LimitOrdersControllerGetTakerLimitOrdersSortOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpErrorResponse, LimitOrdersTakerResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
            chain_id=chain_id,
            yt=yt,
            type_=type_,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed

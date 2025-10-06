from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.limit_orders_controller_fetch_makers_sort_by import LimitOrdersControllerFetchMakersSortBy
from ...models.limit_orders_controller_fetch_makers_sort_order import LimitOrdersControllerFetchMakersSortOrder
from ...models.makers_response import MakersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sort_by: Union[
        Unset, LimitOrdersControllerFetchMakersSortBy
    ] = LimitOrdersControllerFetchMakersSortBy.SUM_ORDER_SIZE,
    sort_order: Union[
        Unset, LimitOrdersControllerFetchMakersSortOrder
    ] = LimitOrdersControllerFetchMakersSortOrder.DESC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chainId"] = chain_id

    params["yt"] = yt

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
        "url": "/v1/limit-orders/makers-list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MakersResponse]:
    if response.status_code == 200:
        response_200 = MakersResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MakersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sort_by: Union[
        Unset, LimitOrdersControllerFetchMakersSortBy
    ] = LimitOrdersControllerFetchMakersSortBy.SUM_ORDER_SIZE,
    sort_order: Union[
        Unset, LimitOrdersControllerFetchMakersSortOrder
    ] = LimitOrdersControllerFetchMakersSortOrder.DESC,
) -> Response[MakersResponse]:
    """Fetch list makers

    Args:
        chain_id (Union[Unset, float]):
        yt (Union[Unset, str]):
        sort_by (Union[Unset, LimitOrdersControllerFetchMakersSortBy]):  Default:
            LimitOrdersControllerFetchMakersSortBy.SUM_ORDER_SIZE.
        sort_order (Union[Unset, LimitOrdersControllerFetchMakersSortOrder]):  Default:
            LimitOrdersControllerFetchMakersSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MakersResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        yt=yt,
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
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sort_by: Union[
        Unset, LimitOrdersControllerFetchMakersSortBy
    ] = LimitOrdersControllerFetchMakersSortBy.SUM_ORDER_SIZE,
    sort_order: Union[
        Unset, LimitOrdersControllerFetchMakersSortOrder
    ] = LimitOrdersControllerFetchMakersSortOrder.DESC,
) -> Optional[MakersResponse]:
    """Fetch list makers

    Args:
        chain_id (Union[Unset, float]):
        yt (Union[Unset, str]):
        sort_by (Union[Unset, LimitOrdersControllerFetchMakersSortBy]):  Default:
            LimitOrdersControllerFetchMakersSortBy.SUM_ORDER_SIZE.
        sort_order (Union[Unset, LimitOrdersControllerFetchMakersSortOrder]):  Default:
            LimitOrdersControllerFetchMakersSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MakersResponse
    """

    return sync_detailed(
        client=client,
        chain_id=chain_id,
        yt=yt,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sort_by: Union[
        Unset, LimitOrdersControllerFetchMakersSortBy
    ] = LimitOrdersControllerFetchMakersSortBy.SUM_ORDER_SIZE,
    sort_order: Union[
        Unset, LimitOrdersControllerFetchMakersSortOrder
    ] = LimitOrdersControllerFetchMakersSortOrder.DESC,
) -> Response[MakersResponse]:
    """Fetch list makers

    Args:
        chain_id (Union[Unset, float]):
        yt (Union[Unset, str]):
        sort_by (Union[Unset, LimitOrdersControllerFetchMakersSortBy]):  Default:
            LimitOrdersControllerFetchMakersSortBy.SUM_ORDER_SIZE.
        sort_order (Union[Unset, LimitOrdersControllerFetchMakersSortOrder]):  Default:
            LimitOrdersControllerFetchMakersSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MakersResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        yt=yt,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sort_by: Union[
        Unset, LimitOrdersControllerFetchMakersSortBy
    ] = LimitOrdersControllerFetchMakersSortBy.SUM_ORDER_SIZE,
    sort_order: Union[
        Unset, LimitOrdersControllerFetchMakersSortOrder
    ] = LimitOrdersControllerFetchMakersSortOrder.DESC,
) -> Optional[MakersResponse]:
    """Fetch list makers

    Args:
        chain_id (Union[Unset, float]):
        yt (Union[Unset, str]):
        sort_by (Union[Unset, LimitOrdersControllerFetchMakersSortBy]):  Default:
            LimitOrdersControllerFetchMakersSortBy.SUM_ORDER_SIZE.
        sort_order (Union[Unset, LimitOrdersControllerFetchMakersSortOrder]):  Default:
            LimitOrdersControllerFetchMakersSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MakersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            chain_id=chain_id,
            yt=yt,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_limit_order_dto import CreateLimitOrderDto
from ...models.http_error_response import HttpErrorResponse
from ...models.limit_order_response import LimitOrderResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateLimitOrderDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/limit-orders/makers/limit-orders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpErrorResponse, LimitOrderResponse]]:
    if response.status_code == 201:
        response_201 = LimitOrderResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = HttpErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = HttpErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HttpErrorResponse, LimitOrderResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateLimitOrderDto,
) -> Response[Union[HttpErrorResponse, LimitOrderResponse]]:
    """Create limit order

    Args:
        body (CreateLimitOrderDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpErrorResponse, LimitOrderResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateLimitOrderDto,
) -> Optional[Union[HttpErrorResponse, LimitOrderResponse]]:
    """Create limit order

    Args:
        body (CreateLimitOrderDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpErrorResponse, LimitOrderResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateLimitOrderDto,
) -> Response[Union[HttpErrorResponse, LimitOrderResponse]]:
    """Create limit order

    Args:
        body (CreateLimitOrderDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpErrorResponse, LimitOrderResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateLimitOrderDto,
) -> Optional[Union[HttpErrorResponse, LimitOrderResponse]]:
    """Create limit order

    Args:
        body (CreateLimitOrderDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpErrorResponse, LimitOrderResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

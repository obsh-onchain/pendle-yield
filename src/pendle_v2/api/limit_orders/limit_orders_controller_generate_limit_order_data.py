from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_limit_order_data_dto import GenerateLimitOrderDataDto
from ...models.generate_limit_order_data_response import GenerateLimitOrderDataResponse
from ...models.http_error_response import HttpErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: GenerateLimitOrderDataDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/limit-orders/makers/generate-limit-order-data",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GenerateLimitOrderDataResponse, HttpErrorResponse]]:
    if response.status_code == 201:
        response_201 = GenerateLimitOrderDataResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = HttpErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GenerateLimitOrderDataResponse, HttpErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GenerateLimitOrderDataDto,
) -> Response[Union[GenerateLimitOrderDataResponse, HttpErrorResponse]]:
    """Generate limit order data

    Args:
        body (GenerateLimitOrderDataDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GenerateLimitOrderDataResponse, HttpErrorResponse]]
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
    body: GenerateLimitOrderDataDto,
) -> Optional[Union[GenerateLimitOrderDataResponse, HttpErrorResponse]]:
    """Generate limit order data

    Args:
        body (GenerateLimitOrderDataDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GenerateLimitOrderDataResponse, HttpErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GenerateLimitOrderDataDto,
) -> Response[Union[GenerateLimitOrderDataResponse, HttpErrorResponse]]:
    """Generate limit order data

    Args:
        body (GenerateLimitOrderDataDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GenerateLimitOrderDataResponse, HttpErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GenerateLimitOrderDataDto,
) -> Optional[Union[GenerateLimitOrderDataResponse, HttpErrorResponse]]:
    """Generate limit order data

    Args:
        body (GenerateLimitOrderDataDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GenerateLimitOrderDataResponse, HttpErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

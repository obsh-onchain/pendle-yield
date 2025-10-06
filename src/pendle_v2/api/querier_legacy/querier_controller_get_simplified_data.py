from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_simplified_data_response import GetSimplifiedDataResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_expired: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["isExpired"] = is_expired

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/querier/simplified-data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSimplifiedDataResponse]:
    if response.status_code == 200:
        response_200 = GetSimplifiedDataResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSimplifiedDataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    is_expired: Union[Unset, bool] = UNSET,
) -> Response[GetSimplifiedDataResponse]:
    """Get simplified market data

     Essential market and SY token information for quick overview.

    Args:
        is_expired (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSimplifiedDataResponse]
    """

    kwargs = _get_kwargs(
        is_expired=is_expired,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    is_expired: Union[Unset, bool] = UNSET,
) -> Optional[GetSimplifiedDataResponse]:
    """Get simplified market data

     Essential market and SY token information for quick overview.

    Args:
        is_expired (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSimplifiedDataResponse
    """

    return sync_detailed(
        client=client,
        is_expired=is_expired,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    is_expired: Union[Unset, bool] = UNSET,
) -> Response[GetSimplifiedDataResponse]:
    """Get simplified market data

     Essential market and SY token information for quick overview.

    Args:
        is_expired (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSimplifiedDataResponse]
    """

    kwargs = _get_kwargs(
        is_expired=is_expired,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    is_expired: Union[Unset, bool] = UNSET,
) -> Optional[GetSimplifiedDataResponse]:
    """Get simplified market data

     Essential market and SY token information for quick overview.

    Args:
        is_expired (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSimplifiedDataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            is_expired=is_expired,
        )
    ).parsed

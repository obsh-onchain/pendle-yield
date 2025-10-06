from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metadata_values_response import MetadataValuesResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    keys: list[str],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_keys = keys

    params["keys"] = json_keys

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/metadata",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MetadataValuesResponse]:
    if response.status_code == 200:
        response_200 = MetadataValuesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MetadataValuesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    keys: list[str],
) -> Response[MetadataValuesResponse]:
    """Get metadata via GET

    Args:
        keys (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataValuesResponse]
    """

    kwargs = _get_kwargs(
        keys=keys,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    keys: list[str],
) -> Optional[MetadataValuesResponse]:
    """Get metadata via GET

    Args:
        keys (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetadataValuesResponse
    """

    return sync_detailed(
        client=client,
        keys=keys,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    keys: list[str],
) -> Response[MetadataValuesResponse]:
    """Get metadata via GET

    Args:
        keys (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataValuesResponse]
    """

    kwargs = _get_kwargs(
        keys=keys,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    keys: list[str],
) -> Optional[MetadataValuesResponse]:
    """Get metadata via GET

    Args:
        keys (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetadataValuesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            keys=keys,
        )
    ).parsed

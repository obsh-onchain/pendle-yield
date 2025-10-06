from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_metadata_by_template_response import GetMetadataByTemplateResponse
from ...types import Response


def _get_kwargs(
    template: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/metadata/template/{template}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetMetadataByTemplateResponse]:
    if response.status_code == 200:
        response_200 = GetMetadataByTemplateResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetMetadataByTemplateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetMetadataByTemplateResponse]:
    """Get metadata by template

    Args:
        template (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetadataByTemplateResponse]
    """

    kwargs = _get_kwargs(
        template=template,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetMetadataByTemplateResponse]:
    """Get metadata by template

    Args:
        template (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetadataByTemplateResponse
    """

    return sync_detailed(
        template=template,
        client=client,
    ).parsed


async def asyncio_detailed(
    template: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetMetadataByTemplateResponse]:
    """Get metadata by template

    Args:
        template (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetadataByTemplateResponse]
    """

    kwargs = _get_kwargs(
        template=template,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetMetadataByTemplateResponse]:
    """Get metadata by template

    Args:
        template (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetadataByTemplateResponse
    """

    return (
        await asyncio_detailed(
            template=template,
            client=client,
        )
    ).parsed

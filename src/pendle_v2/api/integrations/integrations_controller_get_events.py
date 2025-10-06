from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.integration_event_response import IntegrationEventResponse
from ...types import UNSET, Response


def _get_kwargs(
    chain_id: float,
    *,
    from_block: float,
    to_block: float,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["fromBlock"] = from_block

    params["toBlock"] = to_block

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/integrations/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IntegrationEventResponse]:
    if response.status_code == 200:
        response_200 = IntegrationEventResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IntegrationEventResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    from_block: float,
    to_block: float,
) -> Response[IntegrationEventResponse]:
    """Get Pendle events within a block range

    Args:
        chain_id (float):
        from_block (float):
        to_block (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationEventResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        from_block=from_block,
        to_block=to_block,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    from_block: float,
    to_block: float,
) -> Optional[IntegrationEventResponse]:
    """Get Pendle events within a block range

    Args:
        chain_id (float):
        from_block (float):
        to_block (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationEventResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
        from_block=from_block,
        to_block=to_block,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    from_block: float,
    to_block: float,
) -> Response[IntegrationEventResponse]:
    """Get Pendle events within a block range

    Args:
        chain_id (float):
        from_block (float):
        to_block (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationEventResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        from_block=from_block,
        to_block=to_block,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    from_block: float,
    to_block: float,
) -> Optional[IntegrationEventResponse]:
    """Get Pendle events within a block range

    Args:
        chain_id (float):
        from_block (float):
        to_block (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationEventResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
            from_block=from_block,
            to_block=to_block,
        )
    ).parsed

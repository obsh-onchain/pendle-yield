from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ve_pendle_extended_data_response import VePendleExtendedDataResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/ve-pendle/data",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VePendleExtendedDataResponse]:
    if response.status_code == 200:
        response_200 = VePendleExtendedDataResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VePendleExtendedDataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[VePendleExtendedDataResponse]:
    """Get vePendle statistics

     The data returned contains:

    - monthly revenue
    - pendle token supply
    - pool vote, swap fee, apr of this epoch and last epoch
    - pool cap for this epoch and expected cap for next epoch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VePendleExtendedDataResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[VePendleExtendedDataResponse]:
    """Get vePendle statistics

     The data returned contains:

    - monthly revenue
    - pendle token supply
    - pool vote, swap fee, apr of this epoch and last epoch
    - pool cap for this epoch and expected cap for next epoch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VePendleExtendedDataResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[VePendleExtendedDataResponse]:
    """Get vePendle statistics

     The data returned contains:

    - monthly revenue
    - pendle token supply
    - pool vote, swap fee, apr of this epoch and last epoch
    - pool cap for this epoch and expected cap for next epoch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VePendleExtendedDataResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[VePendleExtendedDataResponse]:
    """Get vePendle statistics

     The data returned contains:

    - monthly revenue
    - pendle token supply
    - pool vote, swap fee, apr of this epoch and last epoch
    - pool cap for this epoch and expected cap for next epoch

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VePendleExtendedDataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

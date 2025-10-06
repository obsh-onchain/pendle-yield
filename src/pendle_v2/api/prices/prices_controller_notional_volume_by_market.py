import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notional_volume_response import NotionalVolumeResponse
from ...models.prices_controller_notional_volume_by_market_time_frame import (
    PricesControllerNotionalVolumeByMarketTimeFrame,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    address: str,
    *,
    time_frame: Union[
        Unset, PricesControllerNotionalVolumeByMarketTimeFrame
    ] = PricesControllerNotionalVolumeByMarketTimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_time_frame: Union[Unset, str] = UNSET
    if not isinstance(time_frame, Unset):
        json_time_frame = time_frame.value

    params["time_frame"] = json_time_frame

    json_timestamp_start: Union[Unset, str] = UNSET
    if not isinstance(timestamp_start, Unset):
        json_timestamp_start = timestamp_start.isoformat()
    params["timestamp_start"] = json_timestamp_start

    json_timestamp_end: Union[Unset, str] = UNSET
    if not isinstance(timestamp_end, Unset):
        json_timestamp_end = timestamp_end.isoformat()
    params["timestamp_end"] = json_timestamp_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/prices/{address}/notional-volume-by-market",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NotionalVolumeResponse]:
    if response.status_code == 200:
        response_200 = NotionalVolumeResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NotionalVolumeResponse]:
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
    time_frame: Union[
        Unset, PricesControllerNotionalVolumeByMarketTimeFrame
    ] = PricesControllerNotionalVolumeByMarketTimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[NotionalVolumeResponse]:
    """Get notional volume by market

    Args:
        chain_id (float):
        address (str):
        time_frame (Union[Unset, PricesControllerNotionalVolumeByMarketTimeFrame]):  Default:
            PricesControllerNotionalVolumeByMarketTimeFrame.HOUR.
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotionalVolumeResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        time_frame=time_frame,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
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
    time_frame: Union[
        Unset, PricesControllerNotionalVolumeByMarketTimeFrame
    ] = PricesControllerNotionalVolumeByMarketTimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[NotionalVolumeResponse]:
    """Get notional volume by market

    Args:
        chain_id (float):
        address (str):
        time_frame (Union[Unset, PricesControllerNotionalVolumeByMarketTimeFrame]):  Default:
            PricesControllerNotionalVolumeByMarketTimeFrame.HOUR.
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotionalVolumeResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        address=address,
        client=client,
        time_frame=time_frame,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    time_frame: Union[
        Unset, PricesControllerNotionalVolumeByMarketTimeFrame
    ] = PricesControllerNotionalVolumeByMarketTimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[NotionalVolumeResponse]:
    """Get notional volume by market

    Args:
        chain_id (float):
        address (str):
        time_frame (Union[Unset, PricesControllerNotionalVolumeByMarketTimeFrame]):  Default:
            PricesControllerNotionalVolumeByMarketTimeFrame.HOUR.
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotionalVolumeResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        time_frame=time_frame,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    time_frame: Union[
        Unset, PricesControllerNotionalVolumeByMarketTimeFrame
    ] = PricesControllerNotionalVolumeByMarketTimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[NotionalVolumeResponse]:
    """Get notional volume by market

    Args:
        chain_id (float):
        address (str):
        time_frame (Union[Unset, PricesControllerNotionalVolumeByMarketTimeFrame]):  Default:
            PricesControllerNotionalVolumeByMarketTimeFrame.HOUR.
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotionalVolumeResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            address=address,
            client=client,
            time_frame=time_frame,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
        )
    ).parsed

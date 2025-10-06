import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ve_pendle_apy_chart_response import VePendleApyChartResponse
from ...models.ve_pendle_controller_ve_pendle_apy_chart_time_frame import VePendleControllerVePendleApyChartTimeFrame
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    time_frame: Union[
        Unset, VePendleControllerVePendleApyChartTimeFrame
    ] = VePendleControllerVePendleApyChartTimeFrame.HOUR,
    timestamp_gte: Union[Unset, datetime.datetime] = UNSET,
    timestamp_lte: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_time_frame: Union[Unset, str] = UNSET
    if not isinstance(time_frame, Unset):
        json_time_frame = time_frame.value

    params["time_frame"] = json_time_frame

    json_timestamp_gte: Union[Unset, str] = UNSET
    if not isinstance(timestamp_gte, Unset):
        json_timestamp_gte = timestamp_gte.isoformat()
    params["timestamp_gte"] = json_timestamp_gte

    json_timestamp_lte: Union[Unset, str] = UNSET
    if not isinstance(timestamp_lte, Unset):
        json_timestamp_lte = timestamp_lte.isoformat()
    params["timestamp_lte"] = json_timestamp_lte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ve-pendle/ve-pendle-apy-chart",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VePendleApyChartResponse]:
    if response.status_code == 200:
        response_200 = VePendleApyChartResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VePendleApyChartResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    time_frame: Union[
        Unset, VePendleControllerVePendleApyChartTimeFrame
    ] = VePendleControllerVePendleApyChartTimeFrame.HOUR,
    timestamp_gte: Union[Unset, datetime.datetime] = UNSET,
    timestamp_lte: Union[Unset, datetime.datetime] = UNSET,
) -> Response[VePendleApyChartResponse]:
    """Get vePendle APY chart

    Args:
        time_frame (Union[Unset, VePendleControllerVePendleApyChartTimeFrame]):  Default:
            VePendleControllerVePendleApyChartTimeFrame.HOUR.
        timestamp_gte (Union[Unset, datetime.datetime]):
        timestamp_lte (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VePendleApyChartResponse]
    """

    kwargs = _get_kwargs(
        time_frame=time_frame,
        timestamp_gte=timestamp_gte,
        timestamp_lte=timestamp_lte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    time_frame: Union[
        Unset, VePendleControllerVePendleApyChartTimeFrame
    ] = VePendleControllerVePendleApyChartTimeFrame.HOUR,
    timestamp_gte: Union[Unset, datetime.datetime] = UNSET,
    timestamp_lte: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[VePendleApyChartResponse]:
    """Get vePendle APY chart

    Args:
        time_frame (Union[Unset, VePendleControllerVePendleApyChartTimeFrame]):  Default:
            VePendleControllerVePendleApyChartTimeFrame.HOUR.
        timestamp_gte (Union[Unset, datetime.datetime]):
        timestamp_lte (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VePendleApyChartResponse
    """

    return sync_detailed(
        client=client,
        time_frame=time_frame,
        timestamp_gte=timestamp_gte,
        timestamp_lte=timestamp_lte,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    time_frame: Union[
        Unset, VePendleControllerVePendleApyChartTimeFrame
    ] = VePendleControllerVePendleApyChartTimeFrame.HOUR,
    timestamp_gte: Union[Unset, datetime.datetime] = UNSET,
    timestamp_lte: Union[Unset, datetime.datetime] = UNSET,
) -> Response[VePendleApyChartResponse]:
    """Get vePendle APY chart

    Args:
        time_frame (Union[Unset, VePendleControllerVePendleApyChartTimeFrame]):  Default:
            VePendleControllerVePendleApyChartTimeFrame.HOUR.
        timestamp_gte (Union[Unset, datetime.datetime]):
        timestamp_lte (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VePendleApyChartResponse]
    """

    kwargs = _get_kwargs(
        time_frame=time_frame,
        timestamp_gte=timestamp_gte,
        timestamp_lte=timestamp_lte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    time_frame: Union[
        Unset, VePendleControllerVePendleApyChartTimeFrame
    ] = VePendleControllerVePendleApyChartTimeFrame.HOUR,
    timestamp_gte: Union[Unset, datetime.datetime] = UNSET,
    timestamp_lte: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[VePendleApyChartResponse]:
    """Get vePendle APY chart

    Args:
        time_frame (Union[Unset, VePendleControllerVePendleApyChartTimeFrame]):  Default:
            VePendleControllerVePendleApyChartTimeFrame.HOUR.
        timestamp_gte (Union[Unset, datetime.datetime]):
        timestamp_lte (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VePendleApyChartResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            time_frame=time_frame,
            timestamp_gte=timestamp_gte,
            timestamp_lte=timestamp_lte,
        )
    ).parsed

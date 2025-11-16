import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.market_historical_data_response import MarketHistoricalDataResponse
from ...models.markets_controller_market_historical_data_v2_time_frame import (
    MarketsControllerMarketHistoricalDataV2TimeFrame,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    address: str,
    *,
    time_frame: Union[
        Unset, MarketsControllerMarketHistoricalDataV2TimeFrame
    ] = MarketsControllerMarketHistoricalDataV2TimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = "underlyingApy,impliedApy,maxApy,baseApy,tvl",
    include_fee_breakdown: Union[Unset, bool] = UNSET,
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

    params["fields"] = fields

    params["includeFeeBreakdown"] = include_fee_breakdown

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/{chain_id}/markets/{address}/historical-data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MarketHistoricalDataResponse]:
    if response.status_code == 200:
        response_200 = MarketHistoricalDataResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MarketHistoricalDataResponse]:
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
        Unset, MarketsControllerMarketHistoricalDataV2TimeFrame
    ] = MarketsControllerMarketHistoricalDataV2TimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = "underlyingApy,impliedApy,maxApy,baseApy,tvl",
    include_fee_breakdown: Union[Unset, bool] = UNSET,
) -> Response[MarketHistoricalDataResponse]:
    """Get market time-series data by address

     Returns the time-series data for a given market. Useful to draw charts or do data analysis.

    This endpoint supports field selection via the `fields` query parameter. Available fields include:
    timestamp, maxApy, baseApy, underlyingApy, impliedApy, tvl, totalTvl, underlyingInterestApy,
    underlyingRewardApy, ytFloatingApy, swapFeeApy, voterApr, pendleApy, lpRewardApy, totalPt, totalSy,
    totalSupply, ptPrice, ytPrice, syPrice, lpPrice, lastEpochVotes, tradingVolume.

    Args:
        chain_id (float):
        address (str):
        time_frame (Union[Unset, MarketsControllerMarketHistoricalDataV2TimeFrame]):  Default:
            MarketsControllerMarketHistoricalDataV2TimeFrame.HOUR.
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):  Default: 'underlyingApy,impliedApy,maxApy,baseApy,tvl'.
            Example: timestamp,maxApy,baseApy,underlyingApy,impliedApy,tvl,totalTvl,underlyingInterest
            Apy,underlyingRewardApy,ytFloatingApy,swapFeeApy,voterApr,pendleApy,lpRewardApy,totalPt,to
            talSy,totalSupply,ptPrice,ytPrice,syPrice,lpPrice,lastEpochVotes,tradingVolume.
        include_fee_breakdown (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketHistoricalDataResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        time_frame=time_frame,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        fields=fields,
        include_fee_breakdown=include_fee_breakdown,
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
        Unset, MarketsControllerMarketHistoricalDataV2TimeFrame
    ] = MarketsControllerMarketHistoricalDataV2TimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = "underlyingApy,impliedApy,maxApy,baseApy,tvl",
    include_fee_breakdown: Union[Unset, bool] = UNSET,
) -> Optional[MarketHistoricalDataResponse]:
    """Get market time-series data by address

     Returns the time-series data for a given market. Useful to draw charts or do data analysis.

    This endpoint supports field selection via the `fields` query parameter. Available fields include:
    timestamp, maxApy, baseApy, underlyingApy, impliedApy, tvl, totalTvl, underlyingInterestApy,
    underlyingRewardApy, ytFloatingApy, swapFeeApy, voterApr, pendleApy, lpRewardApy, totalPt, totalSy,
    totalSupply, ptPrice, ytPrice, syPrice, lpPrice, lastEpochVotes, tradingVolume.

    Args:
        chain_id (float):
        address (str):
        time_frame (Union[Unset, MarketsControllerMarketHistoricalDataV2TimeFrame]):  Default:
            MarketsControllerMarketHistoricalDataV2TimeFrame.HOUR.
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):  Default: 'underlyingApy,impliedApy,maxApy,baseApy,tvl'.
            Example: timestamp,maxApy,baseApy,underlyingApy,impliedApy,tvl,totalTvl,underlyingInterest
            Apy,underlyingRewardApy,ytFloatingApy,swapFeeApy,voterApr,pendleApy,lpRewardApy,totalPt,to
            talSy,totalSupply,ptPrice,ytPrice,syPrice,lpPrice,lastEpochVotes,tradingVolume.
        include_fee_breakdown (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketHistoricalDataResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        address=address,
        client=client,
        time_frame=time_frame,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        fields=fields,
        include_fee_breakdown=include_fee_breakdown,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    time_frame: Union[
        Unset, MarketsControllerMarketHistoricalDataV2TimeFrame
    ] = MarketsControllerMarketHistoricalDataV2TimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = "underlyingApy,impliedApy,maxApy,baseApy,tvl",
    include_fee_breakdown: Union[Unset, bool] = UNSET,
) -> Response[MarketHistoricalDataResponse]:
    """Get market time-series data by address

     Returns the time-series data for a given market. Useful to draw charts or do data analysis.

    This endpoint supports field selection via the `fields` query parameter. Available fields include:
    timestamp, maxApy, baseApy, underlyingApy, impliedApy, tvl, totalTvl, underlyingInterestApy,
    underlyingRewardApy, ytFloatingApy, swapFeeApy, voterApr, pendleApy, lpRewardApy, totalPt, totalSy,
    totalSupply, ptPrice, ytPrice, syPrice, lpPrice, lastEpochVotes, tradingVolume.

    Args:
        chain_id (float):
        address (str):
        time_frame (Union[Unset, MarketsControllerMarketHistoricalDataV2TimeFrame]):  Default:
            MarketsControllerMarketHistoricalDataV2TimeFrame.HOUR.
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):  Default: 'underlyingApy,impliedApy,maxApy,baseApy,tvl'.
            Example: timestamp,maxApy,baseApy,underlyingApy,impliedApy,tvl,totalTvl,underlyingInterest
            Apy,underlyingRewardApy,ytFloatingApy,swapFeeApy,voterApr,pendleApy,lpRewardApy,totalPt,to
            talSy,totalSupply,ptPrice,ytPrice,syPrice,lpPrice,lastEpochVotes,tradingVolume.
        include_fee_breakdown (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketHistoricalDataResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        time_frame=time_frame,
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        fields=fields,
        include_fee_breakdown=include_fee_breakdown,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    time_frame: Union[
        Unset, MarketsControllerMarketHistoricalDataV2TimeFrame
    ] = MarketsControllerMarketHistoricalDataV2TimeFrame.HOUR,
    timestamp_start: Union[Unset, datetime.datetime] = UNSET,
    timestamp_end: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, str] = "underlyingApy,impliedApy,maxApy,baseApy,tvl",
    include_fee_breakdown: Union[Unset, bool] = UNSET,
) -> Optional[MarketHistoricalDataResponse]:
    """Get market time-series data by address

     Returns the time-series data for a given market. Useful to draw charts or do data analysis.

    This endpoint supports field selection via the `fields` query parameter. Available fields include:
    timestamp, maxApy, baseApy, underlyingApy, impliedApy, tvl, totalTvl, underlyingInterestApy,
    underlyingRewardApy, ytFloatingApy, swapFeeApy, voterApr, pendleApy, lpRewardApy, totalPt, totalSy,
    totalSupply, ptPrice, ytPrice, syPrice, lpPrice, lastEpochVotes, tradingVolume.

    Args:
        chain_id (float):
        address (str):
        time_frame (Union[Unset, MarketsControllerMarketHistoricalDataV2TimeFrame]):  Default:
            MarketsControllerMarketHistoricalDataV2TimeFrame.HOUR.
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
        fields (Union[Unset, str]):  Default: 'underlyingApy,impliedApy,maxApy,baseApy,tvl'.
            Example: timestamp,maxApy,baseApy,underlyingApy,impliedApy,tvl,totalTvl,underlyingInterest
            Apy,underlyingRewardApy,ytFloatingApy,swapFeeApy,voterApr,pendleApy,lpRewardApy,totalPt,to
            talSy,totalSupply,ptPrice,ytPrice,syPrice,lpPrice,lastEpochVotes,tradingVolume.
        include_fee_breakdown (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketHistoricalDataResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            address=address,
            client=client,
            time_frame=time_frame,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
            fields=fields,
            include_fee_breakdown=include_fee_breakdown,
        )
    ).parsed

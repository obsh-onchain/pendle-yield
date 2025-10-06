import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ve_pendle_extended_data_response import VePendleExtendedDataResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    epoch: Union[Unset, datetime.datetime] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    vote_snapshot: Union[Unset, bool] = UNSET,
    pool_voter_data: Union[Unset, bool] = UNSET,
    pool_metadata: Union[Unset, bool] = UNSET,
    token_supply: Union[Unset, bool] = UNSET,
    ongoing_votes: Union[Unset, bool] = UNSET,
    ve_pendle_cap: Union[Unset, bool] = UNSET,
    monthly_revenue: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_epoch: Union[Unset, str] = UNSET
    if not isinstance(epoch, Unset):
        json_epoch = epoch.isoformat()
    params["epoch"] = json_epoch

    params["order_by"] = order_by

    params["voteSnapshot"] = vote_snapshot

    params["poolVoterData"] = pool_voter_data

    params["poolMetadata"] = pool_metadata

    params["tokenSupply"] = token_supply

    params["ongoingVotes"] = ongoing_votes

    params["vePendleCap"] = ve_pendle_cap

    params["monthlyRevenue"] = monthly_revenue

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/ve-pendle/data",
        "params": params,
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
    epoch: Union[Unset, datetime.datetime] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    vote_snapshot: Union[Unset, bool] = UNSET,
    pool_voter_data: Union[Unset, bool] = UNSET,
    pool_metadata: Union[Unset, bool] = UNSET,
    token_supply: Union[Unset, bool] = UNSET,
    ongoing_votes: Union[Unset, bool] = UNSET,
    ve_pendle_cap: Union[Unset, bool] = UNSET,
    monthly_revenue: Union[Unset, bool] = UNSET,
) -> Response[VePendleExtendedDataResponse]:
    """Get full vePendle statistics and governance data with filtering

    Args:
        epoch (Union[Unset, datetime.datetime]):
        order_by (Union[Unset, str]):  Example: voterApr:-1.
        vote_snapshot (Union[Unset, bool]):
        pool_voter_data (Union[Unset, bool]):
        pool_metadata (Union[Unset, bool]):
        token_supply (Union[Unset, bool]):
        ongoing_votes (Union[Unset, bool]):
        ve_pendle_cap (Union[Unset, bool]):
        monthly_revenue (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VePendleExtendedDataResponse]
    """

    kwargs = _get_kwargs(
        epoch=epoch,
        order_by=order_by,
        vote_snapshot=vote_snapshot,
        pool_voter_data=pool_voter_data,
        pool_metadata=pool_metadata,
        token_supply=token_supply,
        ongoing_votes=ongoing_votes,
        ve_pendle_cap=ve_pendle_cap,
        monthly_revenue=monthly_revenue,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: Union[Unset, datetime.datetime] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    vote_snapshot: Union[Unset, bool] = UNSET,
    pool_voter_data: Union[Unset, bool] = UNSET,
    pool_metadata: Union[Unset, bool] = UNSET,
    token_supply: Union[Unset, bool] = UNSET,
    ongoing_votes: Union[Unset, bool] = UNSET,
    ve_pendle_cap: Union[Unset, bool] = UNSET,
    monthly_revenue: Union[Unset, bool] = UNSET,
) -> Optional[VePendleExtendedDataResponse]:
    """Get full vePendle statistics and governance data with filtering

    Args:
        epoch (Union[Unset, datetime.datetime]):
        order_by (Union[Unset, str]):  Example: voterApr:-1.
        vote_snapshot (Union[Unset, bool]):
        pool_voter_data (Union[Unset, bool]):
        pool_metadata (Union[Unset, bool]):
        token_supply (Union[Unset, bool]):
        ongoing_votes (Union[Unset, bool]):
        ve_pendle_cap (Union[Unset, bool]):
        monthly_revenue (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VePendleExtendedDataResponse
    """

    return sync_detailed(
        client=client,
        epoch=epoch,
        order_by=order_by,
        vote_snapshot=vote_snapshot,
        pool_voter_data=pool_voter_data,
        pool_metadata=pool_metadata,
        token_supply=token_supply,
        ongoing_votes=ongoing_votes,
        ve_pendle_cap=ve_pendle_cap,
        monthly_revenue=monthly_revenue,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: Union[Unset, datetime.datetime] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    vote_snapshot: Union[Unset, bool] = UNSET,
    pool_voter_data: Union[Unset, bool] = UNSET,
    pool_metadata: Union[Unset, bool] = UNSET,
    token_supply: Union[Unset, bool] = UNSET,
    ongoing_votes: Union[Unset, bool] = UNSET,
    ve_pendle_cap: Union[Unset, bool] = UNSET,
    monthly_revenue: Union[Unset, bool] = UNSET,
) -> Response[VePendleExtendedDataResponse]:
    """Get full vePendle statistics and governance data with filtering

    Args:
        epoch (Union[Unset, datetime.datetime]):
        order_by (Union[Unset, str]):  Example: voterApr:-1.
        vote_snapshot (Union[Unset, bool]):
        pool_voter_data (Union[Unset, bool]):
        pool_metadata (Union[Unset, bool]):
        token_supply (Union[Unset, bool]):
        ongoing_votes (Union[Unset, bool]):
        ve_pendle_cap (Union[Unset, bool]):
        monthly_revenue (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VePendleExtendedDataResponse]
    """

    kwargs = _get_kwargs(
        epoch=epoch,
        order_by=order_by,
        vote_snapshot=vote_snapshot,
        pool_voter_data=pool_voter_data,
        pool_metadata=pool_metadata,
        token_supply=token_supply,
        ongoing_votes=ongoing_votes,
        ve_pendle_cap=ve_pendle_cap,
        monthly_revenue=monthly_revenue,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: Union[Unset, datetime.datetime] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    vote_snapshot: Union[Unset, bool] = UNSET,
    pool_voter_data: Union[Unset, bool] = UNSET,
    pool_metadata: Union[Unset, bool] = UNSET,
    token_supply: Union[Unset, bool] = UNSET,
    ongoing_votes: Union[Unset, bool] = UNSET,
    ve_pendle_cap: Union[Unset, bool] = UNSET,
    monthly_revenue: Union[Unset, bool] = UNSET,
) -> Optional[VePendleExtendedDataResponse]:
    """Get full vePendle statistics and governance data with filtering

    Args:
        epoch (Union[Unset, datetime.datetime]):
        order_by (Union[Unset, str]):  Example: voterApr:-1.
        vote_snapshot (Union[Unset, bool]):
        pool_voter_data (Union[Unset, bool]):
        pool_metadata (Union[Unset, bool]):
        token_supply (Union[Unset, bool]):
        ongoing_votes (Union[Unset, bool]):
        ve_pendle_cap (Union[Unset, bool]):
        monthly_revenue (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VePendleExtendedDataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            epoch=epoch,
            order_by=order_by,
            vote_snapshot=vote_snapshot,
            pool_voter_data=pool_voter_data,
            pool_metadata=pool_metadata,
            token_supply=token_supply,
            ongoing_votes=ongoing_votes,
            ve_pendle_cap=ve_pendle_cap,
            monthly_revenue=monthly_revenue,
        )
    ).parsed

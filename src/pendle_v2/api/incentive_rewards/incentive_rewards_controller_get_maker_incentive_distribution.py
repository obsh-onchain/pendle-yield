import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.merkl_reward_response import MerklRewardResponse
from ...types import UNSET, Response


def _get_kwargs(
    chain_id: float,
    *,
    epoch_timestamp: datetime.datetime,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_epoch_timestamp = epoch_timestamp.isoformat()
    params["epochTimestamp"] = json_epoch_timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/incentive-rewards/{chain_id}/maker-incentive",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MerklRewardResponse]:
    if response.status_code == 200:
        response_200 = MerklRewardResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MerklRewardResponse]:
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
    epoch_timestamp: datetime.datetime,
) -> Response[MerklRewardResponse]:
    """Get maker incentive distribution file

    Args:
        chain_id (float):
        epoch_timestamp (datetime.datetime):  Example: 2025-10-09T12:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MerklRewardResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        epoch_timestamp=epoch_timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    epoch_timestamp: datetime.datetime,
) -> Optional[MerklRewardResponse]:
    """Get maker incentive distribution file

    Args:
        chain_id (float):
        epoch_timestamp (datetime.datetime):  Example: 2025-10-09T12:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MerklRewardResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
        epoch_timestamp=epoch_timestamp,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    epoch_timestamp: datetime.datetime,
) -> Response[MerklRewardResponse]:
    """Get maker incentive distribution file

    Args:
        chain_id (float):
        epoch_timestamp (datetime.datetime):  Example: 2025-10-09T12:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MerklRewardResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        epoch_timestamp=epoch_timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    epoch_timestamp: datetime.datetime,
) -> Optional[MerklRewardResponse]:
    """Get maker incentive distribution file

    Args:
        chain_id (float):
        epoch_timestamp (datetime.datetime):  Example: 2025-10-09T12:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MerklRewardResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
            epoch_timestamp=epoch_timestamp,
        )
    ).parsed

import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.vote_snapshot_response import VoteSnapshotResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    epoch: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_epoch: Union[Unset, str] = UNSET
    if not isinstance(epoch, Unset):
        json_epoch = epoch.isoformat()
    params["epoch"] = json_epoch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ve-pendle/vote-snapshot",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VoteSnapshotResponse]:
    if response.status_code == 200:
        response_200 = VoteSnapshotResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VoteSnapshotResponse]:
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
) -> Response[VoteSnapshotResponse]:
    """Get vote snapshot

    Args:
        epoch (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VoteSnapshotResponse]
    """

    kwargs = _get_kwargs(
        epoch=epoch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[VoteSnapshotResponse]:
    """Get vote snapshot

    Args:
        epoch (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VoteSnapshotResponse
    """

    return sync_detailed(
        client=client,
        epoch=epoch,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: Union[Unset, datetime.datetime] = UNSET,
) -> Response[VoteSnapshotResponse]:
    """Get vote snapshot

    Args:
        epoch (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VoteSnapshotResponse]
    """

    kwargs = _get_kwargs(
        epoch=epoch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[VoteSnapshotResponse]:
    """Get vote snapshot

    Args:
        epoch (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VoteSnapshotResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            epoch=epoch,
        )
    ).parsed

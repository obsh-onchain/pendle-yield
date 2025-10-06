import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transactions_response_entity import TransactionsResponseEntity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    from_timestamp: Union[Unset, datetime.datetime] = UNSET,
    to_timestamp: Union[Unset, datetime.datetime] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    user: str,
    market: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    json_from_timestamp: Union[Unset, str] = UNSET
    if not isinstance(from_timestamp, Unset):
        json_from_timestamp = from_timestamp.isoformat()
    params["fromTimestamp"] = json_from_timestamp

    json_to_timestamp: Union[Unset, str] = UNSET
    if not isinstance(to_timestamp, Unset):
        json_to_timestamp = to_timestamp.isoformat()
    params["toTimestamp"] = json_to_timestamp

    params["chainId"] = chain_id

    params["user"] = user

    params["market"] = market

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/pnl/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TransactionsResponseEntity]:
    if response.status_code == 200:
        response_200 = TransactionsResponseEntity.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TransactionsResponseEntity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    from_timestamp: Union[Unset, datetime.datetime] = UNSET,
    to_timestamp: Union[Unset, datetime.datetime] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    user: str,
    market: Union[Unset, str] = UNSET,
) -> Response[TransactionsResponseEntity]:
    """Get PNL transactions of a user

     Get PNL transactions of a user

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        from_timestamp (Union[Unset, datetime.datetime]):
        to_timestamp (Union[Unset, datetime.datetime]):
        chain_id (Union[Unset, float]):
        user (str):
        market (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionsResponseEntity]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp,
        chain_id=chain_id,
        user=user,
        market=market,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    from_timestamp: Union[Unset, datetime.datetime] = UNSET,
    to_timestamp: Union[Unset, datetime.datetime] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    user: str,
    market: Union[Unset, str] = UNSET,
) -> Optional[TransactionsResponseEntity]:
    """Get PNL transactions of a user

     Get PNL transactions of a user

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        from_timestamp (Union[Unset, datetime.datetime]):
        to_timestamp (Union[Unset, datetime.datetime]):
        chain_id (Union[Unset, float]):
        user (str):
        market (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionsResponseEntity
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp,
        chain_id=chain_id,
        user=user,
        market=market,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    from_timestamp: Union[Unset, datetime.datetime] = UNSET,
    to_timestamp: Union[Unset, datetime.datetime] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    user: str,
    market: Union[Unset, str] = UNSET,
) -> Response[TransactionsResponseEntity]:
    """Get PNL transactions of a user

     Get PNL transactions of a user

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        from_timestamp (Union[Unset, datetime.datetime]):
        to_timestamp (Union[Unset, datetime.datetime]):
        chain_id (Union[Unset, float]):
        user (str):
        market (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionsResponseEntity]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp,
        chain_id=chain_id,
        user=user,
        market=market,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    from_timestamp: Union[Unset, datetime.datetime] = UNSET,
    to_timestamp: Union[Unset, datetime.datetime] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    user: str,
    market: Union[Unset, str] = UNSET,
) -> Optional[TransactionsResponseEntity]:
    """Get PNL transactions of a user

     Get PNL transactions of a user

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        from_timestamp (Union[Unset, datetime.datetime]):
        to_timestamp (Union[Unset, datetime.datetime]):
        chain_id (Union[Unset, float]):
        user (str):
        market (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionsResponseEntity
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            chain_id=chain_id,
            user=user,
            market=market,
        )
    ).parsed

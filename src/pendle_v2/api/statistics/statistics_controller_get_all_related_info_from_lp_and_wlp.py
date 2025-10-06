from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_related_info_from_lp_and_wlp_response import GetAllRelatedInfoFromLpAndWlpResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    chain_id: float,
    market_address: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chainId"] = chain_id

    params["marketAddress"] = market_address

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/statistics/get-all-related-info-from-lp-and-wlp",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllRelatedInfoFromLpAndWlpResponse]:
    if response.status_code == 200:
        response_200 = GetAllRelatedInfoFromLpAndWlpResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllRelatedInfoFromLpAndWlpResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: float,
    market_address: Union[Unset, str] = UNSET,
) -> Response[GetAllRelatedInfoFromLpAndWlpResponse]:
    """Get LP and WLP token info

    Args:
        chain_id (float):  Example: 1.
        market_address (Union[Unset, str]):  Example: 0x0000000000000000000000000000000000000000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllRelatedInfoFromLpAndWlpResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        market_address=market_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: float,
    market_address: Union[Unset, str] = UNSET,
) -> Optional[GetAllRelatedInfoFromLpAndWlpResponse]:
    """Get LP and WLP token info

    Args:
        chain_id (float):  Example: 1.
        market_address (Union[Unset, str]):  Example: 0x0000000000000000000000000000000000000000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllRelatedInfoFromLpAndWlpResponse
    """

    return sync_detailed(
        client=client,
        chain_id=chain_id,
        market_address=market_address,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: float,
    market_address: Union[Unset, str] = UNSET,
) -> Response[GetAllRelatedInfoFromLpAndWlpResponse]:
    """Get LP and WLP token info

    Args:
        chain_id (float):  Example: 1.
        market_address (Union[Unset, str]):  Example: 0x0000000000000000000000000000000000000000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllRelatedInfoFromLpAndWlpResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        market_address=market_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    chain_id: float,
    market_address: Union[Unset, str] = UNSET,
) -> Optional[GetAllRelatedInfoFromLpAndWlpResponse]:
    """Get LP and WLP token info

    Args:
        chain_id (float):  Example: 1.
        market_address (Union[Unset, str]):  Example: 0x0000000000000000000000000000000000000000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllRelatedInfoFromLpAndWlpResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            chain_id=chain_id,
            market_address=market_address,
        )
    ).parsed

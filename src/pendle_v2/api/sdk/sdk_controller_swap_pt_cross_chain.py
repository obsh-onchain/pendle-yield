from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sdk_controller_swap_pt_cross_chain_exact_amount_type import SdkControllerSwapPtCrossChainExactAmountType
from ...types import UNSET, Response


def _get_kwargs(
    chain_id: float,
    *,
    receiver: str,
    pt: str,
    token: str,
    exact_amount_type: SdkControllerSwapPtCrossChainExactAmountType,
    exact_amount: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["receiver"] = receiver

    params["pt"] = pt

    params["token"] = token

    json_exact_amount_type = exact_amount_type.value
    params["exactAmountType"] = json_exact_amount_type

    params["exactAmount"] = exact_amount

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/sdk/{chain_id}/swap-pt-cross-chain",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    receiver: str,
    pt: str,
    token: str,
    exact_amount_type: SdkControllerSwapPtCrossChainExactAmountType,
    exact_amount: str,
) -> Response[Any]:
    """Swap PT using fixed price AMM for cross-chain operations

     Swap PT tokens using the fixed price AMM. Supports both exact PT input and exact token output modes.

    Args:
        chain_id (float):
        receiver (str):
        pt (str):
        token (str):
        exact_amount_type (SdkControllerSwapPtCrossChainExactAmountType):
        exact_amount (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        receiver=receiver,
        pt=pt,
        token=token,
        exact_amount_type=exact_amount_type,
        exact_amount=exact_amount,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    receiver: str,
    pt: str,
    token: str,
    exact_amount_type: SdkControllerSwapPtCrossChainExactAmountType,
    exact_amount: str,
) -> Response[Any]:
    """Swap PT using fixed price AMM for cross-chain operations

     Swap PT tokens using the fixed price AMM. Supports both exact PT input and exact token output modes.

    Args:
        chain_id (float):
        receiver (str):
        pt (str):
        token (str):
        exact_amount_type (SdkControllerSwapPtCrossChainExactAmountType):
        exact_amount (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        receiver=receiver,
        pt=pt,
        token=token,
        exact_amount_type=exact_amount_type,
        exact_amount=exact_amount,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

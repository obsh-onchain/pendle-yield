from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sdk_controller_cancel_single_limit_order_order_type import SdkControllerCancelSingleLimitOrderOrderType
from ...types import UNSET, Response


def _get_kwargs(
    chain_id: float,
    *,
    user_address: str,
    salt: str,
    expiry: str,
    nonce: str,
    order_type: SdkControllerCancelSingleLimitOrderOrderType,
    token: str,
    yt: str,
    maker: str,
    receiver: str,
    making_amount: str,
    ln_implied_rate: str,
    fail_safe_rate: str,
    permit: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["userAddress"] = user_address

    params["salt"] = salt

    params["expiry"] = expiry

    params["nonce"] = nonce

    json_order_type = order_type.value
    params["orderType"] = json_order_type

    params["token"] = token

    params["YT"] = yt

    params["maker"] = maker

    params["receiver"] = receiver

    params["makingAmount"] = making_amount

    params["lnImpliedRate"] = ln_implied_rate

    params["failSafeRate"] = fail_safe_rate

    params["permit"] = permit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/sdk/{chain_id}/limit-order/cancel-single",
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
    user_address: str,
    salt: str,
    expiry: str,
    nonce: str,
    order_type: SdkControllerCancelSingleLimitOrderOrderType,
    token: str,
    yt: str,
    maker: str,
    receiver: str,
    making_amount: str,
    ln_implied_rate: str,
    fail_safe_rate: str,
    permit: str,
) -> Response[Any]:
    """Cancel one single limit order by order hash

    Args:
        chain_id (float):
        user_address (str):
        salt (str):
        expiry (str):
        nonce (str):
        order_type (SdkControllerCancelSingleLimitOrderOrderType):
        token (str):
        yt (str):
        maker (str):
        receiver (str):
        making_amount (str):
        ln_implied_rate (str):
        fail_safe_rate (str):
        permit (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        user_address=user_address,
        salt=salt,
        expiry=expiry,
        nonce=nonce,
        order_type=order_type,
        token=token,
        yt=yt,
        maker=maker,
        receiver=receiver,
        making_amount=making_amount,
        ln_implied_rate=ln_implied_rate,
        fail_safe_rate=fail_safe_rate,
        permit=permit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    user_address: str,
    salt: str,
    expiry: str,
    nonce: str,
    order_type: SdkControllerCancelSingleLimitOrderOrderType,
    token: str,
    yt: str,
    maker: str,
    receiver: str,
    making_amount: str,
    ln_implied_rate: str,
    fail_safe_rate: str,
    permit: str,
) -> Response[Any]:
    """Cancel one single limit order by order hash

    Args:
        chain_id (float):
        user_address (str):
        salt (str):
        expiry (str):
        nonce (str):
        order_type (SdkControllerCancelSingleLimitOrderOrderType):
        token (str):
        yt (str):
        maker (str):
        receiver (str):
        making_amount (str):
        ln_implied_rate (str):
        fail_safe_rate (str):
        permit (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        user_address=user_address,
        salt=salt,
        expiry=expiry,
        nonce=nonce,
        order_type=order_type,
        token=token,
        yt=yt,
        maker=maker,
        receiver=receiver,
        making_amount=making_amount,
        ln_implied_rate=ln_implied_rate,
        fail_safe_rate=fail_safe_rate,
        permit=permit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

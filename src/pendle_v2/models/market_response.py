import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apy_breakdown_response import ApyBreakdownResponse
    from ..models.asset_response import AssetResponse
    from ..models.estimated_daily_pool_reward_response import EstimatedDailyPoolRewardResponse
    from ..models.market_extended_info_response import MarketExtendedInfoResponse
    from ..models.valuation_response import ValuationResponse


T = TypeVar("T", bound="MarketResponse")


@_attrs_define
class MarketResponse:
    """
    Attributes:
        id (str): Unique identifier of the market in format "{chainId}-{address}"
        chain_id (float): Chain ID where the market is deployed
        address (str): Contract address of the market
        symbol (str): Symbol of the market
        expiry (datetime.datetime): Expiry date of the PT/YT tokens
        pt (AssetResponse):
        yt (AssetResponse):
        sy (AssetResponse):
        lp (AssetResponse):
        accounting_asset (AssetResponse):
        underlying_asset (AssetResponse):
        reward_tokens (list['AssetResponse']):
        input_tokens (list['AssetResponse']):
        output_tokens (list['AssetResponse']):
        asset_representation (str): String representation of the asset type for this market
        is_whitelisted_pro (bool): Whether this market is whitelisted for pro interface
        is_whitelisted_simple (bool): Whether this market is whitelisted for simple interface
        votable (bool): Whether this market can receive vePENDLE votes
        is_active (bool): Whether the market is currently active (not expired and not manually deactivated)
        is_whitelisted_limit_order (bool): Whether limit orders are enabled for this market
        category_ids (list[str]): Array of category IDs this market belongs to
        timestamp (datetime.datetime): Timestamp when the market data was last updated
        scalar_root (float):
        initial_anchor (float):
        extended_info (MarketExtendedInfoResponse):
        is_new (bool): Market which whitelisted in the last 2 weeks will have isNew==true
        name (str):
        simple_name (str):
        simple_symbol (str):
        simple_icon (str):
        pro_name (str):
        farm_name (str):
        farm_symbol (str):
        farm_simple_name (str):
        farm_simple_symbol (str):
        farm_simple_icon (str):
        farm_pro_name (str):
        farm_pro_symbol (str):
        farm_pro_icon (str):
        base_pricing_asset (Union['AssetResponse', None, Unset]): Same as accountingAsset
        protocol (Union[None, Unset, str]):
        underlying_pool (Union[None, Unset, str]):
        pro_symbol (Union[None, Unset, str]):
        pro_icon (Union[None, Unset, str]):
        accent_color (Union[None, Unset, str]):
        total_pt (Union[None, Unset, float]): Total PT in the market
        total_sy (Union[None, Unset, float]): Total SY in the market
        total_lp (Union[None, Unset, float]): Total supply of the LP token
        total_active_supply (Union[None, Unset, float]): Total active supply of the LP token, used for calculate
            boosting
        liquidity (Union['ValuationResponse', None, Unset]): Market liquidity, this is the liquidity of PT and SY in the
            AMM
        trading_volume (Union['ValuationResponse', None, Unset]): Market 24h trading volume
        underlying_interest_apy (Union[None, Unset, float]): Annual percentage yield from the underlying asset interest
        underlying_reward_apy (Union[None, Unset, float]): Annual percentage yield from the underlying asset rewards
        underlying_reward_apy_breakdown (Union[None, Unset, list['ApyBreakdownResponse']]):
        underlying_apy (Union[None, Unset, float]): APY of the underlying asset
        implied_apy (Union[None, Unset, float]): Implied APY of market
        yt_floating_apy (Union[None, Unset, float]): Floating APY for YT holders (underlyingApy - impliedApy)
        pt_discount (Union[None, Unset, float]): PT discount relative to underlying asset
        swap_fee_apy (Union[None, Unset, float]): Swap fee APY for LP holders, without boosting
        pendle_apy (Union[None, Unset, float]): APY from Pendle rewards
        arb_apy (Union[None, Unset, float]): APY from arbitrage opportunities
        aggregated_apy (Union[None, Unset, float]): APY including yield, swap fee and Pendle rewards without boosting
        max_boosted_apy (Union[None, Unset, float]): APY when maximum boost is applied
        lp_reward_apy (Union[None, Unset, float]): APY from LP reward tokens
        voter_apy (Union[None, Unset, float]): APY for voters (vePENDLE holders) from voting on this pool
        yt_roi (Union[None, Unset, float]): Return on investment for YT holders
        pt_roi (Union[None, Unset, float]): Return on investment for PT holders
        estimated_daily_pool_rewards (Union[None, Unset, list['EstimatedDailyPoolRewardResponse']]):
        data_updated_at (Union[None, Unset, datetime.datetime]):
        liquidity_change_24_h (Union[None, Unset, float]): 24-hour percentage change in liquidity
        trading_volume_change_24_h (Union[None, Unset, float]): 24-hour percentage change in trading volume
        underlying_interest_apy_change_24_h (Union[None, Unset, float]): 24-hour change in underlying interest APY (in
            percentage points)
        underlying_reward_apy_change_24_h (Union[None, Unset, float]): 24-hour change in underlying reward APY (in
            percentage points)
        underlying_apy_change_24_h (Union[None, Unset, float]): 24-hour change in underlying APY (in percentage points)
        implied_apy_change_24_h (Union[None, Unset, float]): 24-hour change in implied APY (in percentage points)
        yt_floating_apy_change_24_h (Union[None, Unset, float]): 24-hour change in YT floating APY (in percentage
            points)
        pt_discount_change_24_h (Union[None, Unset, float]): 24-hour change in PT discount (in percentage points)
        swap_fee_apy_change_24_h (Union[None, Unset, float]): 24-hour change in swap fee APY (in percentage points)
        pendle_apy_change_24_h (Union[None, Unset, float]): 24-hour change in PENDLE APY (in percentage points)
        aggregated_apy_change_24_h (Union[None, Unset, float]): 24-hour change in aggregated APY (in percentage points)
        lp_reward_apy_change_24_h (Union[None, Unset, float]): 24-hour change in LP reward APY (in percentage points)
        voter_apy_change_24_h (Union[None, Unset, float]): 24-hour change in voter APY (in percentage points)
        is_featured (Union[None, Unset, bool]):
        is_popular (Union[None, Unset, bool]):
        tvl_threshold_timestamp (Union[None, Unset, datetime.datetime]):
        whitelisted_pro_at (Union[None, Unset, datetime.datetime]):
    """

    id: str
    chain_id: float
    address: str
    symbol: str
    expiry: datetime.datetime
    pt: "AssetResponse"
    yt: "AssetResponse"
    sy: "AssetResponse"
    lp: "AssetResponse"
    accounting_asset: "AssetResponse"
    underlying_asset: "AssetResponse"
    reward_tokens: list["AssetResponse"]
    input_tokens: list["AssetResponse"]
    output_tokens: list["AssetResponse"]
    asset_representation: str
    is_whitelisted_pro: bool
    is_whitelisted_simple: bool
    votable: bool
    is_active: bool
    is_whitelisted_limit_order: bool
    category_ids: list[str]
    timestamp: datetime.datetime
    scalar_root: float
    initial_anchor: float
    extended_info: "MarketExtendedInfoResponse"
    is_new: bool
    name: str
    simple_name: str
    simple_symbol: str
    simple_icon: str
    pro_name: str
    farm_name: str
    farm_symbol: str
    farm_simple_name: str
    farm_simple_symbol: str
    farm_simple_icon: str
    farm_pro_name: str
    farm_pro_symbol: str
    farm_pro_icon: str
    base_pricing_asset: Union["AssetResponse", None, Unset] = UNSET
    protocol: Union[None, Unset, str] = UNSET
    underlying_pool: Union[None, Unset, str] = UNSET
    pro_symbol: Union[None, Unset, str] = UNSET
    pro_icon: Union[None, Unset, str] = UNSET
    accent_color: Union[None, Unset, str] = UNSET
    total_pt: Union[None, Unset, float] = UNSET
    total_sy: Union[None, Unset, float] = UNSET
    total_lp: Union[None, Unset, float] = UNSET
    total_active_supply: Union[None, Unset, float] = UNSET
    liquidity: Union["ValuationResponse", None, Unset] = UNSET
    trading_volume: Union["ValuationResponse", None, Unset] = UNSET
    underlying_interest_apy: Union[None, Unset, float] = UNSET
    underlying_reward_apy: Union[None, Unset, float] = UNSET
    underlying_reward_apy_breakdown: Union[None, Unset, list["ApyBreakdownResponse"]] = UNSET
    underlying_apy: Union[None, Unset, float] = UNSET
    implied_apy: Union[None, Unset, float] = UNSET
    yt_floating_apy: Union[None, Unset, float] = UNSET
    pt_discount: Union[None, Unset, float] = UNSET
    swap_fee_apy: Union[None, Unset, float] = UNSET
    pendle_apy: Union[None, Unset, float] = UNSET
    arb_apy: Union[None, Unset, float] = UNSET
    aggregated_apy: Union[None, Unset, float] = UNSET
    max_boosted_apy: Union[None, Unset, float] = UNSET
    lp_reward_apy: Union[None, Unset, float] = UNSET
    voter_apy: Union[None, Unset, float] = UNSET
    yt_roi: Union[None, Unset, float] = UNSET
    pt_roi: Union[None, Unset, float] = UNSET
    estimated_daily_pool_rewards: Union[None, Unset, list["EstimatedDailyPoolRewardResponse"]] = UNSET
    data_updated_at: Union[None, Unset, datetime.datetime] = UNSET
    liquidity_change_24_h: Union[None, Unset, float] = UNSET
    trading_volume_change_24_h: Union[None, Unset, float] = UNSET
    underlying_interest_apy_change_24_h: Union[None, Unset, float] = UNSET
    underlying_reward_apy_change_24_h: Union[None, Unset, float] = UNSET
    underlying_apy_change_24_h: Union[None, Unset, float] = UNSET
    implied_apy_change_24_h: Union[None, Unset, float] = UNSET
    yt_floating_apy_change_24_h: Union[None, Unset, float] = UNSET
    pt_discount_change_24_h: Union[None, Unset, float] = UNSET
    swap_fee_apy_change_24_h: Union[None, Unset, float] = UNSET
    pendle_apy_change_24_h: Union[None, Unset, float] = UNSET
    aggregated_apy_change_24_h: Union[None, Unset, float] = UNSET
    lp_reward_apy_change_24_h: Union[None, Unset, float] = UNSET
    voter_apy_change_24_h: Union[None, Unset, float] = UNSET
    is_featured: Union[None, Unset, bool] = UNSET
    is_popular: Union[None, Unset, bool] = UNSET
    tvl_threshold_timestamp: Union[None, Unset, datetime.datetime] = UNSET
    whitelisted_pro_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_response import AssetResponse
        from ..models.valuation_response import ValuationResponse

        id = self.id

        chain_id = self.chain_id

        address = self.address

        symbol = self.symbol

        expiry = self.expiry.isoformat()

        pt = self.pt.to_dict()

        yt = self.yt.to_dict()

        sy = self.sy.to_dict()

        lp = self.lp.to_dict()

        accounting_asset = self.accounting_asset.to_dict()

        underlying_asset = self.underlying_asset.to_dict()

        reward_tokens = []
        for reward_tokens_item_data in self.reward_tokens:
            reward_tokens_item = reward_tokens_item_data.to_dict()
            reward_tokens.append(reward_tokens_item)

        input_tokens = []
        for input_tokens_item_data in self.input_tokens:
            input_tokens_item = input_tokens_item_data.to_dict()
            input_tokens.append(input_tokens_item)

        output_tokens = []
        for output_tokens_item_data in self.output_tokens:
            output_tokens_item = output_tokens_item_data.to_dict()
            output_tokens.append(output_tokens_item)

        asset_representation = self.asset_representation

        is_whitelisted_pro = self.is_whitelisted_pro

        is_whitelisted_simple = self.is_whitelisted_simple

        votable = self.votable

        is_active = self.is_active

        is_whitelisted_limit_order = self.is_whitelisted_limit_order

        category_ids = self.category_ids

        timestamp = self.timestamp.isoformat()

        scalar_root = self.scalar_root

        initial_anchor = self.initial_anchor

        extended_info = self.extended_info.to_dict()

        is_new = self.is_new

        name = self.name

        simple_name = self.simple_name

        simple_symbol = self.simple_symbol

        simple_icon = self.simple_icon

        pro_name = self.pro_name

        farm_name = self.farm_name

        farm_symbol = self.farm_symbol

        farm_simple_name = self.farm_simple_name

        farm_simple_symbol = self.farm_simple_symbol

        farm_simple_icon = self.farm_simple_icon

        farm_pro_name = self.farm_pro_name

        farm_pro_symbol = self.farm_pro_symbol

        farm_pro_icon = self.farm_pro_icon

        base_pricing_asset: Union[None, Unset, dict[str, Any]]
        if isinstance(self.base_pricing_asset, Unset):
            base_pricing_asset = UNSET
        elif isinstance(self.base_pricing_asset, AssetResponse):
            base_pricing_asset = self.base_pricing_asset.to_dict()
        else:
            base_pricing_asset = self.base_pricing_asset

        protocol: Union[None, Unset, str]
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        underlying_pool: Union[None, Unset, str]
        if isinstance(self.underlying_pool, Unset):
            underlying_pool = UNSET
        else:
            underlying_pool = self.underlying_pool

        pro_symbol: Union[None, Unset, str]
        if isinstance(self.pro_symbol, Unset):
            pro_symbol = UNSET
        else:
            pro_symbol = self.pro_symbol

        pro_icon: Union[None, Unset, str]
        if isinstance(self.pro_icon, Unset):
            pro_icon = UNSET
        else:
            pro_icon = self.pro_icon

        accent_color: Union[None, Unset, str]
        if isinstance(self.accent_color, Unset):
            accent_color = UNSET
        else:
            accent_color = self.accent_color

        total_pt: Union[None, Unset, float]
        if isinstance(self.total_pt, Unset):
            total_pt = UNSET
        else:
            total_pt = self.total_pt

        total_sy: Union[None, Unset, float]
        if isinstance(self.total_sy, Unset):
            total_sy = UNSET
        else:
            total_sy = self.total_sy

        total_lp: Union[None, Unset, float]
        if isinstance(self.total_lp, Unset):
            total_lp = UNSET
        else:
            total_lp = self.total_lp

        total_active_supply: Union[None, Unset, float]
        if isinstance(self.total_active_supply, Unset):
            total_active_supply = UNSET
        else:
            total_active_supply = self.total_active_supply

        liquidity: Union[None, Unset, dict[str, Any]]
        if isinstance(self.liquidity, Unset):
            liquidity = UNSET
        elif isinstance(self.liquidity, ValuationResponse):
            liquidity = self.liquidity.to_dict()
        else:
            liquidity = self.liquidity

        trading_volume: Union[None, Unset, dict[str, Any]]
        if isinstance(self.trading_volume, Unset):
            trading_volume = UNSET
        elif isinstance(self.trading_volume, ValuationResponse):
            trading_volume = self.trading_volume.to_dict()
        else:
            trading_volume = self.trading_volume

        underlying_interest_apy: Union[None, Unset, float]
        if isinstance(self.underlying_interest_apy, Unset):
            underlying_interest_apy = UNSET
        else:
            underlying_interest_apy = self.underlying_interest_apy

        underlying_reward_apy: Union[None, Unset, float]
        if isinstance(self.underlying_reward_apy, Unset):
            underlying_reward_apy = UNSET
        else:
            underlying_reward_apy = self.underlying_reward_apy

        underlying_reward_apy_breakdown: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.underlying_reward_apy_breakdown, Unset):
            underlying_reward_apy_breakdown = UNSET
        elif isinstance(self.underlying_reward_apy_breakdown, list):
            underlying_reward_apy_breakdown = []
            for underlying_reward_apy_breakdown_type_0_item_data in self.underlying_reward_apy_breakdown:
                underlying_reward_apy_breakdown_type_0_item = underlying_reward_apy_breakdown_type_0_item_data.to_dict()
                underlying_reward_apy_breakdown.append(underlying_reward_apy_breakdown_type_0_item)

        else:
            underlying_reward_apy_breakdown = self.underlying_reward_apy_breakdown

        underlying_apy: Union[None, Unset, float]
        if isinstance(self.underlying_apy, Unset):
            underlying_apy = UNSET
        else:
            underlying_apy = self.underlying_apy

        implied_apy: Union[None, Unset, float]
        if isinstance(self.implied_apy, Unset):
            implied_apy = UNSET
        else:
            implied_apy = self.implied_apy

        yt_floating_apy: Union[None, Unset, float]
        if isinstance(self.yt_floating_apy, Unset):
            yt_floating_apy = UNSET
        else:
            yt_floating_apy = self.yt_floating_apy

        pt_discount: Union[None, Unset, float]
        if isinstance(self.pt_discount, Unset):
            pt_discount = UNSET
        else:
            pt_discount = self.pt_discount

        swap_fee_apy: Union[None, Unset, float]
        if isinstance(self.swap_fee_apy, Unset):
            swap_fee_apy = UNSET
        else:
            swap_fee_apy = self.swap_fee_apy

        pendle_apy: Union[None, Unset, float]
        if isinstance(self.pendle_apy, Unset):
            pendle_apy = UNSET
        else:
            pendle_apy = self.pendle_apy

        arb_apy: Union[None, Unset, float]
        if isinstance(self.arb_apy, Unset):
            arb_apy = UNSET
        else:
            arb_apy = self.arb_apy

        aggregated_apy: Union[None, Unset, float]
        if isinstance(self.aggregated_apy, Unset):
            aggregated_apy = UNSET
        else:
            aggregated_apy = self.aggregated_apy

        max_boosted_apy: Union[None, Unset, float]
        if isinstance(self.max_boosted_apy, Unset):
            max_boosted_apy = UNSET
        else:
            max_boosted_apy = self.max_boosted_apy

        lp_reward_apy: Union[None, Unset, float]
        if isinstance(self.lp_reward_apy, Unset):
            lp_reward_apy = UNSET
        else:
            lp_reward_apy = self.lp_reward_apy

        voter_apy: Union[None, Unset, float]
        if isinstance(self.voter_apy, Unset):
            voter_apy = UNSET
        else:
            voter_apy = self.voter_apy

        yt_roi: Union[None, Unset, float]
        if isinstance(self.yt_roi, Unset):
            yt_roi = UNSET
        else:
            yt_roi = self.yt_roi

        pt_roi: Union[None, Unset, float]
        if isinstance(self.pt_roi, Unset):
            pt_roi = UNSET
        else:
            pt_roi = self.pt_roi

        estimated_daily_pool_rewards: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.estimated_daily_pool_rewards, Unset):
            estimated_daily_pool_rewards = UNSET
        elif isinstance(self.estimated_daily_pool_rewards, list):
            estimated_daily_pool_rewards = []
            for estimated_daily_pool_rewards_type_0_item_data in self.estimated_daily_pool_rewards:
                estimated_daily_pool_rewards_type_0_item = estimated_daily_pool_rewards_type_0_item_data.to_dict()
                estimated_daily_pool_rewards.append(estimated_daily_pool_rewards_type_0_item)

        else:
            estimated_daily_pool_rewards = self.estimated_daily_pool_rewards

        data_updated_at: Union[None, Unset, str]
        if isinstance(self.data_updated_at, Unset):
            data_updated_at = UNSET
        elif isinstance(self.data_updated_at, datetime.datetime):
            data_updated_at = self.data_updated_at.isoformat()
        else:
            data_updated_at = self.data_updated_at

        liquidity_change_24_h: Union[None, Unset, float]
        if isinstance(self.liquidity_change_24_h, Unset):
            liquidity_change_24_h = UNSET
        else:
            liquidity_change_24_h = self.liquidity_change_24_h

        trading_volume_change_24_h: Union[None, Unset, float]
        if isinstance(self.trading_volume_change_24_h, Unset):
            trading_volume_change_24_h = UNSET
        else:
            trading_volume_change_24_h = self.trading_volume_change_24_h

        underlying_interest_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.underlying_interest_apy_change_24_h, Unset):
            underlying_interest_apy_change_24_h = UNSET
        else:
            underlying_interest_apy_change_24_h = self.underlying_interest_apy_change_24_h

        underlying_reward_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.underlying_reward_apy_change_24_h, Unset):
            underlying_reward_apy_change_24_h = UNSET
        else:
            underlying_reward_apy_change_24_h = self.underlying_reward_apy_change_24_h

        underlying_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.underlying_apy_change_24_h, Unset):
            underlying_apy_change_24_h = UNSET
        else:
            underlying_apy_change_24_h = self.underlying_apy_change_24_h

        implied_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.implied_apy_change_24_h, Unset):
            implied_apy_change_24_h = UNSET
        else:
            implied_apy_change_24_h = self.implied_apy_change_24_h

        yt_floating_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.yt_floating_apy_change_24_h, Unset):
            yt_floating_apy_change_24_h = UNSET
        else:
            yt_floating_apy_change_24_h = self.yt_floating_apy_change_24_h

        pt_discount_change_24_h: Union[None, Unset, float]
        if isinstance(self.pt_discount_change_24_h, Unset):
            pt_discount_change_24_h = UNSET
        else:
            pt_discount_change_24_h = self.pt_discount_change_24_h

        swap_fee_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.swap_fee_apy_change_24_h, Unset):
            swap_fee_apy_change_24_h = UNSET
        else:
            swap_fee_apy_change_24_h = self.swap_fee_apy_change_24_h

        pendle_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.pendle_apy_change_24_h, Unset):
            pendle_apy_change_24_h = UNSET
        else:
            pendle_apy_change_24_h = self.pendle_apy_change_24_h

        aggregated_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.aggregated_apy_change_24_h, Unset):
            aggregated_apy_change_24_h = UNSET
        else:
            aggregated_apy_change_24_h = self.aggregated_apy_change_24_h

        lp_reward_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.lp_reward_apy_change_24_h, Unset):
            lp_reward_apy_change_24_h = UNSET
        else:
            lp_reward_apy_change_24_h = self.lp_reward_apy_change_24_h

        voter_apy_change_24_h: Union[None, Unset, float]
        if isinstance(self.voter_apy_change_24_h, Unset):
            voter_apy_change_24_h = UNSET
        else:
            voter_apy_change_24_h = self.voter_apy_change_24_h

        is_featured: Union[None, Unset, bool]
        if isinstance(self.is_featured, Unset):
            is_featured = UNSET
        else:
            is_featured = self.is_featured

        is_popular: Union[None, Unset, bool]
        if isinstance(self.is_popular, Unset):
            is_popular = UNSET
        else:
            is_popular = self.is_popular

        tvl_threshold_timestamp: Union[None, Unset, str]
        if isinstance(self.tvl_threshold_timestamp, Unset):
            tvl_threshold_timestamp = UNSET
        elif isinstance(self.tvl_threshold_timestamp, datetime.datetime):
            tvl_threshold_timestamp = self.tvl_threshold_timestamp.isoformat()
        else:
            tvl_threshold_timestamp = self.tvl_threshold_timestamp

        whitelisted_pro_at: Union[None, Unset, str]
        if isinstance(self.whitelisted_pro_at, Unset):
            whitelisted_pro_at = UNSET
        elif isinstance(self.whitelisted_pro_at, datetime.datetime):
            whitelisted_pro_at = self.whitelisted_pro_at.isoformat()
        else:
            whitelisted_pro_at = self.whitelisted_pro_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "chainId": chain_id,
                "address": address,
                "symbol": symbol,
                "expiry": expiry,
                "pt": pt,
                "yt": yt,
                "sy": sy,
                "lp": lp,
                "accountingAsset": accounting_asset,
                "underlyingAsset": underlying_asset,
                "rewardTokens": reward_tokens,
                "inputTokens": input_tokens,
                "outputTokens": output_tokens,
                "assetRepresentation": asset_representation,
                "isWhitelistedPro": is_whitelisted_pro,
                "isWhitelistedSimple": is_whitelisted_simple,
                "votable": votable,
                "isActive": is_active,
                "isWhitelistedLimitOrder": is_whitelisted_limit_order,
                "categoryIds": category_ids,
                "timestamp": timestamp,
                "scalarRoot": scalar_root,
                "initialAnchor": initial_anchor,
                "extendedInfo": extended_info,
                "isNew": is_new,
                "name": name,
                "simpleName": simple_name,
                "simpleSymbol": simple_symbol,
                "simpleIcon": simple_icon,
                "proName": pro_name,
                "farmName": farm_name,
                "farmSymbol": farm_symbol,
                "farmSimpleName": farm_simple_name,
                "farmSimpleSymbol": farm_simple_symbol,
                "farmSimpleIcon": farm_simple_icon,
                "farmProName": farm_pro_name,
                "farmProSymbol": farm_pro_symbol,
                "farmProIcon": farm_pro_icon,
            }
        )
        if base_pricing_asset is not UNSET:
            field_dict["basePricingAsset"] = base_pricing_asset
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if underlying_pool is not UNSET:
            field_dict["underlyingPool"] = underlying_pool
        if pro_symbol is not UNSET:
            field_dict["proSymbol"] = pro_symbol
        if pro_icon is not UNSET:
            field_dict["proIcon"] = pro_icon
        if accent_color is not UNSET:
            field_dict["accentColor"] = accent_color
        if total_pt is not UNSET:
            field_dict["totalPt"] = total_pt
        if total_sy is not UNSET:
            field_dict["totalSy"] = total_sy
        if total_lp is not UNSET:
            field_dict["totalLp"] = total_lp
        if total_active_supply is not UNSET:
            field_dict["totalActiveSupply"] = total_active_supply
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity
        if trading_volume is not UNSET:
            field_dict["tradingVolume"] = trading_volume
        if underlying_interest_apy is not UNSET:
            field_dict["underlyingInterestApy"] = underlying_interest_apy
        if underlying_reward_apy is not UNSET:
            field_dict["underlyingRewardApy"] = underlying_reward_apy
        if underlying_reward_apy_breakdown is not UNSET:
            field_dict["underlyingRewardApyBreakdown"] = underlying_reward_apy_breakdown
        if underlying_apy is not UNSET:
            field_dict["underlyingApy"] = underlying_apy
        if implied_apy is not UNSET:
            field_dict["impliedApy"] = implied_apy
        if yt_floating_apy is not UNSET:
            field_dict["ytFloatingApy"] = yt_floating_apy
        if pt_discount is not UNSET:
            field_dict["ptDiscount"] = pt_discount
        if swap_fee_apy is not UNSET:
            field_dict["swapFeeApy"] = swap_fee_apy
        if pendle_apy is not UNSET:
            field_dict["pendleApy"] = pendle_apy
        if arb_apy is not UNSET:
            field_dict["arbApy"] = arb_apy
        if aggregated_apy is not UNSET:
            field_dict["aggregatedApy"] = aggregated_apy
        if max_boosted_apy is not UNSET:
            field_dict["maxBoostedApy"] = max_boosted_apy
        if lp_reward_apy is not UNSET:
            field_dict["lpRewardApy"] = lp_reward_apy
        if voter_apy is not UNSET:
            field_dict["voterApy"] = voter_apy
        if yt_roi is not UNSET:
            field_dict["ytRoi"] = yt_roi
        if pt_roi is not UNSET:
            field_dict["ptRoi"] = pt_roi
        if estimated_daily_pool_rewards is not UNSET:
            field_dict["estimatedDailyPoolRewards"] = estimated_daily_pool_rewards
        if data_updated_at is not UNSET:
            field_dict["dataUpdatedAt"] = data_updated_at
        if liquidity_change_24_h is not UNSET:
            field_dict["liquidityChange24h"] = liquidity_change_24_h
        if trading_volume_change_24_h is not UNSET:
            field_dict["tradingVolumeChange24h"] = trading_volume_change_24_h
        if underlying_interest_apy_change_24_h is not UNSET:
            field_dict["underlyingInterestApyChange24h"] = underlying_interest_apy_change_24_h
        if underlying_reward_apy_change_24_h is not UNSET:
            field_dict["underlyingRewardApyChange24h"] = underlying_reward_apy_change_24_h
        if underlying_apy_change_24_h is not UNSET:
            field_dict["underlyingApyChange24h"] = underlying_apy_change_24_h
        if implied_apy_change_24_h is not UNSET:
            field_dict["impliedApyChange24h"] = implied_apy_change_24_h
        if yt_floating_apy_change_24_h is not UNSET:
            field_dict["ytFloatingApyChange24h"] = yt_floating_apy_change_24_h
        if pt_discount_change_24_h is not UNSET:
            field_dict["ptDiscountChange24h"] = pt_discount_change_24_h
        if swap_fee_apy_change_24_h is not UNSET:
            field_dict["swapFeeApyChange24h"] = swap_fee_apy_change_24_h
        if pendle_apy_change_24_h is not UNSET:
            field_dict["pendleApyChange24h"] = pendle_apy_change_24_h
        if aggregated_apy_change_24_h is not UNSET:
            field_dict["aggregatedApyChange24h"] = aggregated_apy_change_24_h
        if lp_reward_apy_change_24_h is not UNSET:
            field_dict["lpRewardApyChange24h"] = lp_reward_apy_change_24_h
        if voter_apy_change_24_h is not UNSET:
            field_dict["voterApyChange24h"] = voter_apy_change_24_h
        if is_featured is not UNSET:
            field_dict["isFeatured"] = is_featured
        if is_popular is not UNSET:
            field_dict["isPopular"] = is_popular
        if tvl_threshold_timestamp is not UNSET:
            field_dict["tvlThresholdTimestamp"] = tvl_threshold_timestamp
        if whitelisted_pro_at is not UNSET:
            field_dict["whitelistedProAt"] = whitelisted_pro_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apy_breakdown_response import ApyBreakdownResponse
        from ..models.asset_response import AssetResponse
        from ..models.estimated_daily_pool_reward_response import EstimatedDailyPoolRewardResponse
        from ..models.market_extended_info_response import MarketExtendedInfoResponse
        from ..models.valuation_response import ValuationResponse

        d = dict(src_dict)
        id = d.pop("id")

        chain_id = d.pop("chainId")

        address = d.pop("address")

        symbol = d.pop("symbol")

        expiry = isoparse(d.pop("expiry"))

        pt = AssetResponse.from_dict(d.pop("pt"))

        yt = AssetResponse.from_dict(d.pop("yt"))

        sy = AssetResponse.from_dict(d.pop("sy"))

        lp = AssetResponse.from_dict(d.pop("lp"))

        accounting_asset = AssetResponse.from_dict(d.pop("accountingAsset"))

        underlying_asset = AssetResponse.from_dict(d.pop("underlyingAsset"))

        reward_tokens = []
        _reward_tokens = d.pop("rewardTokens")
        for reward_tokens_item_data in _reward_tokens:
            reward_tokens_item = AssetResponse.from_dict(reward_tokens_item_data)

            reward_tokens.append(reward_tokens_item)

        input_tokens = []
        _input_tokens = d.pop("inputTokens")
        for input_tokens_item_data in _input_tokens:
            input_tokens_item = AssetResponse.from_dict(input_tokens_item_data)

            input_tokens.append(input_tokens_item)

        output_tokens = []
        _output_tokens = d.pop("outputTokens")
        for output_tokens_item_data in _output_tokens:
            output_tokens_item = AssetResponse.from_dict(output_tokens_item_data)

            output_tokens.append(output_tokens_item)

        asset_representation = d.pop("assetRepresentation")

        is_whitelisted_pro = d.pop("isWhitelistedPro")

        is_whitelisted_simple = d.pop("isWhitelistedSimple")

        votable = d.pop("votable")

        is_active = d.pop("isActive")

        is_whitelisted_limit_order = d.pop("isWhitelistedLimitOrder")

        category_ids = cast(list[str], d.pop("categoryIds"))

        timestamp = isoparse(d.pop("timestamp"))

        scalar_root = d.pop("scalarRoot")

        initial_anchor = d.pop("initialAnchor")

        extended_info = MarketExtendedInfoResponse.from_dict(d.pop("extendedInfo"))

        is_new = d.pop("isNew")

        name = d.pop("name")

        simple_name = d.pop("simpleName")

        simple_symbol = d.pop("simpleSymbol")

        simple_icon = d.pop("simpleIcon")

        pro_name = d.pop("proName")

        farm_name = d.pop("farmName")

        farm_symbol = d.pop("farmSymbol")

        farm_simple_name = d.pop("farmSimpleName")

        farm_simple_symbol = d.pop("farmSimpleSymbol")

        farm_simple_icon = d.pop("farmSimpleIcon")

        farm_pro_name = d.pop("farmProName")

        farm_pro_symbol = d.pop("farmProSymbol")

        farm_pro_icon = d.pop("farmProIcon")

        def _parse_base_pricing_asset(data: object) -> Union["AssetResponse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                base_pricing_asset_type_1 = AssetResponse.from_dict(data)

                return base_pricing_asset_type_1
            except:  # noqa: E722
                pass
            return cast(Union["AssetResponse", None, Unset], data)

        base_pricing_asset = _parse_base_pricing_asset(d.pop("basePricingAsset", UNSET))

        def _parse_protocol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_underlying_pool(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        underlying_pool = _parse_underlying_pool(d.pop("underlyingPool", UNSET))

        def _parse_pro_symbol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pro_symbol = _parse_pro_symbol(d.pop("proSymbol", UNSET))

        def _parse_pro_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pro_icon = _parse_pro_icon(d.pop("proIcon", UNSET))

        def _parse_accent_color(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        accent_color = _parse_accent_color(d.pop("accentColor", UNSET))

        def _parse_total_pt(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_pt = _parse_total_pt(d.pop("totalPt", UNSET))

        def _parse_total_sy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_sy = _parse_total_sy(d.pop("totalSy", UNSET))

        def _parse_total_lp(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_lp = _parse_total_lp(d.pop("totalLp", UNSET))

        def _parse_total_active_supply(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_active_supply = _parse_total_active_supply(d.pop("totalActiveSupply", UNSET))

        def _parse_liquidity(data: object) -> Union["ValuationResponse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                liquidity_type_1 = ValuationResponse.from_dict(data)

                return liquidity_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ValuationResponse", None, Unset], data)

        liquidity = _parse_liquidity(d.pop("liquidity", UNSET))

        def _parse_trading_volume(data: object) -> Union["ValuationResponse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trading_volume_type_1 = ValuationResponse.from_dict(data)

                return trading_volume_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ValuationResponse", None, Unset], data)

        trading_volume = _parse_trading_volume(d.pop("tradingVolume", UNSET))

        def _parse_underlying_interest_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        underlying_interest_apy = _parse_underlying_interest_apy(d.pop("underlyingInterestApy", UNSET))

        def _parse_underlying_reward_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        underlying_reward_apy = _parse_underlying_reward_apy(d.pop("underlyingRewardApy", UNSET))

        def _parse_underlying_reward_apy_breakdown(data: object) -> Union[None, Unset, list["ApyBreakdownResponse"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                underlying_reward_apy_breakdown_type_0 = []
                _underlying_reward_apy_breakdown_type_0 = data
                for underlying_reward_apy_breakdown_type_0_item_data in _underlying_reward_apy_breakdown_type_0:
                    underlying_reward_apy_breakdown_type_0_item = ApyBreakdownResponse.from_dict(
                        underlying_reward_apy_breakdown_type_0_item_data
                    )

                    underlying_reward_apy_breakdown_type_0.append(underlying_reward_apy_breakdown_type_0_item)

                return underlying_reward_apy_breakdown_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ApyBreakdownResponse"]], data)

        underlying_reward_apy_breakdown = _parse_underlying_reward_apy_breakdown(
            d.pop("underlyingRewardApyBreakdown", UNSET)
        )

        def _parse_underlying_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        underlying_apy = _parse_underlying_apy(d.pop("underlyingApy", UNSET))

        def _parse_implied_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        implied_apy = _parse_implied_apy(d.pop("impliedApy", UNSET))

        def _parse_yt_floating_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        yt_floating_apy = _parse_yt_floating_apy(d.pop("ytFloatingApy", UNSET))

        def _parse_pt_discount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pt_discount = _parse_pt_discount(d.pop("ptDiscount", UNSET))

        def _parse_swap_fee_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        swap_fee_apy = _parse_swap_fee_apy(d.pop("swapFeeApy", UNSET))

        def _parse_pendle_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pendle_apy = _parse_pendle_apy(d.pop("pendleApy", UNSET))

        def _parse_arb_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        arb_apy = _parse_arb_apy(d.pop("arbApy", UNSET))

        def _parse_aggregated_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        aggregated_apy = _parse_aggregated_apy(d.pop("aggregatedApy", UNSET))

        def _parse_max_boosted_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_boosted_apy = _parse_max_boosted_apy(d.pop("maxBoostedApy", UNSET))

        def _parse_lp_reward_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lp_reward_apy = _parse_lp_reward_apy(d.pop("lpRewardApy", UNSET))

        def _parse_voter_apy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        voter_apy = _parse_voter_apy(d.pop("voterApy", UNSET))

        def _parse_yt_roi(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        yt_roi = _parse_yt_roi(d.pop("ytRoi", UNSET))

        def _parse_pt_roi(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pt_roi = _parse_pt_roi(d.pop("ptRoi", UNSET))

        def _parse_estimated_daily_pool_rewards(
            data: object,
        ) -> Union[None, Unset, list["EstimatedDailyPoolRewardResponse"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                estimated_daily_pool_rewards_type_0 = []
                _estimated_daily_pool_rewards_type_0 = data
                for estimated_daily_pool_rewards_type_0_item_data in _estimated_daily_pool_rewards_type_0:
                    estimated_daily_pool_rewards_type_0_item = EstimatedDailyPoolRewardResponse.from_dict(
                        estimated_daily_pool_rewards_type_0_item_data
                    )

                    estimated_daily_pool_rewards_type_0.append(estimated_daily_pool_rewards_type_0_item)

                return estimated_daily_pool_rewards_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["EstimatedDailyPoolRewardResponse"]], data)

        estimated_daily_pool_rewards = _parse_estimated_daily_pool_rewards(d.pop("estimatedDailyPoolRewards", UNSET))

        def _parse_data_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_updated_at_type_0 = isoparse(data)

                return data_updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        data_updated_at = _parse_data_updated_at(d.pop("dataUpdatedAt", UNSET))

        def _parse_liquidity_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        liquidity_change_24_h = _parse_liquidity_change_24_h(d.pop("liquidityChange24h", UNSET))

        def _parse_trading_volume_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        trading_volume_change_24_h = _parse_trading_volume_change_24_h(d.pop("tradingVolumeChange24h", UNSET))

        def _parse_underlying_interest_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        underlying_interest_apy_change_24_h = _parse_underlying_interest_apy_change_24_h(
            d.pop("underlyingInterestApyChange24h", UNSET)
        )

        def _parse_underlying_reward_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        underlying_reward_apy_change_24_h = _parse_underlying_reward_apy_change_24_h(
            d.pop("underlyingRewardApyChange24h", UNSET)
        )

        def _parse_underlying_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        underlying_apy_change_24_h = _parse_underlying_apy_change_24_h(d.pop("underlyingApyChange24h", UNSET))

        def _parse_implied_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        implied_apy_change_24_h = _parse_implied_apy_change_24_h(d.pop("impliedApyChange24h", UNSET))

        def _parse_yt_floating_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        yt_floating_apy_change_24_h = _parse_yt_floating_apy_change_24_h(d.pop("ytFloatingApyChange24h", UNSET))

        def _parse_pt_discount_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pt_discount_change_24_h = _parse_pt_discount_change_24_h(d.pop("ptDiscountChange24h", UNSET))

        def _parse_swap_fee_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        swap_fee_apy_change_24_h = _parse_swap_fee_apy_change_24_h(d.pop("swapFeeApyChange24h", UNSET))

        def _parse_pendle_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pendle_apy_change_24_h = _parse_pendle_apy_change_24_h(d.pop("pendleApyChange24h", UNSET))

        def _parse_aggregated_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        aggregated_apy_change_24_h = _parse_aggregated_apy_change_24_h(d.pop("aggregatedApyChange24h", UNSET))

        def _parse_lp_reward_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lp_reward_apy_change_24_h = _parse_lp_reward_apy_change_24_h(d.pop("lpRewardApyChange24h", UNSET))

        def _parse_voter_apy_change_24_h(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        voter_apy_change_24_h = _parse_voter_apy_change_24_h(d.pop("voterApyChange24h", UNSET))

        def _parse_is_featured(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_featured = _parse_is_featured(d.pop("isFeatured", UNSET))

        def _parse_is_popular(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_popular = _parse_is_popular(d.pop("isPopular", UNSET))

        def _parse_tvl_threshold_timestamp(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tvl_threshold_timestamp_type_0 = isoparse(data)

                return tvl_threshold_timestamp_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        tvl_threshold_timestamp = _parse_tvl_threshold_timestamp(d.pop("tvlThresholdTimestamp", UNSET))

        def _parse_whitelisted_pro_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                whitelisted_pro_at_type_0 = isoparse(data)

                return whitelisted_pro_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        whitelisted_pro_at = _parse_whitelisted_pro_at(d.pop("whitelistedProAt", UNSET))

        market_response = cls(
            id=id,
            chain_id=chain_id,
            address=address,
            symbol=symbol,
            expiry=expiry,
            pt=pt,
            yt=yt,
            sy=sy,
            lp=lp,
            accounting_asset=accounting_asset,
            underlying_asset=underlying_asset,
            reward_tokens=reward_tokens,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            asset_representation=asset_representation,
            is_whitelisted_pro=is_whitelisted_pro,
            is_whitelisted_simple=is_whitelisted_simple,
            votable=votable,
            is_active=is_active,
            is_whitelisted_limit_order=is_whitelisted_limit_order,
            category_ids=category_ids,
            timestamp=timestamp,
            scalar_root=scalar_root,
            initial_anchor=initial_anchor,
            extended_info=extended_info,
            is_new=is_new,
            name=name,
            simple_name=simple_name,
            simple_symbol=simple_symbol,
            simple_icon=simple_icon,
            pro_name=pro_name,
            farm_name=farm_name,
            farm_symbol=farm_symbol,
            farm_simple_name=farm_simple_name,
            farm_simple_symbol=farm_simple_symbol,
            farm_simple_icon=farm_simple_icon,
            farm_pro_name=farm_pro_name,
            farm_pro_symbol=farm_pro_symbol,
            farm_pro_icon=farm_pro_icon,
            base_pricing_asset=base_pricing_asset,
            protocol=protocol,
            underlying_pool=underlying_pool,
            pro_symbol=pro_symbol,
            pro_icon=pro_icon,
            accent_color=accent_color,
            total_pt=total_pt,
            total_sy=total_sy,
            total_lp=total_lp,
            total_active_supply=total_active_supply,
            liquidity=liquidity,
            trading_volume=trading_volume,
            underlying_interest_apy=underlying_interest_apy,
            underlying_reward_apy=underlying_reward_apy,
            underlying_reward_apy_breakdown=underlying_reward_apy_breakdown,
            underlying_apy=underlying_apy,
            implied_apy=implied_apy,
            yt_floating_apy=yt_floating_apy,
            pt_discount=pt_discount,
            swap_fee_apy=swap_fee_apy,
            pendle_apy=pendle_apy,
            arb_apy=arb_apy,
            aggregated_apy=aggregated_apy,
            max_boosted_apy=max_boosted_apy,
            lp_reward_apy=lp_reward_apy,
            voter_apy=voter_apy,
            yt_roi=yt_roi,
            pt_roi=pt_roi,
            estimated_daily_pool_rewards=estimated_daily_pool_rewards,
            data_updated_at=data_updated_at,
            liquidity_change_24_h=liquidity_change_24_h,
            trading_volume_change_24_h=trading_volume_change_24_h,
            underlying_interest_apy_change_24_h=underlying_interest_apy_change_24_h,
            underlying_reward_apy_change_24_h=underlying_reward_apy_change_24_h,
            underlying_apy_change_24_h=underlying_apy_change_24_h,
            implied_apy_change_24_h=implied_apy_change_24_h,
            yt_floating_apy_change_24_h=yt_floating_apy_change_24_h,
            pt_discount_change_24_h=pt_discount_change_24_h,
            swap_fee_apy_change_24_h=swap_fee_apy_change_24_h,
            pendle_apy_change_24_h=pendle_apy_change_24_h,
            aggregated_apy_change_24_h=aggregated_apy_change_24_h,
            lp_reward_apy_change_24_h=lp_reward_apy_change_24_h,
            voter_apy_change_24_h=voter_apy_change_24_h,
            is_featured=is_featured,
            is_popular=is_popular,
            tvl_threshold_timestamp=tvl_threshold_timestamp,
            whitelisted_pro_at=whitelisted_pro_at,
        )

        market_response.additional_properties = d
        return market_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

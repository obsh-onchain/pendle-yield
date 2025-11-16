from enum import Enum


class MultiRouteConvertResponseAction(str, Enum):
    ADD_LIQUIDITY = "add-liquidity"
    ADD_LIQUIDITY_DUAL = "add-liquidity-dual"
    CONVERT_LP_TO_PT = "convert-lp-to-pt"
    EXIT_MARKET = "exit-market"
    MINT_PY = "mint-py"
    MINT_SY = "mint-sy"
    PENDLE_SWAP = "pendle-swap"
    REDEEM_PY = "redeem-py"
    REDEEM_SY = "redeem-sy"
    REMOVE_LIQUIDITY = "remove-liquidity"
    REMOVE_LIQUIDITY_DUAL = "remove-liquidity-dual"
    ROLL_OVER_PT = "roll-over-pt"
    SWAP = "swap"
    TRANSFER_LIQUIDITY = "transfer-liquidity"

    def __str__(self) -> str:
        return str(self.value)

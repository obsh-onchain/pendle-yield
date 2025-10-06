from enum import Enum


class PnLTransactionEntityAction(str, Enum):
    ADDLIQUIDITYDUALTOKENANDPT = "addLiquidityDualTokenAndPt"
    ADDLIQUIDITYSINGLEPT = "addLiquiditySinglePt"
    ADDLIQUIDITYSINGLETOKEN = "addLiquiditySingleToken"
    ADDLIQUIDITYSINGLETOKENKEEPYT = "addLiquiditySingleTokenKeepYt"
    BUYPT = "buyPt"
    BUYPTLIMITORDER = "buyPtLimitOrder"
    BUYYT = "buyYt"
    BUYYTLIMITORDER = "buyYtLimitOrder"
    MINTPY = "mintPy"
    REDEEMMARKETREWARDS = "redeemMarketRewards"
    REDEEMPY = "redeemPy"
    REDEEMYTREWARDS = "redeemYtRewards"
    REDEEMYTYIELD = "redeemYtYield"
    REMOVELIQUIDITYDUALTOKENANDPT = "removeLiquidityDualTokenAndPt"
    REMOVELIQUIDITYSINGLETOKEN = "removeLiquiditySingleToken"
    REMOVELIQUIDITYTOPT = "removeLiquidityToPt"
    SELLPT = "sellPt"
    SELLPTLIMITORDER = "sellPtLimitOrder"
    SELLYT = "sellYt"
    SELLYTLIMITORDER = "sellYtLimitOrder"
    SWAPPTTOYT = "swapPtToYt"
    SWAPYTTOPT = "swapYtToPt"
    TRANSFERLPIN = "transferLpIn"
    TRANSFERLPOUT = "transferLpOut"
    TRANSFERPTIN = "transferPtIn"
    TRANSFERPTOUT = "transferPtOut"
    TRANSFERYTIN = "transferYtIn"
    TRANSFERYTOUT = "transferYtOut"

    def __str__(self) -> str:
        return str(self.value)

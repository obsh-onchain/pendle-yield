from enum import Enum


class SdkControllerSwapPtCrossChainExactAmountType(str, Enum):
    PT = "pt"
    TOKEN = "token"

    def __str__(self) -> str:
        return str(self.value)

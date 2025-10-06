from enum import Enum


class MerkleControllerGetProofByAddressCampaign(str, Enum):
    ARBITRUM_GRANT = "arbitrum-grant"
    EXTERNAL_REWARDS = "external-rewards"
    MULTI_TOKEN = "multi-token"
    VEPENDLE = "vependle"
    VEPENDLE_USD = "vependle-usd"

    def __str__(self) -> str:
        return str(self.value)

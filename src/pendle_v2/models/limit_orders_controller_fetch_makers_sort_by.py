from enum import Enum


class LimitOrdersControllerFetchMakersSortBy(str, Enum):
    NUM_ORDERS = "num_orders"
    SUM_ORDER_SIZE = "sum_order_size"

    def __str__(self) -> str:
        return str(self.value)

from abc import ABC, abstractmethod

from .company import Company


class StockExchange(ABC):
    @abstractmethod
    def get_stock_exchange_quotations(self) -> list[Company]:
        pass

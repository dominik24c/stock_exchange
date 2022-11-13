from celery import shared_task
from django.core.cache import cache
from django.conf import settings

from .core import save_stock_exchange_to_redis
from .core.stock_exchange_bankier import StockExchangeBankier
# from .core.stock_exchange_dto import StockExchangeDTO


@shared_task
def save_stock_exchange_data() -> None:
    # save_stock_exchange_to_redis(StockExchangeDTO())
    save_stock_exchange_to_redis(StockExchangeBankier())

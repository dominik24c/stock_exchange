from django.core.cache import cache
from django.conf import settings

from .company import Company
from .stock_exchange import StockExchange


def get_stock_exchange_from_redis() -> list[dict]:
    companies = []
    for idx in range(settings.AMOUNT_OF_COMPANIES):
        company = cache.get(f'{settings.CACHE_KEY_NAME}{idx}')
        if company is not None:
            companies.append(company.as_dict())
    return companies


def save_stock_exchange_to_redis(se: StockExchange) -> None:
    for idx, company_obj in enumerate(se.get_stock_exchange_quotations()):
        # value = cache.get(f'{settings.CACHE_KEY_NAME}{idx}')
        # if value is not None:
        #     print(value)
        cache.set(f'{settings.CACHE_KEY_NAME}{idx}', company_obj)

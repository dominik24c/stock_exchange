import datetime
import random
from decimal import Decimal

from django.conf import settings

from .stock_exchange import StockExchange
from .company import Company


class StockExchangeDTO(StockExchange):
    def get_stock_exchange_quotations(self) -> list[Company]:
        companies = []
        for i in range(settings.AMOUNT_OF_COMPANIES):
            exchange = round(random.uniform(0.2, 4), 4)
            days = random.randint(0, 1)
            hours = round(random.uniform(0, 2), 4)
            date = datetime.datetime.now() - datetime.timedelta(days=days, hours=hours)
            companies.append(Company(f"Company{i}", Decimal(str(exchange)),
                                     Decimal(str(round(random.uniform(-2, 5), 4))),
                                     f"{round(random.uniform(0.2, 2), 4)}%",
                                     random.randint(1, 100), random.randint(1, 1000),
                                     Decimal(str(round(exchange + random.uniform(0.2, 1), 4))),
                                     Decimal(str(round(exchange + random.uniform(0.5, 1), 4))),
                                     Decimal(str(round(exchange + random.uniform(-0.3, 0.0), 4))),
                                     date.strftime("%d.%m %H:%M")))

        return companies

from dataclasses import dataclass, asdict
from decimal import Decimal


@dataclass
class Company:
    name: str
    exchange: Decimal
    rate_change: Decimal
    rate_change_percent: str
    number_of_transaction: int
    turnover: int
    opening: Decimal
    min: Decimal
    max: Decimal
    updated_at: str

    def __str__(self) -> str:
        return f"{self.name} {self.exchange} {self.updated_at}"

    def as_dict(self) -> dict:
        company_dict = {}
        for k, v in asdict(self).items():
            if isinstance(v, Decimal):
                company_dict[k] = str(v)
            else:
                company_dict[k] = v
        return company_dict

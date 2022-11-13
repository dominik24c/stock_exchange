from typing import Type, overload
from decimal import Decimal


@overload
def convert_str_to_number(value: str, cls: Type[int]) -> int:
    ...


@overload
def convert_str_to_number(value: str, cls: Type[float]) -> float:
    ...


@overload
def convert_str_to_number(value: str, cls: Type[Decimal]) -> Decimal:
    ...


def convert_str_to_number(value, cls: Type[int] | Type[float] | Type[Decimal]) -> int | float | Decimal:
    """Remove &nbsp html code(one space)"""
    utilized_value = "".join(value.split())
    if cls is Decimal:
        utilized_value = utilized_value.replace(',', '.')
    return cls(utilized_value)

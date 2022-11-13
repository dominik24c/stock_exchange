from decimal import Decimal

import requests
from bs4 import BeautifulSoup
from django.conf import settings

from .company import Company
from .exceptions import InvalidResponseStatusCode, InvalidAmountOfCompanies
from .stock_exchange import StockExchange
from .utils import convert_str_to_number


class StockExchangeBankier(StockExchange):
    def get_stock_exchange_quotations(self) -> list[Company]:
        companies = []
        response = requests.get(settings.URL)
        # print(response)
        if response.status_code != 200:
            raise InvalidResponseStatusCode
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            # print(soup.prettify())
            section = soup.select_one('section#quotes > div#boxQuotes > div.boxContent')
            table = section.select_one('table.sortTable.floatingHeaderTable')
            tbody = table.select_one('tbody')
            table_rows = tbody.find_all('tr')
            # print(len(table_rows))
            if settings.AMOUNT_OF_COMPANIES > len(table_rows):
                raise InvalidAmountOfCompanies

            for i, r in enumerate(table_rows):
                if settings.AMOUNT_OF_COMPANIES <= i:
                    break
                p = r.select_one('td:nth-child(1) > a')
                if p is not None:
                    company_name = p.attrs.get('title')
                    exchange = convert_str_to_number(r.select_one('td:nth-child(2)').text, Decimal)  # kurs
                    rate_change = convert_str_to_number(r.select_one('td:nth-child(3)').text, Decimal)  # zmiana
                    rate_change_percent = r.select_one('td:nth-child(4)').text  # zmian procentowa
                    number_of_transaction = convert_str_to_number(r.select_one('td:nth-child(5)').text, int)
                    turnover = convert_str_to_number(r.select_one('td:nth-child(6)').text, int)  # obrot
                    opening = convert_str_to_number(r.select_one('td:nth-child(7)').text, Decimal)  # otawrcie
                    max_val = convert_str_to_number(r.select_one('td:nth-child(8)').text, Decimal)  # min
                    min_val = convert_str_to_number(r.select_one('td:nth-child(9)').text, Decimal)  # max
                    updated_at = r.select_one('td:nth-child(10)').text
                    companies.append(
                        Company(company_name, exchange, rate_change, rate_change_percent, number_of_transaction,
                                turnover,
                                opening, max_val, min_val, updated_at))
                    # print(f"{company_name} {exchange} {rate_change} {rate_change_percent} {number_of_transaction}")
                    # print(f"{turnover} {opening} {max_val} {min_val} {updated_at}")
        return companies

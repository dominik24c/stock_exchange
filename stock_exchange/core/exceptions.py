class StockExchangeException(Exception):
    pass


class InvalidResponseStatusCode(StockExchangeException):
    pass


class InvalidAmountOfCompanies(StockExchangeException):
    pass

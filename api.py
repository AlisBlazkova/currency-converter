from currency_converter import CurrencyConverter


def get(amount, input_currency, output_currency):
    """
    This function responds to a request for /api/currency_converter/{amount}/{input_currency}/{output_currency}.
    :param amount: The currency amount which you want to convert.
    :param input_currency: The currency code or currency symbol which you want to convert.
    :param output_currency: The currency code or currency symbol in which you want to convert.
    :return: The converted amount in json format.
    """

    converter = CurrencyConverter()
    # it returns comma when you do not enter currency to 'output_currency'
    if output_currency == ",":
        output_currency = ""
    return converter.convert(amount, input_currency, output_currency)

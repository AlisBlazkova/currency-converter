import click
import json

from currency_converter import CurrencyConverter


@click.command()
@click.option('--amount', prompt='Please, insert the amount of the currency.', type=float,
              help='Insert the amount in a float of the currency which you want to convert.')
@click.option('--input_currency', prompt='Please, insert the currency which you want to convert.',
              help='The currency which you want to convert. Insert currency code or currency symbol.')
@click.option('--output_currency',
              help='The currency in which you want to convert. Insert currency code or currency symbol.')
def currency_converter(amount, input_currency, output_currency):
    """
    The program takes AMOUNT of the currency
    that you want to convert from INPUT_CURRENCY to OUTPUT_CURRENCY.
    :return The dictionary of data in json format which contains converted amount.
    """

    converter = CurrencyConverter()
    conversion = converter.convert(amount, input_currency, output_currency)
    print(json.dumps(conversion, sort_keys=True, indent=4))


if __name__ == '__main__':
    currency_converter()

from unittest import TestCase

from currency_converter import CurrencyConverter


class TestCurrencyConverter(TestCase):
    def test_input_with_codes(self):
        cc = CurrencyConverter()
        conversion = cc.convert(100, 'EUR', 'CZK')
        amount = conversion['input']['amount']
        input_currency = conversion['input']['currency']
        output_currency = list(conversion['output'].keys())[0]

        self.assertEqual(amount, 100.0)
        self.assertEqual(input_currency, 'EUR')
        self.assertEqual(output_currency, 'CZK')

    def test_input_with_one_symbol(self):
        cc = CurrencyConverter()
        conversion = cc.convert(0.9, '¥', 'AUD')
        amount = conversion['input']['amount']
        input_currency = conversion['input']['currency']
        output_currency = list(conversion['output'].keys())[0]

        self.assertEqual(amount, 0.9)
        self.assertEqual(input_currency, 'CNY')
        self.assertEqual(output_currency, 'AUD')

    def test_input_with_two_symbols(self):
        cc = CurrencyConverter()
        conversion = cc.convert(1.4, '€', '¥')
        amount = conversion['input']['amount']
        input_currency = conversion['input']['currency']
        output_currency = list(conversion['output'].keys())[0]

        self.assertEqual(amount, 1.4)
        self.assertEqual(input_currency, 'EUR')
        self.assertEqual(output_currency, 'CNY')

    def test_only_input_currency_code(self):
        cc = CurrencyConverter()
        conversion = cc.convert(10.84, 'GBP', None)
        amount = conversion['input']['amount']
        input_currency = conversion['input']['currency']
        output_currency = list(conversion['output'].keys())

        self.assertEqual(amount, 10.84)
        self.assertEqual(input_currency, 'GBP')
        self.assertTrue(len(output_currency) > 1)

    def test_only_input_currency_symbol(self):
        cc = CurrencyConverter()
        conversion = cc.convert(6.3, '€', None)
        amount = conversion['input']['amount']
        input_currency = conversion['input']['currency']
        output_currency = list(conversion['output'].keys())

        self.assertEqual(amount, 6.3)
        self.assertEqual(input_currency, 'EUR')
        self.assertTrue(len(output_currency) > 1)

    def test_error_message(self):
        cc = CurrencyConverter()
        conversion = cc.convert(5.48, '$', None)
        expected = {'message': 'Currency code or symbol is not supported.'}, 500

        self.assertEqual(conversion, expected)

    def test_json_data_with_codes(self):
        cc = CurrencyConverter()
        conversion = cc.convert(100, 'EUR', 'CZK')
        expected = {
            "input": {
                "amount": 100.0,
                "currency": "EUR"
            },
            "output": {
                "CZK": 2560.9
            }
        }

        self.assertEqual(conversion, expected,
                         f"The JSON export of the currency is incorrect. Received {conversion}, expected {expected}.")

    def test_json_data_with_symbols(self):
        cc = CurrencyConverter()
        conversion = cc.convert(1.6, '€', '¥')
        expected = {
            "input": {
                "amount": 1.6,
                "currency": "EUR"
            },
            "output": {
                "CNY": 12.45
            }
        }

        self.assertEqual(conversion, expected,
                         f"The JSON export of the currency is incorrect. Received {conversion}, expected {expected}.")

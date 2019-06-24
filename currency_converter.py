from forex_python.converter import CurrencyRates, CurrencyCodes


class CurrencyConverter:
    def __init__(self):
        self.cc = CurrencyCodes()
        self.cr = CurrencyRates()

    def get_code_from_symbol(self, input_currency, output_currency):
        """
        If 'input_currency' or 'output_currency' contain a currency symbol,
        this function transforms the currency symbol to the currency code.
        :return: The currency code.
        """

        input_currency_code = self.cc.get_currency_code_from_symbol(input_currency)
        output_currency_code = self.cc.get_currency_code_from_symbol(output_currency)

        if input_currency_code:
            input_currency = input_currency_code

        if output_currency_code:
            output_currency = output_currency_code

        return input_currency, output_currency

    @staticmethod
    def json_data(amount, input_currency, output_currency):
        output_data = {
            "input": {"amount": amount, "currency": input_currency},
            "output": output_currency,
        }

        return output_data

    def convert(self, amount, input_currency, output_currency):
        """
        This function converts the currency amount from 'input_currency' to 'output_currency'.
        :param amount: The amount of the currency which you want to convert.
        :param input_currency: The currency from which you want to convert.
        :param output_currency: The currency to which you want to convert.
        :return: The converted amount.
        """

        input_currency, output_currency = self.get_code_from_symbol(
            input_currency, output_currency
        )

        try:
            if output_currency:
                converted_amount = self.cr.convert(
                    input_currency, output_currency, amount
                )
                output_currency = {output_currency: round(converted_amount, 2)}
                return CurrencyConverter.json_data(
                    amount, input_currency, output_currency
                )
            else:
                output_currency = self.convert_all_codes(amount, input_currency)
                return CurrencyConverter.json_data(
                    amount, input_currency, output_currency
                )
        except:
            return {"message": "Currency code or symbol is not supported."}, 500

    def convert_all_codes(self, amount, input_currency):
        """
        If 'output_currency' is missing, it converts the amount to all possible currencies.
        :return: The converted amount all possible currencies.
        """

        rates_all_codes = self.cr.get_rates(input_currency)
        return {key: round(value * amount, 2) for key, value in rates_all_codes.items()}

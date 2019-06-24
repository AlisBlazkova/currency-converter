# Currency Converter
Entry task for Kiwi.com

The project with Click, Forex Python, web API, Connexion, Swagger UI, Unit test and Travis CI.

## Currency Source
Forex Python is a Free Foreign exchange rates and currency conversion.

https://ratesapi.io is a free API for current and historical foreign exchange rates published by European Central Bank.
The rates are updated daily 3PM CET.

## Requirements
```
pip install -r requirements.txt
```

## Tests
Tests run automatized thanks to Travis CI.

## Parameters
- `amount` - amount which we want to convert
- `input_currency` - currency code or currency symbol
- `output_currency` - currency code or currency symbol

## Functionality
If `output_currency` parameter is missing, it converts to all possible currencies.

## Output
- json with following structure
```
{
    "input": { 
        "amount": <float>,
        "currency": <3 letter currency code>
    }
    "output": {
        <3 letter currency code>: <float>
    }
}
```

## CLI Usage
```
./cli.py --amount 100 --input_currency EUR --output_currency CZK
{
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2560.1
    }
}
```

```
./cli.py --amount 1.4 --input_currency ¥ --output_currency AUD
{
    "input": {
        "amount": 1.4,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.29
    }
}
```

```
./cli.py --amount 10.02 --input_currency €
{
    "input": {
        "amount": 10.02,
        "currency": "EUR"
    },
    "output": {
        "AUD": 16.42,
        "BGN": 19.6,
        "BRL": 43.65,
        "CAD": 15.06,
        "CHF": 11.13,
        "CNY": 78.51,
        "CZK": 256.52,
        "DKK": 74.81,
        "GBP": 8.95,
        "HKD": 89.18,
        "HRK": 74.11,
        "HUF": 3249.39,
        "IDR": 161572.5,
        "ILS": 41.11,
        "INR": 792.45,
        "ISK": 1417.83,
        "JPY": 1224.94,
        "KRW": 13204.06,
        "MXN": 218.67,
        "MYR": 47.27,
        "NOK": 96.84,
        "NZD": 17.28,
        "PHP": 586.48,
        "PLN": 42.63,
        "RON": 47.28,
        "RUB": 718.56,
        "SEK": 106.29,
        "SGD": 15.46,
        "THB": 350.78,
        "TRY": 66.18,
        "USD": 11.42,
        "ZAR": 163.62
	}
}
```

## Web API
Web App is deployed on [PythonAnywhere](https://www.pythonanywhere.com).

Here is my app [Currency Converter](https://alisblazkova.pythonanywhere.com/api/ui).

BUT OpenApi 3.0 does not work correctly with PythonAnywhere. So rather run web Api in CLI.

1. Run ```server.py```
2. Enter to browser ```http://127.0.0.1:5000/api/ui/```

```
"GET /api/currency_converter/14/MXN/GBP HTTP/1.1" 200
{
	"input": {
		"amount": 14,
		"currency": "MXN"
	},
	"output": {
		"GBP": 0.57
	}
}
```

```
"GET /api/currency_converter/120/Kč/, HTTP/1.1" 200
{
	"input": {
		"amount": 120,
		"currency": "CZK"
	},
	"output": {
		"AUD": 7.68,
		"BGN": 9.17,
		"BRL": 20.42,
		"CAD": 7.05,
		"CHF": 5.21,
		"CNY": 36.73,
		"CZK": 120,
		"DKK": 35,
		"EUR": 4.69,
		"GBP": 4.19,
		"HKD": 41.72,
		"HRK": 34.67,
		"HUF": 1520.05,
		"IDR": 75582.99,
		"ILS": 19.23,
		"INR": 370.7,
		"ISK": 663.26,
		"JPY": 573.02,
		"KRW": 6176.81,
		"MXN": 102.29,
		"MYR": 22.11,
		"NOK": 45.3,
		"NZD": 8.08,
		"PHP": 274.35,
		"PLN": 19.94,
		"RON": 22.12,
		"RUB": 336.14,
		"SEK": 49.72,
		"SGD": 7.23,
		"THB": 164.09,
		"TRY": 30.96,
		"USD": 5.34,
		"ZAR": 76.54
	}
}
```

## Author
Alena Blažková

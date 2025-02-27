import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        float_argv = float(sys.argv[1])
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        rate_float_value = response.json()['bpi']['USD']['rate_float']
        bitcoin_value = float(rate_float_value) * float(sys.argv[1])
        print(f'${bitcoin_value:,.4f}')
    except ValueError:
        sys.exit("Command-line argument is not a number")

import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument ")

try:
    coin = float(sys.argv[1])
except ValueError:
     sys.exit("Command-line argument is not a number")

try:
    res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    res.raise_for_status()
    data = res.json()
    usd_dollar = data["bpi"]["USD"]["rate_float"]
except requests.RequestException as error:
    sys.exit(f"${cost:,.4f}")

cost = coin * usd_dollar
if len(sys.argv) == 2:
    print(f"${cost:,.4f}")








import munch
import requests
import json
import runner


response = requests.get(
    'https://fmpcloud.io/api/v3/stock/list?apikey=e5ccbcc74abe54698f96836dd4c51d48')
symbolsList = response.json()
runner.analyze_stocks(symbolsList)

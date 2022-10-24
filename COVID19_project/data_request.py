import requests
import json
from datetime import datetime

def covid_data_request():

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix = int(yesterday.timestamp() * 1000)

    last_day_data = request.get(f"https://api.covidtracking.com/v2/us/daily/{yesterday_unix}.json")

    last_day_data_json = last_day_data.json()
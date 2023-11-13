import pandas as pd
import requests
import json
from tokens import Tokens
from requests import get
tokens=Tokens()

page=1
while True:
    url = f'https://www.strava.com/api/v3/activities?access_token={tokens.get_access_token()}&per_page=200&page={page}'
    requests=get(url).json()
    if not requests:
        break
    for activity in requests:
        print(activity['name'])
        
    page+=1
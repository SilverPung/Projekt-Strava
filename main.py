import requests
import json
from tokens import Tokens
from requests import get
from database import Connection
import sqlite3
tokens=Tokens()

page=1
while True:
    url = f'https://www.strava.com/api/v3/activities?access_token={tokens.get_access_token()}&per_page=200&page={page}'
    requests=get(url).json()
    if not requests:
        break
    with sqlite3.connect("database.db")as connection:
        connect=Connection(connection)
        for activity in requests:
            connect.add_activity(activity["id"],activity["athlete"]["id"],activity["name"],activity["distance"],activity["start_date_local"])
            #connect.add_activity()
            
    page+=1
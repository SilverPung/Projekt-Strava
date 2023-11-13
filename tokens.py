import pandas as pd
import requests
from requests import get,post
import json
import time
class Tokens():
    def __init__(self) -> None:
        # Get the tokens from file to connect to Strava
        with open('strava_tokens.json') as json_file:
            self.strava_tokens = json.load(json_file)
        # If access_token has expired then use the refresh_token to get the new access_token
        if self.strava_tokens['expires_at'] < time.time():
        #Make Strava auth API call with current refresh token
            response = requests.post(
                                url = 'https://www.strava.com/oauth/token',
                                data = {
                                        'client_id': 116334,
                                        'client_secret': '73a8fb9e3ce9260295c4f312063b3a7c4fc25d5c',
                                        'grant_type': 'refresh_token',
                                        'refresh_token': self.strava_tokens['refresh_token']
                                        }
                            )
        #Save response as json in new variable
            new_strava_tokens = response.json()
        # Save new tokens to file
            with open('strava_tokens.json', 'w') as outfile:
                json.dump(new_strava_tokens, outfile)
        #Use new Strava tokens from now
            self.strava_tokens = new_strava_tokens
    def get_access_token(self):
        return self.strava_tokens['access_token']
    def get_refresh_token(self):
        return self.strava_tokens['refresh_token']
    def get_tokens(self):
        return self.strava_tokens
def get_autorization():
    pass
#to write



from tokens import Tokens
import requests
from requests import get
tokens=Tokens()
url=f'https://www.strava.com/api/v3/athlete?code=153234943cc8d13cbdcebb2620e0a87b98c5fe86'
print(get(url).text)
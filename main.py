from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
id = 789 # Long | The identifier of the activity.

try: 
    # Get Activity Zones
    api_response = api_instance.getZonesByActivityId(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->getZonesByActivityId: %s\n" % e)
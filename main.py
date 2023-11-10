from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The name of the activity.
type = 'type_example' # str | Type of activity. For example - Run, Ride etc.
start_date_local = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | ISO 8601 formatted date time.
elapsed_time = 56 # int | In seconds.
description = 'description_example' # str | Description of the activity. (optional)
distance = 3.4 # float | In meters. (optional)
trainer = 56 # int | Set to 1 to mark as a trainer activity. (optional)
photo_ids = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | List of native photo ids to attach to the activity. (optional)
commute = 56 # int | Set to 1 to mark as commute. (optional)

try:
    # Create an Activity
    api_response = api_instance.create_activity(name, type, start_date_local, elapsed_time, description=description, distance=distance, trainer=trainer, photo_ids=photo_ids, commute=commute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->create_activity: %s\n" % e)
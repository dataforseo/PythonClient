# BusinessDataGoogleLocationsCountryResponseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | the current version of the API | [optional] 
**status_code** | **int** | general status code you can find the full list of the response codes here | [optional] 
**status_message** | **str** | general informational message you can find the full list of general informational messages here | [optional] 
**time** | **str** | total execution time, seconds | [optional] 
**cost** | **float** | total tasks cost, USD | [optional] 
**tasks_count** | **int** | the number of tasks in the tasks array | [optional] 
**tasks_error** | **int** | the number of tasks in the tasks array returned with an error | [optional] 
**tasks** | [**List[BusinessDataGoogleLocationsCountryTaskInfo]**](BusinessDataGoogleLocationsCountryTaskInfo.md) | array of tasks | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_locations_country_response_info import BusinessDataGoogleLocationsCountryResponseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleLocationsCountryResponseInfo from a JSON string
business_data_google_locations_country_response_info_instance = BusinessDataGoogleLocationsCountryResponseInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataGoogleLocationsCountryResponseInfo.to_json())

# convert the object into a dict
business_data_google_locations_country_response_info_dict = business_data_google_locations_country_response_info_instance.to_dict()
# create an instance of BusinessDataGoogleLocationsCountryResponseInfo from a dict
business_data_google_locations_country_response_info_from_dict = BusinessDataGoogleLocationsCountryResponseInfo.from_dict(business_data_google_locations_country_response_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



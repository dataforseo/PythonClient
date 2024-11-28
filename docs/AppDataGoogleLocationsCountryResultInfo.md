# AppDataGoogleLocationsCountryResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code | [optional] 
**location_name** | **str** | full name of the location | [optional] 
**location_name_parent** | **str** | the name of the superordinate location example: \&quot;location_code\&quot;: 1006473, \&quot;location_name\&quot;: \&quot;Altrincham,England,United Kingdom\&quot;, \&quot;location_name_parent\&quot;: \&quot;England,United Kingdom\&quot;, where location_name_parent corresponds to: \&quot;location_code\&quot;: 20339, \&quot;location_name\&quot;: \&quot;England,United Kingdom\&quot; | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 
**location_type** | **str** | location type | [optional] 

## Example

```python
from dataforseo_client.models.app_data_google_locations_country_result_info import AppDataGoogleLocationsCountryResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataGoogleLocationsCountryResultInfo from a JSON string
app_data_google_locations_country_result_info_instance = AppDataGoogleLocationsCountryResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataGoogleLocationsCountryResultInfo.to_json())

# convert the object into a dict
app_data_google_locations_country_result_info_dict = app_data_google_locations_country_result_info_instance.to_dict()
# create an instance of AppDataGoogleLocationsCountryResultInfo from a dict
app_data_google_locations_country_result_info_from_dict = AppDataGoogleLocationsCountryResultInfo.from_dict(app_data_google_locations_country_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppDataAppleLocationsResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code | [optional] 
**location_name** | **str** | full name of the location | [optional] 
**location_name_parent** | **int** | the name of the superordinate location example: \&quot;location_code\&quot;: 1006473, \&quot;location_name\&quot;: \&quot;Altrincham,England,United Kingdom\&quot;, \&quot;location_name_parent\&quot;: \&quot;England,United Kingdom\&quot;, where location_name_parent corresponds to: \&quot;location_code\&quot;: 20339, \&quot;location_name\&quot;: \&quot;England,United Kingdom\&quot; note: Apple App Data API currently supports countries only, that is why this value will always be null | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 
**location_type** | **str** | location type | [optional] 

## Example

```python
from dataforseo_client.models.app_data_apple_locations_result_info import AppDataAppleLocationsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataAppleLocationsResultInfo from a JSON string
app_data_apple_locations_result_info_instance = AppDataAppleLocationsResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataAppleLocationsResultInfo.to_json())

# convert the object into a dict
app_data_apple_locations_result_info_dict = app_data_apple_locations_result_info_instance.to_dict()
# create an instance of AppDataAppleLocationsResultInfo from a dict
app_data_apple_locations_result_info_from_dict = AppDataAppleLocationsResultInfo.from_dict(app_data_apple_locations_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BusinessDataGoogleLocationsCountryResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code | [optional] 
**location_name** | **str** | full name of the location | [optional] 
**location_name_parent** | **str** | the name of the superordinate location example: \&quot;location_code\&quot;: 9041134, \&quot;location_name\&quot;: \&quot;Vienna International Airport,Lower Austria,Austria\&quot;, \&quot;location_name_parent\&quot;: \&quot;Lower Austria,Austria\&quot; | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 
**location_type** | **str** | location type | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_locations_country_result_info import BusinessDataGoogleLocationsCountryResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleLocationsCountryResultInfo from a JSON string
business_data_google_locations_country_result_info_instance = BusinessDataGoogleLocationsCountryResultInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataGoogleLocationsCountryResultInfo.to_json()

# convert the object into a dict
business_data_google_locations_country_result_info_dict = business_data_google_locations_country_result_info_instance.to_dict()
# create an instance of BusinessDataGoogleLocationsCountryResultInfo from a dict
business_data_google_locations_country_result_info_form_dict = business_data_google_locations_country_result_info.from_dict(business_data_google_locations_country_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



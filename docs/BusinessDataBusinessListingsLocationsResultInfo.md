# BusinessDataBusinessListingsLocationsResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_name** | **str** | full name of the location | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 
**business_count** | **int** | number of businesses in this location in our database | [optional] 

## Example

```python
from dataforseo_client.models.business_data_business_listings_locations_result_info import BusinessDataBusinessListingsLocationsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataBusinessListingsLocationsResultInfo from a JSON string
business_data_business_listings_locations_result_info_instance = BusinessDataBusinessListingsLocationsResultInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataBusinessListingsLocationsResultInfo.to_json()

# convert the object into a dict
business_data_business_listings_locations_result_info_dict = business_data_business_listings_locations_result_info_instance.to_dict()
# create an instance of BusinessDataBusinessListingsLocationsResultInfo from a dict
business_data_business_listings_locations_result_info_form_dict = business_data_business_listings_locations_result_info.from_dict(business_data_business_listings_locations_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



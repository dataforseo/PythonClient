# BusinessAddressLocationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lines** | **List[Optional[str]]** | business address contains few address lines specified by the business entity | [optional] 
**latitude** | **str** | latitude in GPS coordinates | [optional] 
**longitude** | **str** | longitude in GPS coordinates | [optional] 

## Example

```python
from dataforseo_client.models.business_address_location_info import BusinessAddressLocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessAddressLocationInfo from a JSON string
business_address_location_info_instance = BusinessAddressLocationInfo.from_json(json)
# print the JSON string representation of the object
print BusinessAddressLocationInfo.to_json()

# convert the object into a dict
business_address_location_info_dict = business_address_location_info_instance.to_dict()
# create an instance of BusinessAddressLocationInfo from a dict
business_address_location_info_form_dict = business_address_location_info.from_dict(business_address_location_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



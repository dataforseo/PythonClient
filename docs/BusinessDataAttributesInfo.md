# BusinessDataAttributesInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_attributes** | **Dict[str, Optional[List[Optional[str]]]]** | available attributes indicates attributes a business entity can offer | [optional] 
**unavailable_attributes** | **Dict[str, Optional[List[Optional[str]]]]** | unavailable attributes indicates attributes a business entity cannot offer | [optional] 

## Example

```python
from dataforseo_client.models.business_data_attributes_info import BusinessDataAttributesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataAttributesInfo from a JSON string
business_data_attributes_info_instance = BusinessDataAttributesInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataAttributesInfo.to_json())

# convert the object into a dict
business_data_attributes_info_dict = business_data_attributes_info_instance.to_dict()
# create an instance of BusinessDataAttributesInfo from a dict
business_data_attributes_info_from_dict = BusinessDataAttributesInfo.from_dict(business_data_attributes_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



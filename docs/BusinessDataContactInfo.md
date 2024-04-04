# BusinessDataContactInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**value** | **str** | contact displayed in SERP  example: \&quot;+119797979736\&quot; | [optional] 
**source** | **str** | data source | [optional] 

## Example

```python
from dataforseo_client.models.business_data_contact_info import BusinessDataContactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataContactInfo from a JSON string
business_data_contact_info_instance = BusinessDataContactInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataContactInfo.to_json()

# convert the object into a dict
business_data_contact_info_dict = business_data_contact_info_instance.to_dict()
# create an instance of BusinessDataContactInfo from a dict
business_data_contact_info_form_dict = business_data_contact_info.from_dict(business_data_contact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



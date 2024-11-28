# LocalServicesDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL of the Ad element in SERP | [optional] 
**domain** | **str** | domain where a link points | [optional] 
**items** | [**List[LocalServicesElement]**](LocalServicesElement.md) | elements of search results found in SERP | [optional] 

## Example

```python
from dataforseo_client.models.local_services_dataforseo_labs_serp_element_item import LocalServicesDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of LocalServicesDataforseoLabsSerpElementItem from a JSON string
local_services_dataforseo_labs_serp_element_item_instance = LocalServicesDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(LocalServicesDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
local_services_dataforseo_labs_serp_element_item_dict = local_services_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of LocalServicesDataforseoLabsSerpElementItem from a dict
local_services_dataforseo_labs_serp_element_item_from_dict = LocalServicesDataforseoLabsSerpElementItem.from_dict(local_services_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



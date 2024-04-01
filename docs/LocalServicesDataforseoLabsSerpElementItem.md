# LocalServicesDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
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
local_services_dataforseo_labs_serp_element_item_form_dict = local_services_dataforseo_labs_serp_element_item.from_dict(local_services_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



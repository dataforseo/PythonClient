# BaseSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 

## Example

```python
from dataforseo_client.models.base_serp_element_item import BaseSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSerpElementItem from a JSON string
base_serp_element_item_instance = BaseSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(BaseSerpElementItem.to_json())

# convert the object into a dict
base_serp_element_item_dict = base_serp_element_item_instance.to_dict()
# create an instance of BaseSerpElementItem from a dict
base_serp_element_item_from_dict = BaseSerpElementItem.from_dict(base_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



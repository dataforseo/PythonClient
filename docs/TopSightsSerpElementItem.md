# TopSightsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[TopSightsElement]**](TopSightsElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.top_sights_serp_element_item import TopSightsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of TopSightsSerpElementItem from a JSON string
top_sights_serp_element_item_instance = TopSightsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print TopSightsSerpElementItem.to_json()

# convert the object into a dict
top_sights_serp_element_item_dict = top_sights_serp_element_item_instance.to_dict()
# create an instance of TopSightsSerpElementItem from a dict
top_sights_serp_element_item_form_dict = top_sights_serp_element_item.from_dict(top_sights_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



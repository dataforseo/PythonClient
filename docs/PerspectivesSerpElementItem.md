# PerspectivesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[PerspectivesElement]**](PerspectivesElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.perspectives_serp_element_item import PerspectivesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PerspectivesSerpElementItem from a JSON string
perspectives_serp_element_item_instance = PerspectivesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print PerspectivesSerpElementItem.to_json()

# convert the object into a dict
perspectives_serp_element_item_dict = perspectives_serp_element_item_instance.to_dict()
# create an instance of PerspectivesSerpElementItem from a dict
perspectives_serp_element_item_form_dict = perspectives_serp_element_item.from_dict(perspectives_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



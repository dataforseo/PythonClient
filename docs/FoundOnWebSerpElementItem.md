# FoundOnWebSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**related_searches** | **List[Optional[str]]** | search queries related to the elment | [optional] 
**items** | [**List[FoundOnWebElement]**](FoundOnWebElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.found_on_web_serp_element_item import FoundOnWebSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of FoundOnWebSerpElementItem from a JSON string
found_on_web_serp_element_item_instance = FoundOnWebSerpElementItem.from_json(json)
# print the JSON string representation of the object
print FoundOnWebSerpElementItem.to_json()

# convert the object into a dict
found_on_web_serp_element_item_dict = found_on_web_serp_element_item_instance.to_dict()
# create an instance of FoundOnWebSerpElementItem from a dict
found_on_web_serp_element_item_form_dict = found_on_web_serp_element_item.from_dict(found_on_web_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



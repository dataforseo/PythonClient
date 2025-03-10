# VisualStoriesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**items** | [**List[LicensesElement]**](LicensesElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.visual_stories_serp_element_item import VisualStoriesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of VisualStoriesSerpElementItem from a JSON string
visual_stories_serp_element_item_instance = VisualStoriesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(VisualStoriesSerpElementItem.to_json())

# convert the object into a dict
visual_stories_serp_element_item_dict = visual_stories_serp_element_item_instance.to_dict()
# create an instance of VisualStoriesSerpElementItem from a dict
visual_stories_serp_element_item_from_dict = VisualStoriesSerpElementItem.from_dict(visual_stories_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



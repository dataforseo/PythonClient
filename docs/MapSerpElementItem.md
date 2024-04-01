# MapSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values; positions of elements with different type values are omitted from rank_group; always equals 0 for desktop | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP always equals 0 for desktop | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**url** | **str** | source URL | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.map_serp_element_item import MapSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MapSerpElementItem from a JSON string
map_serp_element_item_instance = MapSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(MapSerpElementItem.to_json())

# convert the object into a dict
map_serp_element_item_dict = map_serp_element_item_instance.to_dict()
# create an instance of MapSerpElementItem from a dict
map_serp_element_item_form_dict = map_serp_element_item.from_dict(map_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



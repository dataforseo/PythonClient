# MapSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
print MapSerpElementItem.to_json()

# convert the object into a dict
map_serp_element_item_dict = map_serp_element_item_instance.to_dict()
# create an instance of MapSerpElementItem from a dict
map_serp_element_item_form_dict = map_serp_element_item.from_dict(map_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



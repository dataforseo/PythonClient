# GraphItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** | date and time of the value readout in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2025-02-10 09:40:00 +00:00 | [optional] 
**value** | **float** | point value on graph | [optional] 
**volume** | **float** | volume value on graph | [optional] 

## Example

```python
from dataforseo_client.models.graph_items import GraphItems

# TODO update the JSON string below
json = "{}"
# create an instance of GraphItems from a JSON string
graph_items_instance = GraphItems.from_json(json)
# print the JSON string representation of the object
print(GraphItems.to_json())

# convert the object into a dict
graph_items_dict = graph_items_instance.to_dict()
# create an instance of GraphItems from a dict
graph_items_from_dict = GraphItems.from_dict(graph_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



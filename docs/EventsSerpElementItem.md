# EventsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**url** | **str** | source URL | [optional] 
**items** | [**List[EventsElement]**](EventsElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.events_serp_element_item import EventsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of EventsSerpElementItem from a JSON string
events_serp_element_item_instance = EventsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print EventsSerpElementItem.to_json()

# convert the object into a dict
events_serp_element_item_dict = events_serp_element_item_instance.to_dict()
# create an instance of EventsSerpElementItem from a dict
events_serp_element_item_form_dict = events_serp_element_item.from_dict(events_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# EventsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**snippet** | **str** | text alongside the link title | [optional] 
**url** | **str** | URL | [optional] 

## Example

```python
from dataforseo_client.models.events_element import EventsElement

# TODO update the JSON string below
json = "{}"
# create an instance of EventsElement from a JSON string
events_element_instance = EventsElement.from_json(json)
# print the JSON string representation of the object
print(EventsElement.to_json())

# convert the object into a dict
events_element_dict = events_element_instance.to_dict()
# create an instance of EventsElement from a dict
events_element_from_dict = EventsElement.from_dict(events_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



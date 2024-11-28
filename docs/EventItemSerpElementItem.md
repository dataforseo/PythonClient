# EventItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the element | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**url** | **str** | search URL with refinement parameters | [optional] 
**image_url** | **str** | URL of the image featured in the element | [optional] 
**event_dates** | [**EventDates**](EventDates.md) |  | [optional] 
**location_info** | [**LocationInfo**](LocationInfo.md) |  | [optional] 
**information_and_tickets** | [**List[InformationAndTicketsElement]**](InformationAndTicketsElement.md) | additional information and ticket purchase options | [optional] 

## Example

```python
from dataforseo_client.models.event_item_serp_element_item import EventItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of EventItemSerpElementItem from a JSON string
event_item_serp_element_item_instance = EventItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(EventItemSerpElementItem.to_json())

# convert the object into a dict
event_item_serp_element_item_dict = event_item_serp_element_item_instance.to_dict()
# create an instance of EventItemSerpElementItem from a dict
event_item_serp_element_item_from_dict = EventItemSerpElementItem.from_dict(event_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



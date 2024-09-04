# KnowledgeGraphHotelsBookingItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of a given link element | [optional] 
**date_from** | **str** | starting date of stay in the format “year-month-date” example: 2019-11-15 | [optional] 
**date_to** | **str** | ending date of stay in the format “year-month-date” example: 2019-11-17 | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: kc:/local:hotel booking | [optional] 
**items** | [**List[KnowledgeGraphHotelsBookingElement]**](KnowledgeGraphHotelsBookingElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_hotels_booking_item_serp_element_item import KnowledgeGraphHotelsBookingItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphHotelsBookingItemSerpElementItem from a JSON string
knowledge_graph_hotels_booking_item_serp_element_item_instance = KnowledgeGraphHotelsBookingItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphHotelsBookingItemSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_hotels_booking_item_serp_element_item_dict = knowledge_graph_hotels_booking_item_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphHotelsBookingItemSerpElementItem from a dict
knowledge_graph_hotels_booking_item_serp_element_item_form_dict = knowledge_graph_hotels_booking_item_serp_element_item.from_dict(knowledge_graph_hotels_booking_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



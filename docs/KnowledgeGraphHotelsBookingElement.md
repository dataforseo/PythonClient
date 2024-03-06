[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# KnowledgeGraphHotelsBookingElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**source** | **str** | source of the element indicates the source of information included in the shopping_element | [optional]
**description** | **str** | the description of the results element in SERP | [optional]
**url** | **str** | URL | [optional]
**domain** | **str** | domain in the URL | [optional]
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional]
**is_paid** | **bool** | indicates whether the element is an ad | [optional]

## Example

```python
from dataforseo_client.models.knowledge_graph_hotels_booking_element import KnowledgeGraphHotelsBookingElement

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphHotelsBookingElement from a JSON string
knowledge_graph_hotels_booking_element_instance = KnowledgeGraphHotelsBookingElement.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphHotelsBookingElement.to_json()

# convert the object into a dict
knowledge_graph_hotels_booking_element_dict = knowledge_graph_hotels_booking_element_instance.to_dict()
# create an instance of KnowledgeGraphHotelsBookingElement from a dict
knowledge_graph_hotels_booking_element_form_dict = knowledge_graph_hotels_booking_element.from_dict(knowledge_graph_hotels_booking_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
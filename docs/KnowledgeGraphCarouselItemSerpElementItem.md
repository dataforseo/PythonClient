# KnowledgeGraphCarouselItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: action:listen_artist | [optional] 
**link** | [**LinkElement**](LinkElement.md) |  | [optional] 
**items** | [**List[KnowledgeGraphListElement]**](KnowledgeGraphListElement.md) | elements of search results found in SERP | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_carousel_item_serp_element_item import KnowledgeGraphCarouselItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphCarouselItemSerpElementItem from a JSON string
knowledge_graph_carousel_item_serp_element_item_instance = KnowledgeGraphCarouselItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphCarouselItemSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_carousel_item_serp_element_item_dict = knowledge_graph_carousel_item_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphCarouselItemSerpElementItem from a dict
knowledge_graph_carousel_item_serp_element_item_from_dict = KnowledgeGraphCarouselItemSerpElementItem.from_dict(knowledge_graph_carousel_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



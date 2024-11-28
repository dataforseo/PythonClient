# KnowledgeGraphListItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the link element | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: ss:/webfacts:net_worth | [optional] 
**link** | [**LinkElement**](LinkElement.md) |  | [optional] 
**items** | [**List[KnowledgeGraphListElement]**](KnowledgeGraphListElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_list_item_serp_element_item import KnowledgeGraphListItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphListItemSerpElementItem from a JSON string
knowledge_graph_list_item_serp_element_item_instance = KnowledgeGraphListItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphListItemSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_list_item_serp_element_item_dict = knowledge_graph_list_item_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphListItemSerpElementItem from a dict
knowledge_graph_list_item_serp_element_item_from_dict = KnowledgeGraphListItemSerpElementItem.from_dict(knowledge_graph_list_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



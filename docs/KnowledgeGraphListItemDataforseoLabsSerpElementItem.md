# KnowledgeGraphListItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the element | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: kc:/local:place qa | [optional] 
**link** | [**LinkElement**](LinkElement.md) |  | [optional] 
**items** | [**List[KnowledgeGraphListElement]**](KnowledgeGraphListElement.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_list_item_dataforseo_labs_serp_element_item import KnowledgeGraphListItemDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphListItemDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_list_item_dataforseo_labs_serp_element_item_instance = KnowledgeGraphListItemDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphListItemDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_list_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_list_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphListItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_list_item_dataforseo_labs_serp_element_item_from_dict = KnowledgeGraphListItemDataforseoLabsSerpElementItem.from_dict(knowledge_graph_list_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



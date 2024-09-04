# KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of a given link element | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: kc:/local:place qa | [optional] 
**expanded_element** | [**List[KnowledgeGraphExpandedElement]**](KnowledgeGraphExpandedElement.md) | expanded element | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_expanded_item_dataforseo_labs_serp_element_item import KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_expanded_item_dataforseo_labs_serp_element_item_instance = KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_expanded_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_expanded_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_expanded_item_dataforseo_labs_serp_element_item_form_dict = knowledge_graph_expanded_item_dataforseo_labs_serp_element_item.from_dict(knowledge_graph_expanded_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



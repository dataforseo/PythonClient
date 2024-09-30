# KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: action:listen_artist | [optional] 
**items** | [**List[KnowledgeGraphShoppingElement]**](KnowledgeGraphShoppingElement.md) | elements of search results found in SERP | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_shopping_item_dataforseo_labs_serp_element_item import KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_shopping_item_dataforseo_labs_serp_element_item_instance = KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_shopping_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_shopping_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_shopping_item_dataforseo_labs_serp_element_item_form_dict = knowledge_graph_shopping_item_dataforseo_labs_serp_element_item.from_dict(knowledge_graph_shopping_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



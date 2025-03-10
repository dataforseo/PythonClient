# KnowledgeGraphShoppingItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the place | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: kc:/shopping/gpc:organic-offers | [optional] 
**items** | [**List[KnowledgeGraphShoppingElement]**](KnowledgeGraphShoppingElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_shopping_item_serp_element_item import KnowledgeGraphShoppingItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphShoppingItemSerpElementItem from a JSON string
knowledge_graph_shopping_item_serp_element_item_instance = KnowledgeGraphShoppingItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphShoppingItemSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_shopping_item_serp_element_item_dict = knowledge_graph_shopping_item_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphShoppingItemSerpElementItem from a dict
knowledge_graph_shopping_item_serp_element_item_from_dict = KnowledgeGraphShoppingItemSerpElementItem.from_dict(knowledge_graph_shopping_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



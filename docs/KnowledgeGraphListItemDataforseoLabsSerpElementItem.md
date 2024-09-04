# KnowledgeGraphListItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of a given link element | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: kc:/common/topic:social media presence | [optional] 
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
print KnowledgeGraphListItemDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_list_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_list_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphListItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_list_item_dataforseo_labs_serp_element_item_form_dict = knowledge_graph_list_item_dataforseo_labs_serp_element_item.from_dict(knowledge_graph_list_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# KnowledgeGraphPartItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the element | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: kc:/shopping/gpc:organic-offers | [optional] 
**text** | **str** | description content | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | link of the element | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_part_item_dataforseo_labs_serp_element_item import KnowledgeGraphPartItemDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphPartItemDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_part_item_dataforseo_labs_serp_element_item_instance = KnowledgeGraphPartItemDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphPartItemDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_part_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_part_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphPartItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_part_item_dataforseo_labs_serp_element_item_from_dict = KnowledgeGraphPartItemDataforseoLabsSerpElementItem.from_dict(knowledge_graph_part_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



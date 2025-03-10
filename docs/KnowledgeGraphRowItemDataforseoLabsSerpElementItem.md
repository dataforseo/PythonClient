# KnowledgeGraphRowItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: ss:/webfacts:net_worth | [optional] 
**text** | **str** | row content | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_row_item_dataforseo_labs_serp_element_item import KnowledgeGraphRowItemDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphRowItemDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_row_item_dataforseo_labs_serp_element_item_instance = KnowledgeGraphRowItemDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphRowItemDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_row_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_row_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphRowItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_row_item_dataforseo_labs_serp_element_item_from_dict = KnowledgeGraphRowItemDataforseoLabsSerpElementItem.from_dict(knowledge_graph_row_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



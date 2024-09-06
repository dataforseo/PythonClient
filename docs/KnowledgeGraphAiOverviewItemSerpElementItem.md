# KnowledgeGraphAiOverviewItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asynchronous_ai_overview** | **bool** | indicates whether the element is loaded asynchronically if true, the ai_overview element is loaded asynchronically; if false, the ai_overview element is loaded from cache; | [optional] 
**items** | [**List[AiOverviewElement]**](AiOverviewElement.md) | additional items present in the element if there are none, equals null | [optional] 
**references** | [**List[AiOverviewReference]**](AiOverviewReference.md) | additional references relevant to the item includes references to webpages that may have been used to generate the ai_overview | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_ai_overview_item_serp_element_item import KnowledgeGraphAiOverviewItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphAiOverviewItemSerpElementItem from a JSON string
knowledge_graph_ai_overview_item_serp_element_item_instance = KnowledgeGraphAiOverviewItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphAiOverviewItemSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_ai_overview_item_serp_element_item_dict = knowledge_graph_ai_overview_item_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphAiOverviewItemSerpElementItem from a dict
knowledge_graph_ai_overview_item_serp_element_item_form_dict = knowledge_graph_ai_overview_item_serp_element_item.from_dict(knowledge_graph_ai_overview_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# KnowledgeGraphPartItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: kc:/local:place qa | [optional] 
**text** | **str** | reference text text snippet from the page that was used to generate the ai_overview_element | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_part_item_serp_element_item import KnowledgeGraphPartItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphPartItemSerpElementItem from a JSON string
knowledge_graph_part_item_serp_element_item_instance = KnowledgeGraphPartItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphPartItemSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_part_item_serp_element_item_dict = knowledge_graph_part_item_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphPartItemSerpElementItem from a dict
knowledge_graph_part_item_serp_element_item_form_dict = knowledge_graph_part_item_serp_element_item.from_dict(knowledge_graph_part_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



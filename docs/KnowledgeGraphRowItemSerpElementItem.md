# KnowledgeGraphRowItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the item | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: kc:/common/topic:social media presence | [optional] 
**text** | **str** | reference text text snippet from the page that was used to generate the ai_overview_element | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | links featured in the faq_box_element | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_row_item_serp_element_item import KnowledgeGraphRowItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphRowItemSerpElementItem from a JSON string
knowledge_graph_row_item_serp_element_item_instance = KnowledgeGraphRowItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphRowItemSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_row_item_serp_element_item_dict = knowledge_graph_row_item_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphRowItemSerpElementItem from a dict
knowledge_graph_row_item_serp_element_item_from_dict = KnowledgeGraphRowItemSerpElementItem.from_dict(knowledge_graph_row_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



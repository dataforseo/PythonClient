# KnowledgeGraphPartItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: kc:/local:place qa | [optional] 
**text** | **str** | content within the item | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | link of the element | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_part_item_dataforseo_labs_serp_element_item import KnowledgeGraphPartItemDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphPartItemDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_part_item_dataforseo_labs_serp_element_item_instance = KnowledgeGraphPartItemDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphPartItemDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_part_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_part_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphPartItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_part_item_dataforseo_labs_serp_element_item_form_dict = knowledge_graph_part_item_dataforseo_labs_serp_element_item.from_dict(knowledge_graph_part_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



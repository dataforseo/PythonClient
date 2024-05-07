# KnowledgeGraphDescriptionItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**text** | **str** | description content | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_description_item_serp_element_item import KnowledgeGraphDescriptionItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphDescriptionItemSerpElementItem from a JSON string
knowledge_graph_description_item_serp_element_item_instance = KnowledgeGraphDescriptionItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphDescriptionItemSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_description_item_serp_element_item_dict = knowledge_graph_description_item_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphDescriptionItemSerpElementItem from a dict
knowledge_graph_description_item_serp_element_item_form_dict = knowledge_graph_description_item_serp_element_item.from_dict(knowledge_graph_description_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



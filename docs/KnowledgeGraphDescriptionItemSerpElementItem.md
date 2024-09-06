# KnowledgeGraphDescriptionItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | text or description of the element in SERP | [optional] 
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



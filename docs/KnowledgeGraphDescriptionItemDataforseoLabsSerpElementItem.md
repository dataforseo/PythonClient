# KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | description content | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_description_item_dataforseo_labs_serp_element_item import KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_description_item_dataforseo_labs_serp_element_item_instance = KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_description_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_description_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_description_item_dataforseo_labs_serp_element_item_from_dict = KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem.from_dict(knowledge_graph_description_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



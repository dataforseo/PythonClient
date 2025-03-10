# KnowledgeGraphImagesItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**link** | [**LinkElement**](LinkElement.md) |  | [optional] 
**items** | [**List[KnowledgeGraphImagesElement]**](KnowledgeGraphImagesElement.md) | items featured in the faq_box | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_images_item_serp_element_item import KnowledgeGraphImagesItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphImagesItemSerpElementItem from a JSON string
knowledge_graph_images_item_serp_element_item_instance = KnowledgeGraphImagesItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphImagesItemSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_images_item_serp_element_item_dict = knowledge_graph_images_item_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphImagesItemSerpElementItem from a dict
knowledge_graph_images_item_serp_element_item_from_dict = KnowledgeGraphImagesItemSerpElementItem.from_dict(knowledge_graph_images_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



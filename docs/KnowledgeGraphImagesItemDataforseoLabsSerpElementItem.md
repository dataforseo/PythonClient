# KnowledgeGraphImagesItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | [**LinkElement**](LinkElement.md) |  | [optional] 
**items** | [**List[KnowledgeGraphImagesElement]**](KnowledgeGraphImagesElement.md) | contains results featured in the ‘hotels_pack’ element of SERP | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_images_item_dataforseo_labs_serp_element_item import KnowledgeGraphImagesItemDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphImagesItemDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_images_item_dataforseo_labs_serp_element_item_instance = KnowledgeGraphImagesItemDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphImagesItemDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_images_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_images_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphImagesItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_images_item_dataforseo_labs_serp_element_item_from_dict = KnowledgeGraphImagesItemDataforseoLabsSerpElementItem.from_dict(knowledge_graph_images_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



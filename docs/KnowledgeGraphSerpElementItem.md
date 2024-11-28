# KnowledgeGraphSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**subtitle** | **str** | subtitle of the item | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**card_id** | **str** | card id | [optional] 
**url** | **str** | relevant URL in SERP | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 
**logo_url** | **str** | URL of the logo from knowledge graph | [optional] 
**cid** | **str** | google-defined client id unique id of a local establishment; can be used with Google Reviews API to get a full list of reviews | [optional] 
**items** | [**List[BaseSerpElementItem]**](BaseSerpElementItem.md) | contains results featured in the ‘hotels_pack’ element of SERP | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_serp_element_item import KnowledgeGraphSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphSerpElementItem from a JSON string
knowledge_graph_serp_element_item_instance = KnowledgeGraphSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphSerpElementItem.to_json())

# convert the object into a dict
knowledge_graph_serp_element_item_dict = knowledge_graph_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphSerpElementItem from a dict
knowledge_graph_serp_element_item_from_dict = KnowledgeGraphSerpElementItem.from_dict(knowledge_graph_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



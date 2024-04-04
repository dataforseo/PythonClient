# KnowledgeGraphListElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | link anchor text | [optional] 
**subtitle** | **str** | subtitle of the item | [optional] 
**url** | **str** | sitelink URL | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_list_element import KnowledgeGraphListElement

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphListElement from a JSON string
knowledge_graph_list_element_instance = KnowledgeGraphListElement.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphListElement.to_json()

# convert the object into a dict
knowledge_graph_list_element_dict = knowledge_graph_list_element_instance.to_dict()
# create an instance of KnowledgeGraphListElement from a dict
knowledge_graph_list_element_form_dict = knowledge_graph_list_element.from_dict(knowledge_graph_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



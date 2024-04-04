# KnowledgeGraphExpandedElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**featured_title** | **str** | title of a given element | [optional] 
**url** | **str** | relevant URL | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**snippet** | **str** | text alongside the link title | [optional] 
**images** | [**List[ImagesElement]**](ImagesElement.md) | images of the element | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**table** | [**Table**](Table.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_expanded_element import KnowledgeGraphExpandedElement

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphExpandedElement from a JSON string
knowledge_graph_expanded_element_instance = KnowledgeGraphExpandedElement.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphExpandedElement.to_json()

# convert the object into a dict
knowledge_graph_expanded_element_dict = knowledge_graph_expanded_element_instance.to_dict()
# create an instance of KnowledgeGraphExpandedElement from a dict
knowledge_graph_expanded_element_form_dict = knowledge_graph_expanded_element.from_dict(knowledge_graph_expanded_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



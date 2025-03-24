# KnowledgeGraphLinkElementInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | sitelink URL | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**snippet** | **str** | text alongside the link title | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_link_element_info import KnowledgeGraphLinkElementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphLinkElementInfo from a JSON string
knowledge_graph_link_element_info_instance = KnowledgeGraphLinkElementInfo.from_json(json)
# print the JSON string representation of the object
print(KnowledgeGraphLinkElementInfo.to_json())

# convert the object into a dict
knowledge_graph_link_element_info_dict = knowledge_graph_link_element_info_instance.to_dict()
# create an instance of KnowledgeGraphLinkElementInfo from a dict
knowledge_graph_link_element_info_from_dict = KnowledgeGraphLinkElementInfo.from_dict(knowledge_graph_link_element_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



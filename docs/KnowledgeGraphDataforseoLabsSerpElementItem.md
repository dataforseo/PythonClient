# KnowledgeGraphDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**sub_title** | **str** | subtitle of the item | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**card_id** | **str** | card id | [optional] 
**url** | **str** | relevant URL in SERP | [optional] 
**image_url** | **str** | URL of the image from knowledge graph | [optional] 
**logo_url** | **str** | URL of the logo from knowledge graph | [optional] 
**cid** | **str** | google-defined client id | [optional] 
**items** | [**List[PeopleAlsoAskElement]**](PeopleAlsoAskElement.md) | elements of search results found in SERP | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_dataforseo_labs_serp_element_item import KnowledgeGraphDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_dataforseo_labs_serp_element_item_instance = KnowledgeGraphDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_dataforseo_labs_serp_element_item_dict = knowledge_graph_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphDataforseoLabsSerpElementItem from a dict
knowledge_graph_dataforseo_labs_serp_element_item_form_dict = knowledge_graph_dataforseo_labs_serp_element_item.from_dict(knowledge_graph_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



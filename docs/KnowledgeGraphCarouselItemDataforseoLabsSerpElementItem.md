# KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**data_attrid** | **str** | google defined data attribute ID example: ss:/webfacts:net_worth | [optional] 
**link** | [**LinkElement**](LinkElement.md) |  | [optional] 
**items** | [**List[KnowledgeGraphListElement]**](KnowledgeGraphListElement.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.knowledge_graph_carousel_item_dataforseo_labs_serp_element_item import KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem from a JSON string
knowledge_graph_carousel_item_dataforseo_labs_serp_element_item_instance = KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_carousel_item_dataforseo_labs_serp_element_item_dict = knowledge_graph_carousel_item_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem from a dict
knowledge_graph_carousel_item_dataforseo_labs_serp_element_item_form_dict = knowledge_graph_carousel_item_dataforseo_labs_serp_element_item.from_dict(knowledge_graph_carousel_item_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



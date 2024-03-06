[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# KnowledgeGraphSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**title** | **str** | title of the result in SERP | [optional]
**subtitle** | **str** | subtitle of the item | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**card_id** | **str** | card id | [optional]
**url** | **str** | relevant URL in SERP | [optional]
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional]
**logo_url** | **str** | URL of the logo from knowledge graph | [optional]
**cid** | **str** | google-defined client id unique id of a local establishment; can be used with Google Reviews API to get a full list of reviews | [optional]
**items** | [**List[BaseSerpElementItem]**](BaseSerpElementItem.md) | additional items present in the element if there are none, equals null | [optional]
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional]

## Example

```python
from dataforseo_client.models.knowledge_graph_serp_element_item import KnowledgeGraphSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphSerpElementItem from a JSON string
knowledge_graph_serp_element_item_instance = KnowledgeGraphSerpElementItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphSerpElementItem.to_json()

# convert the object into a dict
knowledge_graph_serp_element_item_dict = knowledge_graph_serp_element_item_instance.to_dict()
# create an instance of KnowledgeGraphSerpElementItem from a dict
knowledge_graph_serp_element_item_form_dict = knowledge_graph_serp_element_item.from_dict(knowledge_graph_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
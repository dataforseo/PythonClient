[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# KnowledgeGraphShoppingElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the result in SERP | [optional]
**url** | **str** | relevant URL | [optional]
**domain** | **str** | website domain | [optional]
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional]
**source** | **str** | source of additional information about the result | [optional]
**snippet** | **str** | text alongside the link title | [optional]
**marketplace** | **str** | merchant account provider ecommerce site that hosts products or websites of individual sellers under the same merchant account example: by Google | [optional]
**marketplace_url** | **str** | URL to the merchant account provider ecommerce site that hosts products or websites of individual sellers under the same merchant account | [optional]

## Example

```python
from dataforseo_client.models.knowledge_graph_shopping_element import KnowledgeGraphShoppingElement

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphShoppingElement from a JSON string
knowledge_graph_shopping_element_instance = KnowledgeGraphShoppingElement.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphShoppingElement.to_json()

# convert the object into a dict
knowledge_graph_shopping_element_dict = knowledge_graph_shopping_element_instance.to_dict()
# create an instance of KnowledgeGraphShoppingElement from a dict
knowledge_graph_shopping_element_form_dict = knowledge_graph_shopping_element.from_dict(knowledge_graph_shopping_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
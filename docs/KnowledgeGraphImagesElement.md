[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# KnowledgeGraphImagesElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**url** | **str** | relevant URL in SERP | [optional]
**domain** | **str** | domain in SERP of the Ad element | [optional]
**alt** | **str** | alt tag of the image | [optional]
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional]
**xpath** | **str** | the XPath of the element | [optional]

## Example

```python
from dataforseo_client.models.knowledge_graph_images_element import KnowledgeGraphImagesElement

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeGraphImagesElement from a JSON string
knowledge_graph_images_element_instance = KnowledgeGraphImagesElement.from_json(json)
# print the JSON string representation of the object
print KnowledgeGraphImagesElement.to_json()

# convert the object into a dict
knowledge_graph_images_element_dict = knowledge_graph_images_element_instance.to_dict()
# create an instance of KnowledgeGraphImagesElement from a dict
knowledge_graph_images_element_form_dict = knowledge_graph_images_element.from_dict(knowledge_graph_images_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
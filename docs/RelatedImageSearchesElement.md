[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# RelatedImageSearchesElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the carousel item | [optional]
**alt** | **str** | alt tag of the image | [optional]
**url** | **str** | source URL | [optional]
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional]

## Example

```python
from dataforseo_client.models.related_image_searches_element import RelatedImageSearchesElement

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedImageSearchesElement from a JSON string
related_image_searches_element_instance = RelatedImageSearchesElement.from_json(json)
# print the JSON string representation of the object
print RelatedImageSearchesElement.to_json()

# convert the object into a dict
related_image_searches_element_dict = related_image_searches_element_instance.to_dict()
# create an instance of RelatedImageSearchesElement from a dict
related_image_searches_element_form_dict = related_image_searches_element.from_dict(related_image_searches_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
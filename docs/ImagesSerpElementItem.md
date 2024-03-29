[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ImagesSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**title** | **str** | title of a given link element | [optional]
**url** | **str** | URL | [optional]
**items** | [**List[ImagesElement]**](ImagesElement.md) | contains results featured in the ‘hotels_pack’ element of SERP | [optional]
**related_image_searches** | [**List[RelatedImageSearchesElement]**](RelatedImageSearchesElement.md) | contains keywords and images related to the specified search term if there are none, equals null | [optional]
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional]

## Example

```python
from dataforseo_client.models.images_serp_element_item import ImagesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesSerpElementItem from a JSON string
images_serp_element_item_instance = ImagesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print ImagesSerpElementItem.to_json()

# convert the object into a dict
images_serp_element_item_dict = images_serp_element_item_instance.to_dict()
# create an instance of ImagesSerpElementItem from a dict
images_serp_element_item_form_dict = images_serp_element_item.from_dict(images_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
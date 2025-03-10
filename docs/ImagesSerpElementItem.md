# ImagesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**url** | **str** | source URL | [optional] 
**items** | [**List[ImagesElement]**](ImagesElement.md) | contains arrays of specific images | [optional] 
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
print(ImagesSerpElementItem.to_json())

# convert the object into a dict
images_serp_element_item_dict = images_serp_element_item_instance.to_dict()
# create an instance of ImagesSerpElementItem from a dict
images_serp_element_item_from_dict = ImagesSerpElementItem.from_dict(images_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



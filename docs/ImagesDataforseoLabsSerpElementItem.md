# ImagesDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL | [optional] 
**items** | [**List[ImagesElement]**](ImagesElement.md) | additional items present in the element if there are none, equals null | [optional] 
**related_image_searches** | [**RelatedImageSearchesElement**](RelatedImageSearchesElement.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.images_dataforseo_labs_serp_element_item import ImagesDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesDataforseoLabsSerpElementItem from a JSON string
images_dataforseo_labs_serp_element_item_instance = ImagesDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(ImagesDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
images_dataforseo_labs_serp_element_item_dict = images_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of ImagesDataforseoLabsSerpElementItem from a dict
images_dataforseo_labs_serp_element_item_from_dict = ImagesDataforseoLabsSerpElementItem.from_dict(images_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



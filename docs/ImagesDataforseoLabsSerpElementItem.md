# ImagesDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL of the Ad element in SERP | [optional] 
**items** | [**List[ImagesElement]**](ImagesElement.md) | elements of search results found in SERP | [optional] 
**related_image_searches** | [**List[RelatedImageSearchesElement]**](RelatedImageSearchesElement.md) | contains keywords and images related to the specified search term if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.images_dataforseo_labs_serp_element_item import ImagesDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesDataforseoLabsSerpElementItem from a JSON string
images_dataforseo_labs_serp_element_item_instance = ImagesDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print ImagesDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
images_dataforseo_labs_serp_element_item_dict = images_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of ImagesDataforseoLabsSerpElementItem from a dict
images_dataforseo_labs_serp_element_item_form_dict = images_dataforseo_labs_serp_element_item.from_dict(images_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



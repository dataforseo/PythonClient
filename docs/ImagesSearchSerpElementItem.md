# ImagesSearchSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP for the target domain absolute position among all the elements in SERP | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**subtitle** | **str** | subtitle of the result in SERP | [optional] 
**alt** | **str** | the alt tag of the image | [optional] 
**url** | **str** | the URL of the page where the image is hosted | [optional] 
**source_url** | **str** | the URL of the source image | [optional] 
**encoded_url** | **str** | the URL of the cached version of the image stored on Google’s servers | [optional] 

## Example

```python
from dataforseo_client.models.images_search_serp_element_item import ImagesSearchSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesSearchSerpElementItem from a JSON string
images_search_serp_element_item_instance = ImagesSearchSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(ImagesSearchSerpElementItem.to_json())

# convert the object into a dict
images_search_serp_element_item_dict = images_search_serp_element_item_instance.to_dict()
# create an instance of ImagesSearchSerpElementItem from a dict
images_search_serp_element_item_form_dict = images_search_serp_element_item.from_dict(images_search_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



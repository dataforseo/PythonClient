# ImagesElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**alt** | **str** | alt tag of the image | [optional] 
**url** | **str** | URL link | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 

## Example

```python
from dataforseo_client.models.images_element import ImagesElement

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesElement from a JSON string
images_element_instance = ImagesElement.from_json(json)
# print the JSON string representation of the object
print(ImagesElement.to_json())

# convert the object into a dict
images_element_dict = images_element_instance.to_dict()
# create an instance of ImagesElement from a dict
images_element_from_dict = ImagesElement.from_dict(images_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



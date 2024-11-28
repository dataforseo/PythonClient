# PreviewImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | search URL with refinement parameters | [optional] 
**height** | **int** | height of the preview image | [optional] 
**width** | **int** | width of the preview image | [optional] 

## Example

```python
from dataforseo_client.models.preview_image import PreviewImage

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewImage from a JSON string
preview_image_instance = PreviewImage.from_json(json)
# print the JSON string representation of the object
print(PreviewImage.to_json())

# convert the object into a dict
preview_image_dict = preview_image_instance.to_dict()
# create an instance of PreviewImage from a dict
preview_image_from_dict = PreviewImage.from_dict(preview_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



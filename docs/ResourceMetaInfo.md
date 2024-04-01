# ResourceMetaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternative_text** | **str** | content of the image alt attribute the value depends on the resource_type | [optional] 
**title** | **str** | title | [optional] 
**original_width** | **int** | original image width in px | [optional] 
**original_height** | **int** | original image height in px | [optional] 
**width** | **int** | image width in px | [optional] 
**height** | **int** | image height in px | [optional] 

## Example

```python
from dataforseo_client.models.resource_meta_info import ResourceMetaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceMetaInfo from a JSON string
resource_meta_info_instance = ResourceMetaInfo.from_json(json)
# print the JSON string representation of the object
print(ResourceMetaInfo.to_json())

# convert the object into a dict
resource_meta_info_dict = resource_meta_info_instance.to_dict()
# create an instance of ResourceMetaInfo from a dict
resource_meta_info_form_dict = resource_meta_info.from_dict(resource_meta_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



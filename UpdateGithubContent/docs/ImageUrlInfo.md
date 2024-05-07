# ImageUrlInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the image used in the review | [optional] 

## Example

```python
from dataforseo_client.models.image_url_info import ImageUrlInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImageUrlInfo from a JSON string
image_url_info_instance = ImageUrlInfo.from_json(json)
# print the JSON string representation of the object
print ImageUrlInfo.to_json()

# convert the object into a dict
image_url_info_dict = image_url_info_instance.to_dict()
# create an instance of ImageUrlInfo from a dict
image_url_info_form_dict = image_url_info.from_dict(image_url_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



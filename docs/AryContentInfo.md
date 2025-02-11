# AryContentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | content text | [optional] 
**url** | **str** | page URL displayed in case the text is a link anchor | [optional] 
**urls** | [**List[Urls]**](Urls.md) | contains other URLs and anchors found in the content element | [optional] 

## Example

```python
from dataforseo_client.models.ary_content_info import AryContentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AryContentInfo from a JSON string
ary_content_info_instance = AryContentInfo.from_json(json)
# print the JSON string representation of the object
print(AryContentInfo.to_json())

# convert the object into a dict
ary_content_info_dict = ary_content_info_instance.to_dict()
# create an instance of AryContentInfo from a dict
ary_content_info_from_dict = AryContentInfo.from_dict(ary_content_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



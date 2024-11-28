# ContentItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | content text | [optional] 
**url** | **str** | page URL displayed in case the text is a link anchor | [optional] 
**urls** | [**List[ContentUrlInfo]**](ContentUrlInfo.md) | contains other URLs and anchors found in the content element | [optional] 

## Example

```python
from dataforseo_client.models.content_item_info import ContentItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentItemInfo from a JSON string
content_item_info_instance = ContentItemInfo.from_json(json)
# print the JSON string representation of the object
print(ContentItemInfo.to_json())

# convert the object into a dict
content_item_info_dict = content_item_info_instance.to_dict()
# create an instance of ContentItemInfo from a dict
content_item_info_from_dict = ContentItemInfo.from_dict(content_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SectionContentItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | content text | [optional] 
**url** | **str** | page URL. displayed in case the text is a link anchor | [optional] 
**urls** | [**List[ContentUrlInfo]**](ContentUrlInfo.md) | contains other URLs and anchors found in the content element | [optional] 

## Example

```python
from dataforseo_client.models.section_content_item_info import SectionContentItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SectionContentItemInfo from a JSON string
section_content_item_info_instance = SectionContentItemInfo.from_json(json)
# print the JSON string representation of the object
print(SectionContentItemInfo.to_json())

# convert the object into a dict
section_content_item_info_dict = section_content_item_info_instance.to_dict()
# create an instance of SectionContentItemInfo from a dict
section_content_item_info_from_dict = SectionContentItemInfo.from_dict(section_content_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



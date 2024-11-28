# PageSectionContentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_content** | [**List[ContentItemInfo]**](ContentItemInfo.md) | primary content on the page you can find more information about content priority calculation in this help center article | [optional] 
**secondary_content** | [**List[ContentItemInfo]**](ContentItemInfo.md) | secondary content on the page you can find more information about content priority calculation in this help center article | [optional] 
**table_content** | [**List[TableContent]**](TableContent.md) | content of the table on the page | [optional] 

## Example

```python
from dataforseo_client.models.page_section_content_info import PageSectionContentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PageSectionContentInfo from a JSON string
page_section_content_info_instance = PageSectionContentInfo.from_json(json)
# print the JSON string representation of the object
print(PageSectionContentInfo.to_json())

# convert the object into a dict
page_section_content_info_dict = page_section_content_info_instance.to_dict()
# create an instance of PageSectionContentInfo from a dict
page_section_content_info_from_dict = PageSectionContentInfo.from_dict(page_section_content_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



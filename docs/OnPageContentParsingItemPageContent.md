# OnPageContentParsingItemPageContent

parsed content of the page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**PageSectionContentInfo**](PageSectionContentInfo.md) |  | [optional] 
**footer** | [**PageSectionContentInfo**](PageSectionContentInfo.md) |  | [optional] 
**main_topic** | [**List[TopicInfo]**](TopicInfo.md) | main topic on the page you can find more information about topic priority calculation in this help center article | [optional] 
**secondary_topic** | [**List[TopicInfo]**](TopicInfo.md) | secondary topic on the page you can find more information about topic priority calculation in this help center article | [optional] 

## Example

```python
from dataforseo_client.models.on_page_content_parsing_item_page_content import OnPageContentParsingItemPageContent

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageContentParsingItemPageContent from a JSON string
on_page_content_parsing_item_page_content_instance = OnPageContentParsingItemPageContent.from_json(json)
# print the JSON string representation of the object
print(OnPageContentParsingItemPageContent.to_json())

# convert the object into a dict
on_page_content_parsing_item_page_content_dict = on_page_content_parsing_item_page_content_instance.to_dict()
# create an instance of OnPageContentParsingItemPageContent from a dict
on_page_content_parsing_item_page_content_from_dict = OnPageContentParsingItemPageContent.from_dict(on_page_content_parsing_item_page_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



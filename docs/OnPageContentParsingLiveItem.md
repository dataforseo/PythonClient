# OnPageContentParsingLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**fetch_time** | **str** | date and time when the content was fethced example: \&quot;2022-11-01 10:02:52 +00:00\&quot; | [optional] 
**status_code** | **int** | status code of the page | [optional] 
**page_content** | [**PageContentInfo**](PageContentInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.on_page_content_parsing_live_item import OnPageContentParsingLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageContentParsingLiveItem from a JSON string
on_page_content_parsing_live_item_instance = OnPageContentParsingLiveItem.from_json(json)
# print the JSON string representation of the object
print(OnPageContentParsingLiveItem.to_json())

# convert the object into a dict
on_page_content_parsing_live_item_dict = on_page_content_parsing_live_item_instance.to_dict()
# create an instance of OnPageContentParsingLiveItem from a dict
on_page_content_parsing_live_item_from_dict = OnPageContentParsingLiveItem.from_dict(on_page_content_parsing_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



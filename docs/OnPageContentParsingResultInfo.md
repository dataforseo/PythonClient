# OnPageContentParsingResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional] 
**crawl_status** | [**CrawlStatusInfo**](CrawlStatusInfo.md) |  | [optional] 
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[OnPageContentParsingItem]**](OnPageContentParsingItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.on_page_content_parsing_result_info import OnPageContentParsingResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageContentParsingResultInfo from a JSON string
on_page_content_parsing_result_info_instance = OnPageContentParsingResultInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageContentParsingResultInfo.to_json())

# convert the object into a dict
on_page_content_parsing_result_info_dict = on_page_content_parsing_result_info_instance.to_dict()
# create an instance of OnPageContentParsingResultInfo from a dict
on_page_content_parsing_result_info_from_dict = OnPageContentParsingResultInfo.from_dict(on_page_content_parsing_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OnPageDuplicateTagsResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional] 
**crawl_status** | [**CrawlStatusInfo**](CrawlStatusInfo.md) |  | [optional] 
**total_pages_count** | **int** | total number of pages with duplicate tags displays the total number of pages with duplicate tags of the target website | [optional] 
**pages_count** | **int** | number of pages with duplicate tags in the response displays the number of pages with duplicate tags returned in the response | [optional] 
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[OnPageDuplicateTagsItem]**](OnPageDuplicateTagsItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.on_page_duplicate_tags_result_info import OnPageDuplicateTagsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageDuplicateTagsResultInfo from a JSON string
on_page_duplicate_tags_result_info_instance = OnPageDuplicateTagsResultInfo.from_json(json)
# print the JSON string representation of the object
print OnPageDuplicateTagsResultInfo.to_json()

# convert the object into a dict
on_page_duplicate_tags_result_info_dict = on_page_duplicate_tags_result_info_instance.to_dict()
# create an instance of OnPageDuplicateTagsResultInfo from a dict
on_page_duplicate_tags_result_info_form_dict = on_page_duplicate_tags_result_info.from_dict(on_page_duplicate_tags_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



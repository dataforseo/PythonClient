# OnPagePagesByResourceResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional] 
**crawl_status** | [**CrawlStatusInfo**](CrawlStatusInfo.md) |  | [optional] 
**total_items_count** | **int** | total number of relevant items in the database | [optional] 
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[BaseOnPageResourceItemInfo]**](BaseOnPageResourceItemInfo.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.on_page_pages_by_resource_result_info import OnPagePagesByResourceResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPagePagesByResourceResultInfo from a JSON string
on_page_pages_by_resource_result_info_instance = OnPagePagesByResourceResultInfo.from_json(json)
# print the JSON string representation of the object
print(OnPagePagesByResourceResultInfo.to_json())

# convert the object into a dict
on_page_pages_by_resource_result_info_dict = on_page_pages_by_resource_result_info_instance.to_dict()
# create an instance of OnPagePagesByResourceResultInfo from a dict
on_page_pages_by_resource_result_info_from_dict = OnPagePagesByResourceResultInfo.from_dict(on_page_pages_by_resource_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



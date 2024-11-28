# OnPageKeywordDensityResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional] 
**crawl_status** | [**CrawlStatusInfo**](CrawlStatusInfo.md) |  | [optional] 
**total_items_count** | **int** | total number of relevant items total number of keywords on the specified website or web page matching the set keyword_length and filters | [optional] 
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[OnPageKeywordDensityItem]**](OnPageKeywordDensityItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.on_page_keyword_density_result_info import OnPageKeywordDensityResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageKeywordDensityResultInfo from a JSON string
on_page_keyword_density_result_info_instance = OnPageKeywordDensityResultInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageKeywordDensityResultInfo.to_json())

# convert the object into a dict
on_page_keyword_density_result_info_dict = on_page_keyword_density_result_info_instance.to_dict()
# create an instance of OnPageKeywordDensityResultInfo from a dict
on_page_keyword_density_result_info_from_dict = OnPageKeywordDensityResultInfo.from_dict(on_page_keyword_density_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



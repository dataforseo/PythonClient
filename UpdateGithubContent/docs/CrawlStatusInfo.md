# CrawlStatusInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_crawl_pages** | **int** | maximum number of pages to crawl  indicates the max_crawl_pages limit you specified when setting a task | [optional] 
**pages_in_queue** | **int** | number of pages that are currently in the crawling queue | [optional] 
**pages_crawled** | **int** | number of crawled pages | [optional] 

## Example

```python
from dataforseo_client.models.crawl_status_info import CrawlStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlStatusInfo from a JSON string
crawl_status_info_instance = CrawlStatusInfo.from_json(json)
# print the JSON string representation of the object
print CrawlStatusInfo.to_json()

# convert the object into a dict
crawl_status_info_dict = crawl_status_info_instance.to_dict()
# create an instance of CrawlStatusInfo from a dict
crawl_status_info_form_dict = crawl_status_info.from_dict(crawl_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



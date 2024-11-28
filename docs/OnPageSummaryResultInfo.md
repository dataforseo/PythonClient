# OnPageSummaryResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional] 
**crawl_status** | [**CrawlStatusInfo**](CrawlStatusInfo.md) |  | [optional] 
**crawl_gateway_address** | **str** | crawler ip address displays the IP address used by the crawler to initiate the current crawling session you can find the full list of IPs used by our crawler in the Overview section | [optional] 
**crawl_stop_reason** | **str** | reason why the crawling stopped information about the reason why the crawling process stopped; possible values: limit_exceeded – the limit set in the max_crawl_pages was exceeded; empty_queue – all URLs in the queue were crawled; force_stopped – the crawling process was halted using the On Page API Force Stop function; unexpected_exception – an internal error was encountered while crawling the target, contact support for more info | [optional] 
**domain_info** | [**DomainInfo**](DomainInfo.md) |  | [optional] 
**page_metrics** | [**PageMetrics**](PageMetrics.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.on_page_summary_result_info import OnPageSummaryResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageSummaryResultInfo from a JSON string
on_page_summary_result_info_instance = OnPageSummaryResultInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageSummaryResultInfo.to_json())

# convert the object into a dict
on_page_summary_result_info_dict = on_page_summary_result_info_instance.to_dict()
# create an instance of OnPageSummaryResultInfo from a dict
on_page_summary_result_info_from_dict = OnPageSummaryResultInfo.from_dict(on_page_summary_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



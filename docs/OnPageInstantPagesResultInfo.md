# OnPageInstantPagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional] 
**crawl_status** | [**CrawlStatusInfo**](CrawlStatusInfo.md) |  | [optional] 
**crawl_gateway_address** | **str** | crawler ip address displays the IP address used by the crawler to initiate the current crawling session you can find the full list of IPs used by our crawler in the Overview section | [optional] 
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[BaseOnPageResourceItemInfo]**](BaseOnPageResourceItemInfo.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.on_page_instant_pages_result_info import OnPageInstantPagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageInstantPagesResultInfo from a JSON string
on_page_instant_pages_result_info_instance = OnPageInstantPagesResultInfo.from_json(json)
# print the JSON string representation of the object
print OnPageInstantPagesResultInfo.to_json()

# convert the object into a dict
on_page_instant_pages_result_info_dict = on_page_instant_pages_result_info_instance.to_dict()
# create an instance of OnPageInstantPagesResultInfo from a dict
on_page_instant_pages_result_info_form_dict = on_page_instant_pages_result_info.from_dict(on_page_instant_pages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



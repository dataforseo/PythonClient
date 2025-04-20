# BacklinksBulkPagesSummaryLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | **List[str]** | domains, subdomains or webpages to get summary data for required field a domain or a subdomain should be specified without https:// and www. a page should be specified with absolute URL (including http:// or https://) you can specify up to 1000 pages, domains, or subdomains in each request. note that the URLs you set in a single request cannot belong to more than 100 different domains. | [optional] 
**include_subdomains** | **bool** | indicates if the subdomains of the target will be included in the search optional field if set to false, the subdomains will be ignored default value: true | [optional] 
**rank_scale** | **str** | defines the scale used for calculating and displaying the rank, domain_from_rank, and page_from_rank values optional field you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale possible values: one_hundred — rank values are displayed on a 0–100 scale one_thousand — rank values are displayed on a 0–1000 scale default value: one_thousand learn more about how this parameter works and how ranking metrics are calculated in this Help Center article | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_bulk_pages_summary_live_request_info import BacklinksBulkPagesSummaryLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkPagesSummaryLiveRequestInfo from a JSON string
backlinks_bulk_pages_summary_live_request_info_instance = BacklinksBulkPagesSummaryLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksBulkPagesSummaryLiveRequestInfo.to_json())

# convert the object into a dict
backlinks_bulk_pages_summary_live_request_info_dict = backlinks_bulk_pages_summary_live_request_info_instance.to_dict()
# create an instance of BacklinksBulkPagesSummaryLiveRequestInfo from a dict
backlinks_bulk_pages_summary_live_request_info_from_dict = BacklinksBulkPagesSummaryLiveRequestInfo.from_dict(backlinks_bulk_pages_summary_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



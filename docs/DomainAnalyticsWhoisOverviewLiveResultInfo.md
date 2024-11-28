# DomainAnalyticsWhoisOverviewLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DomainAnalyticsWhoisOverviewLiveItem]**](DomainAnalyticsWhoisOverviewLiveItem.md) | contains ranking and traffic data | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_whois_overview_live_result_info import DomainAnalyticsWhoisOverviewLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsWhoisOverviewLiveResultInfo from a JSON string
domain_analytics_whois_overview_live_result_info_instance = DomainAnalyticsWhoisOverviewLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(DomainAnalyticsWhoisOverviewLiveResultInfo.to_json())

# convert the object into a dict
domain_analytics_whois_overview_live_result_info_dict = domain_analytics_whois_overview_live_result_info_instance.to_dict()
# create an instance of DomainAnalyticsWhoisOverviewLiveResultInfo from a dict
domain_analytics_whois_overview_live_result_info_from_dict = DomainAnalyticsWhoisOverviewLiveResultInfo.from_dict(domain_analytics_whois_overview_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



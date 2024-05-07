# DomainAnalyticsTechnologiesAggregationTechnologiesLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**offset** | **int** | offset in the results array of returned domains | [optional] 
**items** | [**List[DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem]**](DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_aggregation_technologies_live_result_info import DomainAnalyticsTechnologiesAggregationTechnologiesLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesAggregationTechnologiesLiveResultInfo from a JSON string
domain_analytics_technologies_aggregation_technologies_live_result_info_instance = DomainAnalyticsTechnologiesAggregationTechnologiesLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DomainAnalyticsTechnologiesAggregationTechnologiesLiveResultInfo.to_json()

# convert the object into a dict
domain_analytics_technologies_aggregation_technologies_live_result_info_dict = domain_analytics_technologies_aggregation_technologies_live_result_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesAggregationTechnologiesLiveResultInfo from a dict
domain_analytics_technologies_aggregation_technologies_live_result_info_form_dict = domain_analytics_technologies_aggregation_technologies_live_result_info.from_dict(domain_analytics_technologies_aggregation_technologies_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



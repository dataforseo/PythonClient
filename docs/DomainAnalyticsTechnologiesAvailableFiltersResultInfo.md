# DomainAnalyticsTechnologiesAvailableFiltersResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains_by_technology** | **Dict[str, Optional[str]]** |  | [optional] 
**aggregation_technologies** | **Dict[str, Optional[str]]** |  | [optional] 
**technologies_summary** | **Dict[str, Optional[str]]** |  | [optional] 
**domains_by_html_terms** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_available_filters_result_info import DomainAnalyticsTechnologiesAvailableFiltersResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesAvailableFiltersResultInfo from a JSON string
domain_analytics_technologies_available_filters_result_info_instance = DomainAnalyticsTechnologiesAvailableFiltersResultInfo.from_json(json)
# print the JSON string representation of the object
print(DomainAnalyticsTechnologiesAvailableFiltersResultInfo.to_json())

# convert the object into a dict
domain_analytics_technologies_available_filters_result_info_dict = domain_analytics_technologies_available_filters_result_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesAvailableFiltersResultInfo from a dict
domain_analytics_technologies_available_filters_result_info_from_dict = DomainAnalyticsTechnologiesAvailableFiltersResultInfo.from_dict(domain_analytics_technologies_available_filters_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



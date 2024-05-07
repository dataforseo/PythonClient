# AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_technologies** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**domains_by_technology** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**languages** | **float** |  | [optional] 
**locations** | **float** |  | [optional] 
**technologies** | **float** |  | [optional] 
**aggregation_technologies** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**technologies_summary** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**domains_by_html_terms** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**technology_stats** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_technologies_domain_analytics_limits_rates_data_info import AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo from a JSON string
appendix_technologies_domain_analytics_limits_rates_data_info_instance = AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo.to_json()

# convert the object into a dict
appendix_technologies_domain_analytics_limits_rates_data_info_dict = appendix_technologies_domain_analytics_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo from a dict
appendix_technologies_domain_analytics_limits_rates_data_info_form_dict = appendix_technologies_domain_analytics_limits_rates_data_info.from_dict(appendix_technologies_domain_analytics_limits_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



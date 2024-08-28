# AppendixDomainAnalyticsDayStatisticsRatesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks_ready** | **float** |  | [optional] 
**errors** | **float** |  | [optional] 
**whois** | [**AppendixWhoisDomainAnalyticsLimitsRatesDataInfo**](AppendixWhoisDomainAnalyticsLimitsRatesDataInfo.md) |  | [optional] 
**technologies** | [**AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo**](AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo.md) |  | [optional] 
**id_list** | **float** |  | [optional] 
**available_filters** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_domain_analytics_day_statistics_rates_data import AppendixDomainAnalyticsDayStatisticsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixDomainAnalyticsDayStatisticsRatesData from a JSON string
appendix_domain_analytics_day_statistics_rates_data_instance = AppendixDomainAnalyticsDayStatisticsRatesData.from_json(json)
# print the JSON string representation of the object
print AppendixDomainAnalyticsDayStatisticsRatesData.to_json()

# convert the object into a dict
appendix_domain_analytics_day_statistics_rates_data_dict = appendix_domain_analytics_day_statistics_rates_data_instance.to_dict()
# create an instance of AppendixDomainAnalyticsDayStatisticsRatesData from a dict
appendix_domain_analytics_day_statistics_rates_data_form_dict = appendix_domain_analytics_day_statistics_rates_data.from_dict(appendix_domain_analytics_day_statistics_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



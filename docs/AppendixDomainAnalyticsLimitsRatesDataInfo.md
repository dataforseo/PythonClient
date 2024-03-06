[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixDomainAnalyticsLimitsRatesDataInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks_ready** | **float** |  | [optional]
**errors** | **float** |  | [optional]
**whois** | [**AppendixWhoisDomainAnalyticsLimitsRatesDataInfo**](AppendixWhoisDomainAnalyticsLimitsRatesDataInfo.md) |  | [optional]
**technologies** | [**AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo**](AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_domain_analytics_limits_rates_data_info import AppendixDomainAnalyticsLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixDomainAnalyticsLimitsRatesDataInfo from a JSON string
appendix_domain_analytics_limits_rates_data_info_instance = AppendixDomainAnalyticsLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixDomainAnalyticsLimitsRatesDataInfo.to_json()

# convert the object into a dict
appendix_domain_analytics_limits_rates_data_info_dict = appendix_domain_analytics_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixDomainAnalyticsLimitsRatesDataInfo from a dict
appendix_domain_analytics_limits_rates_data_info_form_dict = appendix_domain_analytics_limits_rates_data_info.from_dict(appendix_domain_analytics_limits_rates_data_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
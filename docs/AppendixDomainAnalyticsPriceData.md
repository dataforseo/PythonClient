# AppendixDomainAnalyticsPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whois** | [**AppendixWhoisDomainAnalyticsPriceData**](AppendixWhoisDomainAnalyticsPriceData.md) |  | [optional] 
**technologies** | [**AppendixTechnologiesDomainAnalyticsPriceData**](AppendixTechnologiesDomainAnalyticsPriceData.md) |  | [optional] 
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_domain_analytics_price_data import AppendixDomainAnalyticsPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixDomainAnalyticsPriceData from a JSON string
appendix_domain_analytics_price_data_instance = AppendixDomainAnalyticsPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixDomainAnalyticsPriceData.to_json())

# convert the object into a dict
appendix_domain_analytics_price_data_dict = appendix_domain_analytics_price_data_instance.to_dict()
# create an instance of AppendixDomainAnalyticsPriceData from a dict
appendix_domain_analytics_price_data_from_dict = AppendixDomainAnalyticsPriceData.from_dict(appendix_domain_analytics_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppendixTechnologiesDomainAnalyticsPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**locations** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**technologies** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**aggregation_technologies** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domains_by_html_terms** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domains_by_technology** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domain_technologies** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**technologies_summary** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**technology_stats** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_technologies_domain_analytics_price_data import AppendixTechnologiesDomainAnalyticsPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixTechnologiesDomainAnalyticsPriceData from a JSON string
appendix_technologies_domain_analytics_price_data_instance = AppendixTechnologiesDomainAnalyticsPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixTechnologiesDomainAnalyticsPriceData.to_json())

# convert the object into a dict
appendix_technologies_domain_analytics_price_data_dict = appendix_technologies_domain_analytics_price_data_instance.to_dict()
# create an instance of AppendixTechnologiesDomainAnalyticsPriceData from a dict
appendix_technologies_domain_analytics_price_data_from_dict = AppendixTechnologiesDomainAnalyticsPriceData.from_dict(appendix_technologies_domain_analytics_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



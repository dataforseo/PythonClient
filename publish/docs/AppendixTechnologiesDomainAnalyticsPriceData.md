# AppendixTechnologiesDomainAnalyticsPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**locations** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**technologies** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**aggregation_technologies** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domains_by_html_terms** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domains_by_technology** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domain_technologies** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**technologies_summary** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**technology_stats** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_technologies_domain_analytics_price_data import AppendixTechnologiesDomainAnalyticsPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixTechnologiesDomainAnalyticsPriceData from a JSON string
appendix_technologies_domain_analytics_price_data_instance = AppendixTechnologiesDomainAnalyticsPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixTechnologiesDomainAnalyticsPriceData.to_json()

# convert the object into a dict
appendix_technologies_domain_analytics_price_data_dict = appendix_technologies_domain_analytics_price_data_instance.to_dict()
# create an instance of AppendixTechnologiesDomainAnalyticsPriceData from a dict
appendix_technologies_domain_analytics_price_data_form_dict = appendix_technologies_domain_analytics_price_data.from_dict(appendix_technologies_domain_analytics_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppendixDataforseoLabsPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_competitors** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**app_intersection** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_app_metrics** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_keyword_difficulty** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_search_volume** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_traffic_estimation** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**categories** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**categories_for_domain** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**competitors_domain** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domain_intersection** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domain_metrics_by_categories** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domain_rank_overview** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domain_whois_overview** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**historical_rank_overview** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**historical_search_volume** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**historical_serps** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**keyword_ideas** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**keywords_for_app** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**keywords_for_categories** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**keywords_for_site** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**keyword_suggestions** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**locations_and_languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**page_intersection** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**product_competitors** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**product_keyword_intersections** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**product_rank_overview** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**ranked_keywords** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**related_keywords** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**relevant_pages** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**search_intent** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**serp_competitors** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**subdomains** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**top_searches** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_dataforseo_labs_price_data import AppendixDataforseoLabsPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixDataforseoLabsPriceData from a JSON string
appendix_dataforseo_labs_price_data_instance = AppendixDataforseoLabsPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixDataforseoLabsPriceData.to_json())

# convert the object into a dict
appendix_dataforseo_labs_price_data_dict = appendix_dataforseo_labs_price_data_instance.to_dict()
# create an instance of AppendixDataforseoLabsPriceData from a dict
appendix_dataforseo_labs_price_data_from_dict = AppendixDataforseoLabsPriceData.from_dict(appendix_dataforseo_labs_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



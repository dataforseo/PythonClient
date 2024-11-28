# AppendixDataforseoLabsLimitsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations_and_languages** | **float** |  | [optional] 
**categories** | **float** |  | [optional] 
**errors** | **float** |  | [optional] 
**product_competitors** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**product_keyword_intersections** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**product_rank_overview** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**ranked_keywords** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**serp_competitors** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**subdomains** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**relevant_pages** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**competitors_domain** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**related_keywords** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**domain_rank_overview** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**domain_intersection** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**page_intersection** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**bulk_traffic_estimation** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**bulk_keyword_difficulty** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**bulk_search_volume** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**keywords_for_site** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**keyword_suggestions** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**keyword_ideas** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**historical_search_volume** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**categories_for_domain** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**domain_metrics_by_categories** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**top_searches** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**domain_whois_overview** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**historical_rank_overview** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**keywords_for_categories** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**historical_serps** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**app_competitors** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**keywords_for_app** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**app_intersection** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**bulk_app_metrics** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**search_intent** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_dataforseo_labs_limits_rates_data_info import AppendixDataforseoLabsLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixDataforseoLabsLimitsRatesDataInfo from a JSON string
appendix_dataforseo_labs_limits_rates_data_info_instance = AppendixDataforseoLabsLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixDataforseoLabsLimitsRatesDataInfo.to_json())

# convert the object into a dict
appendix_dataforseo_labs_limits_rates_data_info_dict = appendix_dataforseo_labs_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixDataforseoLabsLimitsRatesDataInfo from a dict
appendix_dataforseo_labs_limits_rates_data_info_from_dict = AppendixDataforseoLabsLimitsRatesDataInfo.from_dict(appendix_dataforseo_labs_limits_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



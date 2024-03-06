[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixDataforseoLabsPriceData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_competitors** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**app_intersection** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**bulk_app_metrics** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**bulk_keyword_difficulty** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**bulk_search_volume** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**bulk_traffic_estimation** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**categories** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**categories_for_domain** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**competitors_domain** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**domain_intersection** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**domain_metrics_by_categories** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**domain_rank_overview** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**domain_whois_overview** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**historical_rank_overview** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**historical_search_volume** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**historical_serps** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**keyword_ideas** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**keywords_for_app** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**keywords_for_categories** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**keywords_for_site** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**keyword_suggestions** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**locations_and_languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**page_intersection** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**product_competitors** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**product_keyword_intersections** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**product_rank_overview** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**ranked_keywords** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**related_keywords** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**relevant_pages** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**search_intent** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**serp_competitors** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**subdomains** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**top_searches** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_dataforseo_labs_price_data import AppendixDataforseoLabsPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixDataforseoLabsPriceData from a JSON string
appendix_dataforseo_labs_price_data_instance = AppendixDataforseoLabsPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixDataforseoLabsPriceData.to_json()

# convert the object into a dict
appendix_dataforseo_labs_price_data_dict = appendix_dataforseo_labs_price_data_instance.to_dict()
# create an instance of AppendixDataforseoLabsPriceData from a dict
appendix_dataforseo_labs_price_data_form_dict = appendix_dataforseo_labs_price_data.from_dict(appendix_dataforseo_labs_price_data_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixKeywordsDataDaysRatesDataInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords_for_keywords** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**keywords_for_site** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**search_volume** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**ad_traffic_by_keywords** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**languages** | **float** |  | [optional]
**locations** | **float** |  | [optional]
**tasks_ready** | **float** |  | [optional]
**explore** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**categories** | **float** |  | [optional]
**errors** | **float** |  | [optional]
**bing** | [**AppendixBingKeywordsDataLimitsRatesDataInfo**](AppendixBingKeywordsDataLimitsRatesDataInfo.md) |  | [optional]
**keyword_performance** | [**AppendixKeywordPerformanceKeywordsDataLimitsRatesDataInfo**](AppendixKeywordPerformanceKeywordsDataLimitsRatesDataInfo.md) |  | [optional]
**search_volume_history** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**google_ads** | [**AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo**](AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_keywords_data_days_rates_data_info import AppendixKeywordsDataDaysRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixKeywordsDataDaysRatesDataInfo from a JSON string
appendix_keywords_data_days_rates_data_info_instance = AppendixKeywordsDataDaysRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixKeywordsDataDaysRatesDataInfo.to_json()

# convert the object into a dict
appendix_keywords_data_days_rates_data_info_dict = appendix_keywords_data_days_rates_data_info_instance.to_dict()
# create an instance of AppendixKeywordsDataDaysRatesDataInfo from a dict
appendix_keywords_data_days_rates_data_info_form_dict = appendix_keywords_data_days_rates_data_info.from_dict(appendix_keywords_data_days_rates_data_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
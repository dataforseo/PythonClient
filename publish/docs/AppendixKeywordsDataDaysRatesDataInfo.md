# AppendixKeywordsDataDaysRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords_for_keywords** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**keywords_for_site** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**search_volume** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**ad_traffic_by_keywords** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**languages** | **float** |  | [optional] 
**locations** | **float** |  | [optional] 
**tasks_ready** | **float** |  | [optional] 
**explore** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**categories** | **float** |  | [optional] 
**errors** | **float** |  | [optional] 
**bing** | [**AppendixBingKeywordsDataLimitsRatesDataInfo**](AppendixBingKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**keyword_performance** | [**AppendixKeywordPerformanceKeywordsDataLimitsRatesDataInfo**](AppendixKeywordPerformanceKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**search_volume_history** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**google_ads** | [**AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo**](AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**dataforseo_trends** | [**AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo**](AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 

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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



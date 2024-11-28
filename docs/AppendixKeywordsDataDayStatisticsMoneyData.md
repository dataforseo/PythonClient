# AppendixKeywordsDataDayStatisticsMoneyData


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
**bing** | [**AppendixBingKeywordsDataDayStatisticsDataInfo**](AppendixBingKeywordsDataDayStatisticsDataInfo.md) |  | [optional] 
**keyword_performance** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**locations_and_languages** | **float** |  | [optional] 
**google_ads** | [**AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo**](AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**dataforseo_trends** | [**AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo**](AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**clickstream_data** | [**AppendixClickstreamDataKeywordsDataLimitsRatesDataInfo**](AppendixClickstreamDataKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**audience_estimation** | [**AppendixDayLimitsRatesDataInfo**](AppendixDayLimitsRatesDataInfo.md) |  | [optional] 
**keyword_suggestions_for_url** | [**AppendixDayLimitsRatesDataInfo**](AppendixDayLimitsRatesDataInfo.md) |  | [optional] 
**search_volume_history** | [**AppendixDayLimitsRatesDataInfo**](AppendixDayLimitsRatesDataInfo.md) |  | [optional] 
**google** | [**AppendixBingKeywordsDataLimitsRatesDataInfo**](AppendixBingKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_keywords_data_day_statistics_money_data import AppendixKeywordsDataDayStatisticsMoneyData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixKeywordsDataDayStatisticsMoneyData from a JSON string
appendix_keywords_data_day_statistics_money_data_instance = AppendixKeywordsDataDayStatisticsMoneyData.from_json(json)
# print the JSON string representation of the object
print(AppendixKeywordsDataDayStatisticsMoneyData.to_json())

# convert the object into a dict
appendix_keywords_data_day_statistics_money_data_dict = appendix_keywords_data_day_statistics_money_data_instance.to_dict()
# create an instance of AppendixKeywordsDataDayStatisticsMoneyData from a dict
appendix_keywords_data_day_statistics_money_data_from_dict = AppendixKeywordsDataDayStatisticsMoneyData.from_dict(appendix_keywords_data_day_statistics_money_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



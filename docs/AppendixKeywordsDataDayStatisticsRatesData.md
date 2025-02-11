# AppendixKeywordsDataDayStatisticsRatesData


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
**audience_estimation** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**keyword_suggestions_for_url** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**job_functions** | **float** |  | [optional] 
**search_volume_history** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**google** | [**AppendixBingKeywordsDataLimitsRatesDataInfo**](AppendixBingKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**industries** | **float** |  | [optional] 
**id_list** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_keywords_data_day_statistics_rates_data import AppendixKeywordsDataDayStatisticsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixKeywordsDataDayStatisticsRatesData from a JSON string
appendix_keywords_data_day_statistics_rates_data_instance = AppendixKeywordsDataDayStatisticsRatesData.from_json(json)
# print the JSON string representation of the object
print(AppendixKeywordsDataDayStatisticsRatesData.to_json())

# convert the object into a dict
appendix_keywords_data_day_statistics_rates_data_dict = appendix_keywords_data_day_statistics_rates_data_instance.to_dict()
# create an instance of AppendixKeywordsDataDayStatisticsRatesData from a dict
appendix_keywords_data_day_statistics_rates_data_from_dict = AppendixKeywordsDataDayStatisticsRatesData.from_dict(appendix_keywords_data_day_statistics_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



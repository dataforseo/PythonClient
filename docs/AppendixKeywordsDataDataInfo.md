# AppendixKeywordsDataDataInfo


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
**keyword_performance** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**locations_and_languages** | **float** |  | [optional] 
**search_volume_history** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**google_ads** | [**AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo**](AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**dataforseo_trends** | [**AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo**](AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**naver** | [**AppendixNaverKeywordsDataDataInfo**](AppendixNaverKeywordsDataDataInfo.md) |  | [optional] 
**google** | [**AppendixBingKeywordsDataLimitsRatesDataInfo**](AppendixBingKeywordsDataLimitsRatesDataInfo.md) |  | [optional] 
**keyword_ideas_ads_api** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_keywords_data_data_info import AppendixKeywordsDataDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixKeywordsDataDataInfo from a JSON string
appendix_keywords_data_data_info_instance = AppendixKeywordsDataDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixKeywordsDataDataInfo.to_json()

# convert the object into a dict
appendix_keywords_data_data_info_dict = appendix_keywords_data_data_info_instance.to_dict()
# create an instance of AppendixKeywordsDataDataInfo from a dict
appendix_keywords_data_data_info_form_dict = appendix_keywords_data_data_info.from_dict(appendix_keywords_data_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



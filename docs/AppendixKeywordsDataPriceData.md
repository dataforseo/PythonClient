# AppendixKeywordsDataPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**ad_traffic_by_keywords** | [**AppendixKeywordsKeywordsDataPriceDataInfo**](AppendixKeywordsKeywordsDataPriceDataInfo.md) |  | [optional] 
**bing** | [**AppendixBingKeywordsDataPriceData**](AppendixBingKeywordsDataPriceData.md) |  | [optional] 
**categories** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**google_ads** | [**AppendixGoogleAdsKeywordsDataPriceData**](AppendixGoogleAdsKeywordsDataPriceData.md) |  | [optional] 
**keyword_performance** | [**AppendixKeywordPerformanceKeywordsDataPriceData**](AppendixKeywordPerformanceKeywordsDataPriceData.md) |  | [optional] 
**keywords_for_keywords** | [**AppendixKeywordsKeywordsDataPriceDataInfo**](AppendixKeywordsKeywordsDataPriceDataInfo.md) |  | [optional] 
**keywords_for_site** | [**AppendixKeywordsKeywordsDataPriceDataInfo**](AppendixKeywordsKeywordsDataPriceDataInfo.md) |  | [optional] 
**languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**locations** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**search_volume_history** | [**AppendixKeywordsKeywordsDataPriceDataInfo**](AppendixKeywordsKeywordsDataPriceDataInfo.md) |  | [optional] 
**search_volume** | [**AppendixKeywordsKeywordsDataPriceDataInfo**](AppendixKeywordsKeywordsDataPriceDataInfo.md) |  | [optional] 
**explore** | [**AppendixExploreKeywordsDataPriceData**](AppendixExploreKeywordsDataPriceData.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_keywords_data_price_data import AppendixKeywordsDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixKeywordsDataPriceData from a JSON string
appendix_keywords_data_price_data_instance = AppendixKeywordsDataPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixKeywordsDataPriceData.to_json()

# convert the object into a dict
appendix_keywords_data_price_data_dict = appendix_keywords_data_price_data_instance.to_dict()
# create an instance of AppendixKeywordsDataPriceData from a dict
appendix_keywords_data_price_data_form_dict = appendix_keywords_data_price_data.from_dict(appendix_keywords_data_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



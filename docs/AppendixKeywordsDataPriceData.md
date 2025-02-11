# AppendixKeywordsDataPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**ad_traffic_by_keywords** | [**AppendixAKeywordsDataPriceDataInfo**](AppendixAKeywordsDataPriceDataInfo.md) |  | [optional] 
**audience_estimation** | [**AppendixAKeywordsDataPriceDataInfo**](AppendixAKeywordsDataPriceDataInfo.md) |  | [optional] 
**bing** | [**AppendixBingKeywordsDataPriceData**](AppendixBingKeywordsDataPriceData.md) |  | [optional] 
**categories** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**clickstream_data** | [**AppendixClickstreamDataKeywordsDataPriceData**](AppendixClickstreamDataKeywordsDataPriceData.md) |  | [optional] 
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**google_ads** | [**AppendixGoogleAdsKeywordsDataPriceData**](AppendixGoogleAdsKeywordsDataPriceData.md) |  | [optional] 
**keyword_performance** | [**AppendixAKeywordsDataPriceDataInfo**](AppendixAKeywordsDataPriceDataInfo.md) |  | [optional] 
**keywords_for_keywords** | [**AppendixAKeywordsDataPriceDataInfo**](AppendixAKeywordsDataPriceDataInfo.md) |  | [optional] 
**keywords_for_site** | [**AppendixAKeywordsDataPriceDataInfo**](AppendixAKeywordsDataPriceDataInfo.md) |  | [optional] 
**keyword_suggestions_for_url** | [**AppendixAKeywordsDataPriceDataInfo**](AppendixAKeywordsDataPriceDataInfo.md) |  | [optional] 
**languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**locations** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**locations_and_languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**search_volume** | [**AppendixAKeywordsDataPriceDataInfo**](AppendixAKeywordsDataPriceDataInfo.md) |  | [optional] 
**dataforseo_trends** | [**AppendixDataforseoTrendsKeywordsDataPriceData**](AppendixDataforseoTrendsKeywordsDataPriceData.md) |  | [optional] 
**explore** | [**AppendixExploreKeywordsDataPriceData**](AppendixExploreKeywordsDataPriceData.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_keywords_data_price_data import AppendixKeywordsDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixKeywordsDataPriceData from a JSON string
appendix_keywords_data_price_data_instance = AppendixKeywordsDataPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixKeywordsDataPriceData.to_json())

# convert the object into a dict
appendix_keywords_data_price_data_dict = appendix_keywords_data_price_data_instance.to_dict()
# create an instance of AppendixKeywordsDataPriceData from a dict
appendix_keywords_data_price_data_from_dict = AppendixKeywordsDataPriceData.from_dict(appendix_keywords_data_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



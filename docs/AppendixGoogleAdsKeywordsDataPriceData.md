# AppendixGoogleAdsKeywordsDataPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_traffic_by_keywords** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**keywords_for_keywords** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**keywords_for_site** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**search_volume** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**status** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_google_ads_keywords_data_price_data import AppendixGoogleAdsKeywordsDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixGoogleAdsKeywordsDataPriceData from a JSON string
appendix_google_ads_keywords_data_price_data_instance = AppendixGoogleAdsKeywordsDataPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixGoogleAdsKeywordsDataPriceData.to_json())

# convert the object into a dict
appendix_google_ads_keywords_data_price_data_dict = appendix_google_ads_keywords_data_price_data_instance.to_dict()
# create an instance of AppendixGoogleAdsKeywordsDataPriceData from a dict
appendix_google_ads_keywords_data_price_data_from_dict = AppendixGoogleAdsKeywordsDataPriceData.from_dict(appendix_google_ads_keywords_data_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



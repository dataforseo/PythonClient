# AppendixBacklinksPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchors** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**backlinks** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_backlinks** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_new_lost_backlinks** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_new_lost_referring_domains** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_pages_summary** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_ranks** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_referring_domains** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**bulk_spam_score** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**competitors** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**content_duplicates** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domain_intersection** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domain_pages** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**domain_pages_summary** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**history** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**page_intersection** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**referring_domains** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**referring_networks** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**summary** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**timeseries_new_lost_summary** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**timeseries_summary** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_backlinks_price_data import AppendixBacklinksPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixBacklinksPriceData from a JSON string
appendix_backlinks_price_data_instance = AppendixBacklinksPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixBacklinksPriceData.to_json())

# convert the object into a dict
appendix_backlinks_price_data_dict = appendix_backlinks_price_data_instance.to_dict()
# create an instance of AppendixBacklinksPriceData from a dict
appendix_backlinks_price_data_from_dict = AppendixBacklinksPriceData.from_dict(appendix_backlinks_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppendixClickstreamDataKeywordsDataPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_search_volume** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**dataforseo_search_volume** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**global_search_volume** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**locations_and_languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_clickstream_data_keywords_data_price_data import AppendixClickstreamDataKeywordsDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixClickstreamDataKeywordsDataPriceData from a JSON string
appendix_clickstream_data_keywords_data_price_data_instance = AppendixClickstreamDataKeywordsDataPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixClickstreamDataKeywordsDataPriceData.to_json())

# convert the object into a dict
appendix_clickstream_data_keywords_data_price_data_dict = appendix_clickstream_data_keywords_data_price_data_instance.to_dict()
# create an instance of AppendixClickstreamDataKeywordsDataPriceData from a dict
appendix_clickstream_data_keywords_data_price_data_from_dict = AppendixClickstreamDataKeywordsDataPriceData.from_dict(appendix_clickstream_data_keywords_data_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



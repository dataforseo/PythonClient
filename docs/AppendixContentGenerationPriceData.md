# AppendixContentGenerationPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_grammar** | [**AppendixContentGenerationPriceDataInfo**](AppendixContentGenerationPriceDataInfo.md) |  | [optional] 
**generate** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**generate_meta_tags** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**generate_sub_topics** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**generate_text** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**paraphrase** | [**AppendixBingKeywordsDataPriceDataInfo**](AppendixBingKeywordsDataPriceDataInfo.md) |  | [optional] 
**text_summary** | [**AppendixContentGenerationPriceDataInfo**](AppendixContentGenerationPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_content_generation_price_data import AppendixContentGenerationPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixContentGenerationPriceData from a JSON string
appendix_content_generation_price_data_instance = AppendixContentGenerationPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixContentGenerationPriceData.to_json())

# convert the object into a dict
appendix_content_generation_price_data_dict = appendix_content_generation_price_data_instance.to_dict()
# create an instance of AppendixContentGenerationPriceData from a dict
appendix_content_generation_price_data_from_dict = AppendixContentGenerationPriceData.from_dict(appendix_content_generation_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



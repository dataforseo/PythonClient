# AppendixPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords_data** | [**AppendixKeywordsDataPriceData**](AppendixKeywordsDataPriceData.md) |  | [optional] 
**merchant** | [**AppendixMerchantPriceData**](AppendixMerchantPriceData.md) |  | [optional] 
**serp** | [**AppendixSerpPriceData**](AppendixSerpPriceData.md) |  | [optional] 
**appendix** | [**AppendixAppendixPriceData**](AppendixAppendixPriceData.md) |  | [optional] 
**app_data** | [**AppendixAppDataPriceData**](AppendixAppDataPriceData.md) |  | [optional] 
**backlinks** | [**AppendixBacklinksPriceData**](AppendixBacklinksPriceData.md) |  | [optional] 
**business_data** | [**AppendixBusinessDataPriceData**](AppendixBusinessDataPriceData.md) |  | [optional] 
**content_analysis** | [**AppendixContentAnalysisPriceData**](AppendixContentAnalysisPriceData.md) |  | [optional] 
**content_generation** | [**AppendixContentGenerationPriceData**](AppendixContentGenerationPriceData.md) |  | [optional] 
**dataforseo_labs** | [**AppendixDataforseoLabsPriceData**](AppendixDataforseoLabsPriceData.md) |  | [optional] 
**domain_analytics** | [**AppendixDomainAnalyticsPriceData**](AppendixDomainAnalyticsPriceData.md) |  | [optional] 
**on_page** | [**AppendixOnPagePriceData**](AppendixOnPagePriceData.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_price_data import AppendixPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixPriceData from a JSON string
appendix_price_data_instance = AppendixPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixPriceData.to_json()

# convert the object into a dict
appendix_price_data_dict = appendix_price_data_instance.to_dict()
# create an instance of AppendixPriceData from a dict
appendix_price_data_form_dict = appendix_price_data.from_dict(appendix_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



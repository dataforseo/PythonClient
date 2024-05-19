# AppendixAppDataPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_info** | [**AppendixProductGoogleMerchantPriceDataInfo**](AppendixProductGoogleMerchantPriceDataInfo.md) |  | [optional] 
**app_list** | [**AppendixProductGoogleMerchantPriceDataInfo**](AppendixProductGoogleMerchantPriceDataInfo.md) |  | [optional] 
**app_reviews** | [**AppendixPriceDataInfo**](AppendixPriceDataInfo.md) |  | [optional] 
**app_searches** | [**AppendixProductGoogleMerchantPriceDataInfo**](AppendixProductGoogleMerchantPriceDataInfo.md) |  | [optional] 
**categories** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**locations** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_app_data_price_data import AppendixAppDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixAppDataPriceData from a JSON string
appendix_app_data_price_data_instance = AppendixAppDataPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixAppDataPriceData.to_json()

# convert the object into a dict
appendix_app_data_price_data_dict = appendix_app_data_price_data_instance.to_dict()
# create an instance of AppendixAppDataPriceData from a dict
appendix_app_data_price_data_form_dict = appendix_app_data_price_data.from_dict(appendix_app_data_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



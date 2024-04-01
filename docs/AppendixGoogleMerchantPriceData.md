# AppendixGoogleMerchantPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_info** | [**AppendixPriceDataInfo**](AppendixPriceDataInfo.md) |  | [optional] 
**product_spec** | [**AppendixProductGoogleMerchantPriceDataInfo**](AppendixProductGoogleMerchantPriceDataInfo.md) |  | [optional] 
**products** | [**AppendixProductGoogleMerchantPriceDataInfo**](AppendixProductGoogleMerchantPriceDataInfo.md) |  | [optional] 
**sellers** | [**AppendixSellersGoogleMerchantPriceData**](AppendixSellersGoogleMerchantPriceData.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_google_merchant_price_data import AppendixGoogleMerchantPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixGoogleMerchantPriceData from a JSON string
appendix_google_merchant_price_data_instance = AppendixGoogleMerchantPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixGoogleMerchantPriceData.to_json())

# convert the object into a dict
appendix_google_merchant_price_data_dict = appendix_google_merchant_price_data_instance.to_dict()
# create an instance of AppendixGoogleMerchantPriceData from a dict
appendix_google_merchant_price_data_form_dict = appendix_google_merchant_price_data.from_dict(appendix_google_merchant_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



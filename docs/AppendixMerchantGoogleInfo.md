# AppendixMerchantGoogleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**AppendixSerpsRatesDataInfo**](AppendixSerpsRatesDataInfo.md) |  | [optional] 
**sellers** | [**AppendixSellersGoogleMerchantLimitsRatesDataInfo**](AppendixSellersGoogleMerchantLimitsRatesDataInfo.md) |  | [optional] 
**product_spec** | [**AppendixSerpsRatesDataInfo**](AppendixSerpsRatesDataInfo.md) |  | [optional] 
**product_info** | [**AppendixSerpsRatesDataInfo**](AppendixSerpsRatesDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_merchant_google_info import AppendixMerchantGoogleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixMerchantGoogleInfo from a JSON string
appendix_merchant_google_info_instance = AppendixMerchantGoogleInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixMerchantGoogleInfo.to_json())

# convert the object into a dict
appendix_merchant_google_info_dict = appendix_merchant_google_info_instance.to_dict()
# create an instance of AppendixMerchantGoogleInfo from a dict
appendix_merchant_google_info_from_dict = AppendixMerchantGoogleInfo.from_dict(appendix_merchant_google_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



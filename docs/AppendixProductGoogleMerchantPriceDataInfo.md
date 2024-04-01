# AppendixProductGoogleMerchantPriceDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_get** | [**AppendixTaskGetProductGoogleMerchantPriceDataInfo**](AppendixTaskGetProductGoogleMerchantPriceDataInfo.md) |  | [optional] 
**task_post** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_product_google_merchant_price_data_info import AppendixProductGoogleMerchantPriceDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixProductGoogleMerchantPriceDataInfo from a JSON string
appendix_product_google_merchant_price_data_info_instance = AppendixProductGoogleMerchantPriceDataInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixProductGoogleMerchantPriceDataInfo.to_json())

# convert the object into a dict
appendix_product_google_merchant_price_data_info_dict = appendix_product_google_merchant_price_data_info_instance.to_dict()
# create an instance of AppendixProductGoogleMerchantPriceDataInfo from a dict
appendix_product_google_merchant_price_data_info_form_dict = appendix_product_google_merchant_price_data_info.from_dict(appendix_product_google_merchant_price_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



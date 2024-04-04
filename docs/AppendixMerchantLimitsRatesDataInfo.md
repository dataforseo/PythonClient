# AppendixMerchantLimitsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google** | [**AppendixMerchantGoogleInfo**](AppendixMerchantGoogleInfo.md) |  | [optional] 
**amazon** | [**AppendixMerchantAmazonInfo**](AppendixMerchantAmazonInfo.md) |  | [optional] 
**locations** | **float** |  | [optional] 
**languages** | **float** |  | [optional] 
**errors** | **float** |  | [optional] 
**reviews** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_merchant_limits_rates_data_info import AppendixMerchantLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixMerchantLimitsRatesDataInfo from a JSON string
appendix_merchant_limits_rates_data_info_instance = AppendixMerchantLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixMerchantLimitsRatesDataInfo.to_json()

# convert the object into a dict
appendix_merchant_limits_rates_data_info_dict = appendix_merchant_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixMerchantLimitsRatesDataInfo from a dict
appendix_merchant_limits_rates_data_info_form_dict = appendix_merchant_limits_rates_data_info.from_dict(appendix_merchant_limits_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



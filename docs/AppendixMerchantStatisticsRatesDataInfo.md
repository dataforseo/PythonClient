# AppendixMerchantStatisticsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google** | [**AppendixMerchantGoogleInfo**](AppendixMerchantGoogleInfo.md) |  | [optional] 
**amazon** | [**AppendixMerchantAmazonInfo**](AppendixMerchantAmazonInfo.md) |  | [optional] 
**locations** | **float** |  | [optional] 
**languages** | **float** |  | [optional] 
**errors** | **float** |  | [optional] 
**reviews** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**tasks_ready** | **float** |  | [optional] 
**id_list** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_merchant_statistics_rates_data_info import AppendixMerchantStatisticsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixMerchantStatisticsRatesDataInfo from a JSON string
appendix_merchant_statistics_rates_data_info_instance = AppendixMerchantStatisticsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixMerchantStatisticsRatesDataInfo.to_json()

# convert the object into a dict
appendix_merchant_statistics_rates_data_info_dict = appendix_merchant_statistics_rates_data_info_instance.to_dict()
# create an instance of AppendixMerchantStatisticsRatesDataInfo from a dict
appendix_merchant_statistics_rates_data_info_form_dict = appendix_merchant_statistics_rates_data_info.from_dict(appendix_merchant_statistics_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



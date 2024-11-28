# AppendixMerchantDayStatisticsRatesData


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
from dataforseo_client.models.appendix_merchant_day_statistics_rates_data import AppendixMerchantDayStatisticsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixMerchantDayStatisticsRatesData from a JSON string
appendix_merchant_day_statistics_rates_data_instance = AppendixMerchantDayStatisticsRatesData.from_json(json)
# print the JSON string representation of the object
print(AppendixMerchantDayStatisticsRatesData.to_json())

# convert the object into a dict
appendix_merchant_day_statistics_rates_data_dict = appendix_merchant_day_statistics_rates_data_instance.to_dict()
# create an instance of AppendixMerchantDayStatisticsRatesData from a dict
appendix_merchant_day_statistics_rates_data_from_dict = AppendixMerchantDayStatisticsRatesData.from_dict(appendix_merchant_day_statistics_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



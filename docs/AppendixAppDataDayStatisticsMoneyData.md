# AppendixAppDataDayStatisticsMoneyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_info** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**app_list** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**app_reviews** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**app_searches** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**errors** | **float** |  | [optional] 
**languages** | **float** |  | [optional] 
**locations** | **float** |  | [optional] 
**categories** | **float** |  | [optional] 
**app_listings** | [**AppendixBusinessListingsBusinessDataLimitsRatesDataInfo**](AppendixBusinessListingsBusinessDataLimitsRatesDataInfo.md) |  | [optional] 
**tasks_ready** | **float** |  | [optional] 
**refund_money** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_app_data_day_statistics_money_data import AppendixAppDataDayStatisticsMoneyData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixAppDataDayStatisticsMoneyData from a JSON string
appendix_app_data_day_statistics_money_data_instance = AppendixAppDataDayStatisticsMoneyData.from_json(json)
# print the JSON string representation of the object
print(AppendixAppDataDayStatisticsMoneyData.to_json())

# convert the object into a dict
appendix_app_data_day_statistics_money_data_dict = appendix_app_data_day_statistics_money_data_instance.to_dict()
# create an instance of AppendixAppDataDayStatisticsMoneyData from a dict
appendix_app_data_day_statistics_money_data_from_dict = AppendixAppDataDayStatisticsMoneyData.from_dict(appendix_app_data_day_statistics_money_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



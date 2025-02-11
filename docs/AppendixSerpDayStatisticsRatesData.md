# AppendixSerpDayStatisticsRatesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_post** | **float** |  | [optional] 
**task_get** | [**AppendixFunctionTypeInfo**](AppendixFunctionTypeInfo.md) |  | [optional] 
**tasks_ready** | **float** |  | [optional] 
**locations** | **float** |  | [optional] 
**languages** | **float** |  | [optional] 
**live** | [**AppendixFunctionTypeInfo**](AppendixFunctionTypeInfo.md) |  | [optional] 
**errors** | **float** |  | [optional] 
**tasks_fixed** | **float** |  | [optional] 
**jobs** | [**AppendixJobsSerpLimitsRatesDataInfo**](AppendixJobsSerpLimitsRatesDataInfo.md) |  | [optional] 
**screenshot** | **float** |  | [optional] 
**id_list** | **float** |  | [optional] 
**ai_summary** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_serp_day_statistics_rates_data import AppendixSerpDayStatisticsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixSerpDayStatisticsRatesData from a JSON string
appendix_serp_day_statistics_rates_data_instance = AppendixSerpDayStatisticsRatesData.from_json(json)
# print the JSON string representation of the object
print(AppendixSerpDayStatisticsRatesData.to_json())

# convert the object into a dict
appendix_serp_day_statistics_rates_data_dict = appendix_serp_day_statistics_rates_data_instance.to_dict()
# create an instance of AppendixSerpDayStatisticsRatesData from a dict
appendix_serp_day_statistics_rates_data_from_dict = AppendixSerpDayStatisticsRatesData.from_dict(appendix_serp_day_statistics_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



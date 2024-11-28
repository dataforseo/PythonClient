# AppendixSerpLimitsRatesDataInfo


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
**jobs** | [**AppendixDayLimitsRatesDataInfo**](AppendixDayLimitsRatesDataInfo.md) |  | [optional] 
**screenshot** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_serp_limits_rates_data_info import AppendixSerpLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixSerpLimitsRatesDataInfo from a JSON string
appendix_serp_limits_rates_data_info_instance = AppendixSerpLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixSerpLimitsRatesDataInfo.to_json())

# convert the object into a dict
appendix_serp_limits_rates_data_info_dict = appendix_serp_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixSerpLimitsRatesDataInfo from a dict
appendix_serp_limits_rates_data_info_from_dict = AppendixSerpLimitsRatesDataInfo.from_dict(appendix_serp_limits_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



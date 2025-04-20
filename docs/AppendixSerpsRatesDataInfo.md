# AppendixSerpsRatesDataInfo


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

## Example

```python
from dataforseo_client.models.appendix_serps_rates_data_info import AppendixSerpsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixSerpsRatesDataInfo from a JSON string
appendix_serps_rates_data_info_instance = AppendixSerpsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixSerpsRatesDataInfo.to_json())

# convert the object into a dict
appendix_serps_rates_data_info_dict = appendix_serps_rates_data_info_instance.to_dict()
# create an instance of AppendixSerpsRatesDataInfo from a dict
appendix_serps_rates_data_info_from_dict = AppendixSerpsRatesDataInfo.from_dict(appendix_serps_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppendixSerpDataInfo


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
**tasks_ready_queue** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_serp_data_info import AppendixSerpDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixSerpDataInfo from a JSON string
appendix_serp_data_info_instance = AppendixSerpDataInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixSerpDataInfo.to_json())

# convert the object into a dict
appendix_serp_data_info_dict = appendix_serp_data_info_instance.to_dict()
# create an instance of AppendixSerpDataInfo from a dict
appendix_serp_data_info_from_dict = AppendixSerpDataInfo.from_dict(appendix_serp_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppendixFunctionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_post** | **float** |  | [optional] 
**task_get** | **float** |  | [optional] 
**tasks_ready** | **float** |  | [optional] 
**live** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_function_info import AppendixFunctionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixFunctionInfo from a JSON string
appendix_function_info_instance = AppendixFunctionInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixFunctionInfo.to_json())

# convert the object into a dict
appendix_function_info_dict = appendix_function_info_instance.to_dict()
# create an instance of AppendixFunctionInfo from a dict
appendix_function_info_form_dict = appendix_function_info.from_dict(appendix_function_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



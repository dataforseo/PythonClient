# AppendixInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_post** | **float** |  | [optional] 
**task_get** | **float** |  | [optional] 
**tasks_ready** | **float** |  | [optional] 
**live** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_info import AppendixInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixInfo from a JSON string
appendix_info_instance = AppendixInfo.from_json(json)
# print the JSON string representation of the object
print AppendixInfo.to_json()

# convert the object into a dict
appendix_info_dict = appendix_info_instance.to_dict()
# create an instance of AppendixInfo from a dict
appendix_info_form_dict = appendix_info.from_dict(appendix_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



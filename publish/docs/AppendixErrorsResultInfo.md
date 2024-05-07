# AppendixErrorsResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | code | [optional] 
**message** | **str** | message | [optional] 

## Example

```python
from dataforseo_client.models.appendix_errors_result_info import AppendixErrorsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixErrorsResultInfo from a JSON string
appendix_errors_result_info_instance = AppendixErrorsResultInfo.from_json(json)
# print the JSON string representation of the object
print AppendixErrorsResultInfo.to_json()

# convert the object into a dict
appendix_errors_result_info_dict = appendix_errors_result_info_instance.to_dict()
# create an instance of AppendixErrorsResultInfo from a dict
appendix_errors_result_info_form_dict = appendix_errors_result_info.from_dict(appendix_errors_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OnPageTasksReadyResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional] 
**target** | **str** | target website specified when setting a task | [optional] 
**date_posted** | **str** | date when the task was posted (in the UTC format) | [optional] 
**tag** | **str** | user-defined task identifier | [optional] 

## Example

```python
from dataforseo_client.models.on_page_tasks_ready_result_info import OnPageTasksReadyResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageTasksReadyResultInfo from a JSON string
on_page_tasks_ready_result_info_instance = OnPageTasksReadyResultInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageTasksReadyResultInfo.to_json())

# convert the object into a dict
on_page_tasks_ready_result_info_dict = on_page_tasks_ready_result_info_instance.to_dict()
# create an instance of OnPageTasksReadyResultInfo from a dict
on_page_tasks_ready_result_info_form_dict = on_page_tasks_ready_result_info.from_dict(on_page_tasks_ready_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



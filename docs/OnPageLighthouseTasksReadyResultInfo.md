# OnPageLighthouseTasksReadyResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional] 
**tag** | **str** | user-defined task identifier | [optional] 
**endpoint_json** | **str** | URL for collecting the results of the OnPage Lighthouse JSON task | [optional] 

## Example

```python
from dataforseo_client.models.on_page_lighthouse_tasks_ready_result_info import OnPageLighthouseTasksReadyResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageLighthouseTasksReadyResultInfo from a JSON string
on_page_lighthouse_tasks_ready_result_info_instance = OnPageLighthouseTasksReadyResultInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageLighthouseTasksReadyResultInfo.to_json())

# convert the object into a dict
on_page_lighthouse_tasks_ready_result_info_dict = on_page_lighthouse_tasks_ready_result_info_instance.to_dict()
# create an instance of OnPageLighthouseTasksReadyResultInfo from a dict
on_page_lighthouse_tasks_ready_result_info_from_dict = OnPageLighthouseTasksReadyResultInfo.from_dict(on_page_lighthouse_tasks_ready_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



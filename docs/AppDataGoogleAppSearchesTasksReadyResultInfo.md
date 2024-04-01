# AppDataGoogleAppSearchesTasksReadyResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional] 
**se** | **str** | search engine specified when setting the task | [optional] 
**date_posted** | **str** | date when the task was posted (in the UTC format) | [optional] 
**tag** | **str** | user-defined task identifier | [optional] 
**endpoint_advanced** | **str** | URL for collecting the results of the Google App Searches task | [optional] 
**endpoint_html** | **str** | URL for collecting the results of the Google App Searches HTML task if HTML tasks are not supported in the specified endpoint, the value will be null | [optional] 

## Example

```python
from dataforseo_client.models.app_data_google_app_searches_tasks_ready_result_info import AppDataGoogleAppSearchesTasksReadyResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataGoogleAppSearchesTasksReadyResultInfo from a JSON string
app_data_google_app_searches_tasks_ready_result_info_instance = AppDataGoogleAppSearchesTasksReadyResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataGoogleAppSearchesTasksReadyResultInfo.to_json())

# convert the object into a dict
app_data_google_app_searches_tasks_ready_result_info_dict = app_data_google_app_searches_tasks_ready_result_info_instance.to_dict()
# create an instance of AppDataGoogleAppSearchesTasksReadyResultInfo from a dict
app_data_google_app_searches_tasks_ready_result_info_form_dict = app_data_google_app_searches_tasks_ready_result_info.from_dict(app_data_google_app_searches_tasks_ready_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



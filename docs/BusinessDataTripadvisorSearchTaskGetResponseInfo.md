[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BusinessDataTripadvisorSearchTaskGetResponseInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | the current version of the API | [optional]
**status_code** | **int** | general status code you can find the full list of the response codes here | [optional]
**status_message** | **str** | general informational message you can find the full list of general informational messages here | [optional]
**time** | **str** | total execution time, seconds | [optional]
**cost** | **float** | total tasks cost, USD | [optional]
**tasks_count** | **int** | the number of tasks in the tasks array | [optional]
**tasks_error** | **int** | the number of tasks in the tasks array returned with an error | [optional]
**tasks** | [**List[BusinessDataTripadvisorSearchTaskGetTaskInfo]**](BusinessDataTripadvisorSearchTaskGetTaskInfo.md) | array of tasks | [optional]

## Example

```python
from dataforseo_client.models.business_data_tripadvisor_search_task_get_response_info import BusinessDataTripadvisorSearchTaskGetResponseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataTripadvisorSearchTaskGetResponseInfo from a JSON string
business_data_tripadvisor_search_task_get_response_info_instance = BusinessDataTripadvisorSearchTaskGetResponseInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataTripadvisorSearchTaskGetResponseInfo.to_json()

# convert the object into a dict
business_data_tripadvisor_search_task_get_response_info_dict = business_data_tripadvisor_search_task_get_response_info_instance.to_dict()
# create an instance of BusinessDataTripadvisorSearchTaskGetResponseInfo from a dict
business_data_tripadvisor_search_task_get_response_info_form_dict = business_data_tripadvisor_search_task_get_response_info.from_dict(business_data_tripadvisor_search_task_get_response_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
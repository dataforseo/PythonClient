# KeywordsDataBingKeywordPerformanceTasksReadyResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional] 
**se** | **str** | search engine specified when setting the task | [optional] 
**function** | **str** | type of the task | [optional] 
**date_posted** | **str** | date when the task was posted (in the UTC format) | [optional] 
**tag** | **str** | user-defined task identifier | [optional] 
**endpoint** | **str** | URL for collecting the results of the task | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_keyword_performance_tasks_ready_result_info import KeywordsDataBingKeywordPerformanceTasksReadyResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingKeywordPerformanceTasksReadyResultInfo from a JSON string
keywords_data_bing_keyword_performance_tasks_ready_result_info_instance = KeywordsDataBingKeywordPerformanceTasksReadyResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataBingKeywordPerformanceTasksReadyResultInfo.to_json())

# convert the object into a dict
keywords_data_bing_keyword_performance_tasks_ready_result_info_dict = keywords_data_bing_keyword_performance_tasks_ready_result_info_instance.to_dict()
# create an instance of KeywordsDataBingKeywordPerformanceTasksReadyResultInfo from a dict
keywords_data_bing_keyword_performance_tasks_ready_result_info_from_dict = KeywordsDataBingKeywordPerformanceTasksReadyResultInfo.from_dict(keywords_data_bing_keyword_performance_tasks_ready_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



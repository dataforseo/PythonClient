# BusinessDataGoogleReviewsTasksReadyResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional] 
**se** | **str** | search engine specified when setting the task can take the following values: google | [optional] 
**se_type** | **str** | type of search engine | [optional] 
**date_posted** | **str** | date when the task was posted (in the UTC format) | [optional] 
**tag** | **str** | user-defined task identifier | [optional] 
**endpoint** | **str** | URL for collecting the results of the task | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_reviews_tasks_ready_result_info import BusinessDataGoogleReviewsTasksReadyResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleReviewsTasksReadyResultInfo from a JSON string
business_data_google_reviews_tasks_ready_result_info_instance = BusinessDataGoogleReviewsTasksReadyResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataGoogleReviewsTasksReadyResultInfo.to_json())

# convert the object into a dict
business_data_google_reviews_tasks_ready_result_info_dict = business_data_google_reviews_tasks_ready_result_info_instance.to_dict()
# create an instance of BusinessDataGoogleReviewsTasksReadyResultInfo from a dict
business_data_google_reviews_tasks_ready_result_info_from_dict = BusinessDataGoogleReviewsTasksReadyResultInfo.from_dict(business_data_google_reviews_tasks_ready_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



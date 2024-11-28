# SerpGoogleSearchByImageTasksFixedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional] 
**se** | **str** | search engine specified when setting the task | [optional] 
**se_type** | **str** | type of search engine can take the following values: search_by_image | [optional] 
**date_fixed** | **str** | date when the task was fixed (in the UTC format) | [optional] 
**tag** | **str** | user-defined task identifier | [optional] 
**endpoint_regular** | **str** | URL for collecting the results of the SERP Regular task if SERP Regular is not supported in the specified endpoint, the value will be null | [optional] 
**endpoint_advanced** | **str** | URL for collecting the results of the SERP Advanced task if SERP Advanced is not supported in the specified endpoint, the value will be null | [optional] 
**endpoint_html** | **str** | URL for collecting the results of the SERP HTML task if SERP HTML is not supported in the specified endpoint, the value will be null | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_search_by_image_tasks_fixed_result_info import SerpGoogleSearchByImageTasksFixedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleSearchByImageTasksFixedResultInfo from a JSON string
serp_google_search_by_image_tasks_fixed_result_info_instance = SerpGoogleSearchByImageTasksFixedResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleSearchByImageTasksFixedResultInfo.to_json())

# convert the object into a dict
serp_google_search_by_image_tasks_fixed_result_info_dict = serp_google_search_by_image_tasks_fixed_result_info_instance.to_dict()
# create an instance of SerpGoogleSearchByImageTasksFixedResultInfo from a dict
serp_google_search_by_image_tasks_fixed_result_info_from_dict = SerpGoogleSearchByImageTasksFixedResultInfo.from_dict(serp_google_search_by_image_tasks_fixed_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



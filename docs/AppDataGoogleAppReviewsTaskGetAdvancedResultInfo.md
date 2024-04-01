# AppDataGoogleAppReviewsTaskGetAdvancedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | application id received in a POST array | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**title** | **str** | title of the app title of the application for which the reviews are collected | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**reviews_count** | **int** | the total number of reviews | [optional] 
**items_count** | **int** | the number of reviews items in the results array you can get more results by using the depth parameter when setting a task | [optional] 
**items** | [**List[BaseAppDataSerpElementItem]**](BaseAppDataSerpElementItem.md) | found reviews you can get more results by using the depth parameter when setting a task | [optional] 

## Example

```python
from dataforseo_client.models.app_data_google_app_reviews_task_get_advanced_result_info import AppDataGoogleAppReviewsTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataGoogleAppReviewsTaskGetAdvancedResultInfo from a JSON string
app_data_google_app_reviews_task_get_advanced_result_info_instance = AppDataGoogleAppReviewsTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataGoogleAppReviewsTaskGetAdvancedResultInfo.to_json())

# convert the object into a dict
app_data_google_app_reviews_task_get_advanced_result_info_dict = app_data_google_app_reviews_task_get_advanced_result_info_instance.to_dict()
# create an instance of AppDataGoogleAppReviewsTaskGetAdvancedResultInfo from a dict
app_data_google_app_reviews_task_get_advanced_result_info_form_dict = app_data_google_app_reviews_task_get_advanced_result_info.from_dict(app_data_google_app_reviews_task_get_advanced_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



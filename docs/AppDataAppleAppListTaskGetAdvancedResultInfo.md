# AppDataAppleAppListTaskGetAdvancedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | app collection received in a POST array | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results in this case, the value will be null | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**se_results_count** | **int** | the total number of results | [optional] 
**items_count** | **int** | the number of app items in the results array you can get more results by using the depth parameter when setting a task | [optional] 
**items** | [**List[BaseAppDataSerpElementItem]**](BaseAppDataSerpElementItem.md) | found apps you can get more results by using the depth parameter when setting a task | [optional] 

## Example

```python
from dataforseo_client.models.app_data_apple_app_list_task_get_advanced_result_info import AppDataAppleAppListTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataAppleAppListTaskGetAdvancedResultInfo from a JSON string
app_data_apple_app_list_task_get_advanced_result_info_instance = AppDataAppleAppListTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataAppleAppListTaskGetAdvancedResultInfo.to_json())

# convert the object into a dict
app_data_apple_app_list_task_get_advanced_result_info_dict = app_data_apple_app_list_task_get_advanced_result_info_instance.to_dict()
# create an instance of AppDataAppleAppListTaskGetAdvancedResultInfo from a dict
app_data_apple_app_list_task_get_advanced_result_info_form_dict = app_data_apple_app_list_task_get_advanced_result_info.from_dict(app_data_apple_app_list_task_get_advanced_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



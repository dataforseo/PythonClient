[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppDataAppleAppInfoTaskGetAdvancedResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | application id received in a POST request | [optional]
**se_domain** | **str** | search engine domain in a POST array | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional]
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**se_results_count** | **int** | the total number of results | [optional]
**items_count** | **int** | the number of items in the results array | [optional]
**items** | [**List[BaseAppDataSerpElementItem]**](BaseAppDataSerpElementItem.md) | found app info | [optional]

## Example

```python
from dataforseo_client.models.app_data_apple_app_info_task_get_advanced_result_info import AppDataAppleAppInfoTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataAppleAppInfoTaskGetAdvancedResultInfo from a JSON string
app_data_apple_app_info_task_get_advanced_result_info_instance = AppDataAppleAppInfoTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print AppDataAppleAppInfoTaskGetAdvancedResultInfo.to_json()

# convert the object into a dict
app_data_apple_app_info_task_get_advanced_result_info_dict = app_data_apple_app_info_task_get_advanced_result_info_instance.to_dict()
# create an instance of AppDataAppleAppInfoTaskGetAdvancedResultInfo from a dict
app_data_apple_app_info_task_get_advanced_result_info_form_dict = app_data_apple_app_info_task_get_advanced_result_info.from_dict(app_data_apple_app_info_task_get_advanced_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
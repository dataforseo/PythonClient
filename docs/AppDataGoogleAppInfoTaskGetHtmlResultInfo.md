# AppDataGoogleAppInfoTaskGetHtmlResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | application ID received in a POST request | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[HtmlItem]**](HtmlItem.md) | HTML pages and related data | [optional] 

## Example

```python
from dataforseo_client.models.app_data_google_app_info_task_get_html_result_info import AppDataGoogleAppInfoTaskGetHtmlResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataGoogleAppInfoTaskGetHtmlResultInfo from a JSON string
app_data_google_app_info_task_get_html_result_info_instance = AppDataGoogleAppInfoTaskGetHtmlResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataGoogleAppInfoTaskGetHtmlResultInfo.to_json())

# convert the object into a dict
app_data_google_app_info_task_get_html_result_info_dict = app_data_google_app_info_task_get_html_result_info_instance.to_dict()
# create an instance of AppDataGoogleAppInfoTaskGetHtmlResultInfo from a dict
app_data_google_app_info_task_get_html_result_info_from_dict = AppDataGoogleAppInfoTaskGetHtmlResultInfo.from_dict(app_data_google_app_info_task_get_html_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



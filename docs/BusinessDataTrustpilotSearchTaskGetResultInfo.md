# BusinessDataTrustpilotSearchTaskGetResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword in a POST array | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**items_count** | **int** | the number of items in the results array you can get more results by using the depth parameter when setting a task | [optional] 
**items** | [**List[BaseBusinessDataSerpElementItem]**](BaseBusinessDataSerpElementItem.md) | found reviews you can get more results by using the depth parameter when setting a task | [optional] 

## Example

```python
from dataforseo_client.models.business_data_trustpilot_search_task_get_result_info import BusinessDataTrustpilotSearchTaskGetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataTrustpilotSearchTaskGetResultInfo from a JSON string
business_data_trustpilot_search_task_get_result_info_instance = BusinessDataTrustpilotSearchTaskGetResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataTrustpilotSearchTaskGetResultInfo.to_json())

# convert the object into a dict
business_data_trustpilot_search_task_get_result_info_dict = business_data_trustpilot_search_task_get_result_info_instance.to_dict()
# create an instance of BusinessDataTrustpilotSearchTaskGetResultInfo from a dict
business_data_trustpilot_search_task_get_result_info_form_dict = business_data_trustpilot_search_task_get_result_info.from_dict(business_data_trustpilot_search_task_get_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



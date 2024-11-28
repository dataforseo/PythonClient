# BusinessDataTripadvisorSearchTaskGetResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array this field will contain the alias parameter if it was specified in a POST array | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **str** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to Tripadvisor results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**item_types** | **List[Optional[str]]** | item types encountered in the result possible item types: tripadvisor_search_organic | [optional] 
**se_results_count** | **int** | the total number of results | [optional] 
**items_count** | **int** | the number of items in the results array you can get more results by using the depth parameter when setting a task | [optional] 
**items** | [**List[BaseBusinessDataSerpElementItem]**](BaseBusinessDataSerpElementItem.md) | Tripadvisor search listing results you can get more results by using the depth parameter when setting a task | [optional] 

## Example

```python
from dataforseo_client.models.business_data_tripadvisor_search_task_get_result_info import BusinessDataTripadvisorSearchTaskGetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataTripadvisorSearchTaskGetResultInfo from a JSON string
business_data_tripadvisor_search_task_get_result_info_instance = BusinessDataTripadvisorSearchTaskGetResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataTripadvisorSearchTaskGetResultInfo.to_json())

# convert the object into a dict
business_data_tripadvisor_search_task_get_result_info_dict = business_data_tripadvisor_search_task_get_result_info_instance.to_dict()
# create an instance of BusinessDataTripadvisorSearchTaskGetResultInfo from a dict
business_data_tripadvisor_search_task_get_result_info_from_dict = BusinessDataTripadvisorSearchTaskGetResultInfo.from_dict(business_data_tripadvisor_search_task_get_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BusinessDataGoogleMyBusinessUpdatesTaskGetResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) this field will contain the cid parameter if you specified it in the keyword field when setting a task; example: cid:2946633002421908862 learn more about the parameter in this help center article | [optional] 
**se_domain** | **str** | search engine domain as specified in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**business_updates_id** | **str** | identifier of the business updates element in SERP | [optional] 
**cid** | **str** | google-defined client id unique id of a local establishment learn more about the cid identifier in this help center article | [optional] 
**feature_id** | **str** | the unique identifier of the element in SERP learn more about the identifier in this help center article | [optional] 
**item_types** | **List[Optional[str]]** | item types types of search engine results encountered in the items array; possible item types: google_business_post | [optional] 
**items_count** | **int** | item types the number of items in the items array | [optional] 
**items** | [**List[BaseBusinessDataSerpElementItem]**](BaseBusinessDataSerpElementItem.md) | encountered item types types of search engine results encountered in the items array; possible item types: google_business_info | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_my_business_updates_task_get_result_info import BusinessDataGoogleMyBusinessUpdatesTaskGetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleMyBusinessUpdatesTaskGetResultInfo from a JSON string
business_data_google_my_business_updates_task_get_result_info_instance = BusinessDataGoogleMyBusinessUpdatesTaskGetResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataGoogleMyBusinessUpdatesTaskGetResultInfo.to_json())

# convert the object into a dict
business_data_google_my_business_updates_task_get_result_info_dict = business_data_google_my_business_updates_task_get_result_info_instance.to_dict()
# create an instance of BusinessDataGoogleMyBusinessUpdatesTaskGetResultInfo from a dict
business_data_google_my_business_updates_task_get_result_info_form_dict = business_data_google_my_business_updates_task_get_result_info.from_dict(business_data_google_my_business_updates_task_get_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



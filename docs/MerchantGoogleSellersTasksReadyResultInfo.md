# MerchantGoogleSellersTasksReadyResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional] 
**se** | **str** | search engine specified when setting the task | [optional] 
**se_type** | **str** | type of search engine can take the following values: shopping | [optional] 
**date_posted** | **str** | date when the task was posted (in the UTC format) | [optional] 
**tag** | **str** | user-defined task identifier | [optional] 
**endpoint_advanced** | **str** | URL for collecting the results of Google Shopping Sellers Advanced task | [optional] 
**endpoint_html** | **str** | URL for collecting the results of Google Shopping Sellers HTML task | [optional] 

## Example

```python
from dataforseo_client.models.merchant_google_sellers_tasks_ready_result_info import MerchantGoogleSellersTasksReadyResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGoogleSellersTasksReadyResultInfo from a JSON string
merchant_google_sellers_tasks_ready_result_info_instance = MerchantGoogleSellersTasksReadyResultInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantGoogleSellersTasksReadyResultInfo.to_json())

# convert the object into a dict
merchant_google_sellers_tasks_ready_result_info_dict = merchant_google_sellers_tasks_ready_result_info_instance.to_dict()
# create an instance of MerchantGoogleSellersTasksReadyResultInfo from a dict
merchant_google_sellers_tasks_ready_result_info_from_dict = MerchantGoogleSellersTasksReadyResultInfo.from_dict(merchant_google_sellers_tasks_ready_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MerchantAmazonProductsTasksReadyResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional] 
**se** | **str** | search engine specified when setting the task | [optional] 
**se_type** | **str** | type of search engine can take the following values: organic | [optional] 
**date_posted** | **str** | date when the task was posted (in the UTC format) | [optional] 
**tag** | **str** | user-defined task identifier | [optional] 
**endpoint_advanced** | **str** | URL for collecting the results of the Amazon Products Advanced task | [optional] 
**endpoint_html** | **str** | URL for collecting the results of the Amazon Products HTML task | [optional] 

## Example

```python
from dataforseo_client.models.merchant_amazon_products_tasks_ready_result_info import MerchantAmazonProductsTasksReadyResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAmazonProductsTasksReadyResultInfo from a JSON string
merchant_amazon_products_tasks_ready_result_info_instance = MerchantAmazonProductsTasksReadyResultInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantAmazonProductsTasksReadyResultInfo.to_json())

# convert the object into a dict
merchant_amazon_products_tasks_ready_result_info_dict = merchant_amazon_products_tasks_ready_result_info_instance.to_dict()
# create an instance of MerchantAmazonProductsTasksReadyResultInfo from a dict
merchant_amazon_products_tasks_ready_result_info_from_dict = MerchantAmazonProductsTasksReadyResultInfo.from_dict(merchant_amazon_products_tasks_ready_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



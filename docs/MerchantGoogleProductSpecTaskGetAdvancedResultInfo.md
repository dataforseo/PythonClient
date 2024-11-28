# MerchantGoogleProductSpecTaskGetAdvancedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | product ID in a POST array learn more about the parameter in this help center guide | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**title** | **str** | title of the product | [optional] 
**description** | **str** | description of the product | [optional] 
**image_url** | **str** | URL of the product image | [optional] 
**tags** | **List[Optional[str]]** | tags of the product | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the format: “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**item_types** | **List[Optional[str]]** | types of items found on the product specification page possible item types: shopping_specification | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BaseMerchantSerpElementItem]**](BaseMerchantSerpElementItem.md) | items on the product specification page contains all product attributes and related data listed on the product specification page | [optional] 

## Example

```python
from dataforseo_client.models.merchant_google_product_spec_task_get_advanced_result_info import MerchantGoogleProductSpecTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGoogleProductSpecTaskGetAdvancedResultInfo from a JSON string
merchant_google_product_spec_task_get_advanced_result_info_instance = MerchantGoogleProductSpecTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantGoogleProductSpecTaskGetAdvancedResultInfo.to_json())

# convert the object into a dict
merchant_google_product_spec_task_get_advanced_result_info_dict = merchant_google_product_spec_task_get_advanced_result_info_instance.to_dict()
# create an instance of MerchantGoogleProductSpecTaskGetAdvancedResultInfo from a dict
merchant_google_product_spec_task_get_advanced_result_info_from_dict = MerchantGoogleProductSpecTaskGetAdvancedResultInfo.from_dict(merchant_google_product_spec_task_get_advanced_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



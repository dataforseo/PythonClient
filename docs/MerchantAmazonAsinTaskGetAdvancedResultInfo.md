# MerchantAmazonAsinTaskGetAdvancedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | ASIN received in a POST array the unique product identifier in Amazon (ASIN) received in a POST array learn more about the identified in this help center guide | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | Amazon domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to Amazon results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**item_types** | **List[Optional[str]]** | types of search results found on Amazon contains types of all search results (items) found in the returned SERP possible item types: amazon_product_info | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BaseAmazonSerpElementItem]**](BaseAmazonSerpElementItem.md) | Amazon product info items | [optional] 

## Example

```python
from dataforseo_client.models.merchant_amazon_asin_task_get_advanced_result_info import MerchantAmazonAsinTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAmazonAsinTaskGetAdvancedResultInfo from a JSON string
merchant_amazon_asin_task_get_advanced_result_info_instance = MerchantAmazonAsinTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantAmazonAsinTaskGetAdvancedResultInfo.to_json())

# convert the object into a dict
merchant_amazon_asin_task_get_advanced_result_info_dict = merchant_amazon_asin_task_get_advanced_result_info_instance.to_dict()
# create an instance of MerchantAmazonAsinTaskGetAdvancedResultInfo from a dict
merchant_amazon_asin_task_get_advanced_result_info_form_dict = merchant_amazon_asin_task_get_advanced_result_info.from_dict(merchant_amazon_asin_task_get_advanced_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



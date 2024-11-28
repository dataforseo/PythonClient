# MerchantAmazonSellersTaskGetAdvancedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | asin received in a POST array learn more about ASINs in this help center guide | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain received in a POST array | [optional] 
**location_code** | **int** | location code received in a POST array | [optional] 
**language_code** | **str** | language code received in a POST array | [optional] 
**check_url** | **str** | direct URL to Amazon results you can use it to make sure the provided results are accurate | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**title** | **str** | product title title of the product relevant to the asin received in a POST array | [optional] 
**image** | **str** | product image url image URL of the product relevant to the asin received in a POST array | [optional] 
**item_types** | **List[Optional[str]]** | types of search results found in Amazon Sellers SERP contains types of all search results (items) found in the returned SERP possible item types: amazon_seller_main_item, amazon_seller_item | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BaseAmazonSerpElementItem]**](BaseAmazonSerpElementItem.md) | items in SERP | [optional] 

## Example

```python
from dataforseo_client.models.merchant_amazon_sellers_task_get_advanced_result_info import MerchantAmazonSellersTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAmazonSellersTaskGetAdvancedResultInfo from a JSON string
merchant_amazon_sellers_task_get_advanced_result_info_instance = MerchantAmazonSellersTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantAmazonSellersTaskGetAdvancedResultInfo.to_json())

# convert the object into a dict
merchant_amazon_sellers_task_get_advanced_result_info_dict = merchant_amazon_sellers_task_get_advanced_result_info_instance.to_dict()
# create an instance of MerchantAmazonSellersTaskGetAdvancedResultInfo from a dict
merchant_amazon_sellers_task_get_advanced_result_info_from_dict = MerchantAmazonSellersTaskGetAdvancedResultInfo.from_dict(merchant_amazon_sellers_task_get_advanced_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



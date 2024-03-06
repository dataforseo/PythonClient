[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# MerchantAmazonProductsTaskGetAdvancedResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) | [optional]
**type** | **str** | type of element | [optional]
**se_domain** | **str** | search engine domain in a POST array | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**check_url** | **str** | direct URL to Amazon results you can use it to make sure that we provided accurate results | [optional]
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**spell** | [**SpellInfo**](SpellInfo.md) |  | [optional]
**item_types** | **List[Optional[str]]** | types of search results found in Amazon SERP contains types of all search results (items) found in the returned SERP possible item types: amazon_serp, amazon_paid, editorial_recommendations, top_rated_from_our_brands, related_searches | [optional]
**se_results_count** | **int** | search engine results count | [optional]
**categories** | **List[Optional[str]]** | amazon product departments and subcategories | [optional]
**items_count** | **int** | the number of results returned in the items array | [optional]
**items** | [**List[BaseAmazonSerpElementItem]**](BaseAmazonSerpElementItem.md) | Amazon product items within the editorial_recommendations element | [optional]

## Example

```python
from dataforseo_client.models.merchant_amazon_products_task_get_advanced_result_info import MerchantAmazonProductsTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAmazonProductsTaskGetAdvancedResultInfo from a JSON string
merchant_amazon_products_task_get_advanced_result_info_instance = MerchantAmazonProductsTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print MerchantAmazonProductsTaskGetAdvancedResultInfo.to_json()

# convert the object into a dict
merchant_amazon_products_task_get_advanced_result_info_dict = merchant_amazon_products_task_get_advanced_result_info_instance.to_dict()
# create an instance of MerchantAmazonProductsTaskGetAdvancedResultInfo from a dict
merchant_amazon_products_task_get_advanced_result_info_form_dict = merchant_amazon_products_task_get_advanced_result_info.from_dict(merchant_amazon_products_task_get_advanced_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# MerchantGoogleSellersTaskGetAdvancedResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | product_id received in a POST array learn more about the parameter in this help center guide | [optional]
**type** | **str** | type of element | [optional]
**se_domain** | **str** | search engine domain in a POST array | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**check_url** | **str** | direct URL to Google Shopping results you can use it to make sure that we provided accurate results | [optional]
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**item_types** | **List[Optional[str]]** | types of search results found in Google Shopping SERP contains types of all search results (items) found in the returned SERP possible item types: shops_list, buy_on_google | [optional]
**items_count** | **int** | the number of results returned in the items array | [optional]
**items** | [**List[BaseMerchantSerpElementItem]**](BaseMerchantSerpElementItem.md) | items in SERP | [optional]

## Example

```python
from dataforseo_client.models.merchant_google_sellers_task_get_advanced_result_info import MerchantGoogleSellersTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGoogleSellersTaskGetAdvancedResultInfo from a JSON string
merchant_google_sellers_task_get_advanced_result_info_instance = MerchantGoogleSellersTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print MerchantGoogleSellersTaskGetAdvancedResultInfo.to_json()

# convert the object into a dict
merchant_google_sellers_task_get_advanced_result_info_dict = merchant_google_sellers_task_get_advanced_result_info_instance.to_dict()
# create an instance of MerchantGoogleSellersTaskGetAdvancedResultInfo from a dict
merchant_google_sellers_task_get_advanced_result_info_form_dict = merchant_google_sellers_task_get_advanced_result_info.from_dict(merchant_google_sellers_task_get_advanced_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
# MerchantAmazonAsinTaskGetHtmlResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | ASIN received in a POST array | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[HtmlItem]**](HtmlItem.md) | HTML pages and related data | [optional] 

## Example

```python
from dataforseo_client.models.merchant_amazon_asin_task_get_html_result_info import MerchantAmazonAsinTaskGetHtmlResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAmazonAsinTaskGetHtmlResultInfo from a JSON string
merchant_amazon_asin_task_get_html_result_info_instance = MerchantAmazonAsinTaskGetHtmlResultInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantAmazonAsinTaskGetHtmlResultInfo.to_json())

# convert the object into a dict
merchant_amazon_asin_task_get_html_result_info_dict = merchant_amazon_asin_task_get_html_result_info_instance.to_dict()
# create an instance of MerchantAmazonAsinTaskGetHtmlResultInfo from a dict
merchant_amazon_asin_task_get_html_result_info_from_dict = MerchantAmazonAsinTaskGetHtmlResultInfo.from_dict(merchant_amazon_asin_task_get_html_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



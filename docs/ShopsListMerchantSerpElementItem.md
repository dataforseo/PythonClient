# ShopsListMerchantSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements found in Google Shopping SERP | [optional] 
**position** | **str** | the alignment of the element in Google Shopping SERP possible values: left, right | [optional] 
**xpath** | **str** | XPath of the element | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**title** | **str** | product title | [optional] 
**url** | **str** | Google Shopping URL forwarding to the product page on the seller’s website if you want to obtain a URL of the advertisement forwarding to the product page on the seller’s website, please refer to the Google Shopping Sellers Ad URL endpoint | [optional] 
**details** | **str** | details and special offers if there are no details, the value will be null | [optional] 
**base_price** | **int** | product price without tax and shipping | [optional] 
**tax** | **int** | the amount of tax tax is specified as the actual amount of money, not as the percentage | [optional] 
**shipping_price** | **int** | product shipping price | [optional] 
**total_price** | **int** | product price including tax and shipping | [optional] 
**currency** | **str** | currency in the ISO format example: USD | [optional] 
**seller_name** | **str** | name of the seller the name of the company that placed a corresponding product on Google Shopping | [optional] 
**rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**shop_ad_aclk** | **str** | unique ad click referral parameter using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL | [optional] 
**product_condition** | **str** | indicated condition of the product possible values: Used, Refurbished, New, null | [optional] 
**product_annotation** | **str** | data from annotations and badges with special offers if there is no annotation for this product, the value will be null examples: LOW PRICE, SPECIAL OFFER, SALE, PRICE DROP | [optional] 

## Example

```python
from dataforseo_client.models.shops_list_merchant_serp_element_item import ShopsListMerchantSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShopsListMerchantSerpElementItem from a JSON string
shops_list_merchant_serp_element_item_instance = ShopsListMerchantSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(ShopsListMerchantSerpElementItem.to_json())

# convert the object into a dict
shops_list_merchant_serp_element_item_dict = shops_list_merchant_serp_element_item_instance.to_dict()
# create an instance of ShopsListMerchantSerpElementItem from a dict
shops_list_merchant_serp_element_item_form_dict = shops_list_merchant_serp_element_item.from_dict(shops_list_merchant_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



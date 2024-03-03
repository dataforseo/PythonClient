# BuyOnGoogleMerchantSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements found in Google Shopping SERP | [optional] 
**position** | **str** | the alignment of the element in Google Shopping SERP possible values: left, right | [optional] 
**xpath** | **str** | XPath of the element | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**title** | **str** | product title | [optional] 
**url** | **str** | Google Shopping URL forwarding to the product page | [optional] 
**details** | **str** | details and special offers if there are no details, the value will be null | [optional] 
**base_price** | **int** | product price without tax and shipping | [optional] 
**tax** | **int** | the amount of tax tax is specified as the actual amount of money, not as the percentage | [optional] 
**shipping_price** | **int** | product shipping price | [optional] 
**total_price** | **int** | product price including tax and shipping | [optional] 
**currency** | **str** | currency in the ISO format example: USD | [optional] 
**seller_name** | **str** | name of the seller the name of the company that placed a corresponding product on Google Shopping | [optional] 
**rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**shop_ad_aclk** | **str** | unique ad click referral parameter using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL in this case, the value equals null | [optional] 
**product_condition** | **str** | indicated condition of the product possible values: Used, Refurbished, New, null | [optional] 

## Example

```python
from dataforseo_client.models.buy_on_google_merchant_serp_element_item import BuyOnGoogleMerchantSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of BuyOnGoogleMerchantSerpElementItem from a JSON string
buy_on_google_merchant_serp_element_item_instance = BuyOnGoogleMerchantSerpElementItem.from_json(json)
# print the JSON string representation of the object
print BuyOnGoogleMerchantSerpElementItem.to_json()

# convert the object into a dict
buy_on_google_merchant_serp_element_item_dict = buy_on_google_merchant_serp_element_item_instance.to_dict()
# create an instance of BuyOnGoogleMerchantSerpElementItem from a dict
buy_on_google_merchant_serp_element_item_form_dict = buy_on_google_merchant_serp_element_item.from_dict(buy_on_google_merchant_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



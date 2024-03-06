[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# GoogleShoppingPaidMerchantSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements found in Google Shopping SERP | [optional]
**position** | **str** | alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | XPath of the element | [optional]
**domain** | **str** | domain in SERP | [optional]
**title** | **str** | product title | [optional]
**description** | **str** | description of the product in Google Shopping SERP | [optional]
**url** | **str** | URL to the product page on the seller’s website | [optional]
**shop_ad_aclk** | **str** | unique ad click referral parameter using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL | [optional]

## Example

```python
from dataforseo_client.models.google_shopping_paid_merchant_serp_element_item import GoogleShoppingPaidMerchantSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleShoppingPaidMerchantSerpElementItem from a JSON string
google_shopping_paid_merchant_serp_element_item_instance = GoogleShoppingPaidMerchantSerpElementItem.from_json(json)
# print the JSON string representation of the object
print GoogleShoppingPaidMerchantSerpElementItem.to_json()

# convert the object into a dict
google_shopping_paid_merchant_serp_element_item_dict = google_shopping_paid_merchant_serp_element_item_instance.to_dict()
# create an instance of GoogleShoppingPaidMerchantSerpElementItem from a dict
google_shopping_paid_merchant_serp_element_item_form_dict = google_shopping_paid_merchant_serp_element_item.from_dict(google_shopping_paid_merchant_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
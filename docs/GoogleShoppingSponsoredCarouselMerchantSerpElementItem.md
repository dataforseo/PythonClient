[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# GoogleShoppingSponsoredCarouselMerchantSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements found in Google Shopping SERP | [optional]
**position** | **str** | alignment of the element in Google Shopping SERP possible values: left, right | [optional]
**xpath** | **str** | XPath of the element | [optional]
**title** | **str** | product title | [optional]
**items** | [**List[GoogleShoppingSponsoredCarouselElement]**](GoogleShoppingSponsoredCarouselElement.md) | items in SERP | [optional]

## Example

```python
from dataforseo_client.models.google_shopping_sponsored_carousel_merchant_serp_element_item import GoogleShoppingSponsoredCarouselMerchantSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleShoppingSponsoredCarouselMerchantSerpElementItem from a JSON string
google_shopping_sponsored_carousel_merchant_serp_element_item_instance = GoogleShoppingSponsoredCarouselMerchantSerpElementItem.from_json(json)
# print the JSON string representation of the object
print GoogleShoppingSponsoredCarouselMerchantSerpElementItem.to_json()

# convert the object into a dict
google_shopping_sponsored_carousel_merchant_serp_element_item_dict = google_shopping_sponsored_carousel_merchant_serp_element_item_instance.to_dict()
# create an instance of GoogleShoppingSponsoredCarouselMerchantSerpElementItem from a dict
google_shopping_sponsored_carousel_merchant_serp_element_item_form_dict = google_shopping_sponsored_carousel_merchant_serp_element_item.from_dict(google_shopping_sponsored_carousel_merchant_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
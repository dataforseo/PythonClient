# GoogleShoppingSponsoredCarouselMerchantSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
print(GoogleShoppingSponsoredCarouselMerchantSerpElementItem.to_json())

# convert the object into a dict
google_shopping_sponsored_carousel_merchant_serp_element_item_dict = google_shopping_sponsored_carousel_merchant_serp_element_item_instance.to_dict()
# create an instance of GoogleShoppingSponsoredCarouselMerchantSerpElementItem from a dict
google_shopping_sponsored_carousel_merchant_serp_element_item_from_dict = GoogleShoppingSponsoredCarouselMerchantSerpElementItem.from_dict(google_shopping_sponsored_carousel_merchant_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GoogleShoppingSponsoredCarouselElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**xpath** | **str** | XPath of the element | [optional] 
**title** | **str** | product title | [optional] 
**tags** | **List[Optional[str]]** | tags assigned to the product | [optional] 
**seller** | **str** | name of the seller the name of the company that placed a corresponding product on Google Shopping | [optional] 
**price** | **float** | product price example: 384.99 | [optional] 
**currency** | **str** | currency in the ISO format example: USD | [optional] 
**product_rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**product_images** | **List[Optional[str]]** | URLs to the images of the product the first URL in the array is the featured image of the product | [optional] 
**shop_ad_aclk** | **str** | unique ad click referral parameter using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL | [optional] 
**delivery_info** | [**DeliveryInfo**](DeliveryInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_shopping_sponsored_carousel_element import GoogleShoppingSponsoredCarouselElement

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleShoppingSponsoredCarouselElement from a JSON string
google_shopping_sponsored_carousel_element_instance = GoogleShoppingSponsoredCarouselElement.from_json(json)
# print the JSON string representation of the object
print GoogleShoppingSponsoredCarouselElement.to_json()

# convert the object into a dict
google_shopping_sponsored_carousel_element_dict = google_shopping_sponsored_carousel_element_instance.to_dict()
# create an instance of GoogleShoppingSponsoredCarouselElement from a dict
google_shopping_sponsored_carousel_element_form_dict = google_shopping_sponsored_carousel_element.from_dict(google_shopping_sponsored_carousel_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



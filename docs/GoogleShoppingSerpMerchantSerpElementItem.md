# GoogleShoppingSerpMerchantSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements found in Google Shopping SERP | [optional] 
**position** | **str** | alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | XPath of the element | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**title** | **str** | title of the element | [optional] 
**description** | **str** | description of the product in Google Shopping SERP | [optional] 
**url** | **str** | URL to the product page on the seller’s website | [optional] 
**shopping_url** | **str** | URL to the product page on Google Shopping | [optional] 
**tags** | **List[Optional[str]]** | tags assigned to the product | [optional] 
**price** | **float** | product price example: 384.99 | [optional] 
**old_price** | **float** | product old price displayed if the product price has been changed example: 499 | [optional] 
**currency** | **str** | currency in the ISO format example: USD | [optional] 
**product_id** | **str** | unique product identifier on Google Shopping note that there is no full list of possible values as the product_id is a dynamic value assigned by Google if there are no values, you will get null example: 4485466949985702538 learn more about the parameter in this help center guide | [optional] 
**data_docid** | **str** | unique identifier of the SERP data element note that there is no full list of possible values as the data_docid is a dynamic value assigned by Google example: 17363035694596624076 | [optional] 
**seller** | **str** | name of the seller the name of the company that placed a corresponding product on Google Shopping | [optional] 
**additional_specifications** | **Dict[str, Optional[str]]** | object containing additional url parameters you can get more details about the product by using this object in the POST request to the Google Shopping Product Specification and Google Shopping Sellers endpoint | [optional] 
**reviews_count** | **int** | number of product reviews indicates the number of reviews left by users on Google Shopping if there are no values, you will get null | [optional] 
**is_best_match** | **bool** | “best match” label if the value is true, the product is marked with the “best match” label if there are no values, you will get null | [optional] 
**product_rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**shop_rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**product_images** | **List[Optional[str]]** | URLs to the images of the product the first URL in the array is the featured image of the product | [optional] 
**shop_ad_aclk** | **str** | unique ad click referral parameter using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL | [optional] 
**delivery_info** | [**DeliveryInfo**](DeliveryInfo.md) |  | [optional] 
**stores_count_info** | [**StoresCountInfo**](StoresCountInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_shopping_serp_merchant_serp_element_item import GoogleShoppingSerpMerchantSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleShoppingSerpMerchantSerpElementItem from a JSON string
google_shopping_serp_merchant_serp_element_item_instance = GoogleShoppingSerpMerchantSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleShoppingSerpMerchantSerpElementItem.to_json())

# convert the object into a dict
google_shopping_serp_merchant_serp_element_item_dict = google_shopping_serp_merchant_serp_element_item_instance.to_dict()
# create an instance of GoogleShoppingSerpMerchantSerpElementItem from a dict
google_shopping_serp_merchant_serp_element_item_form_dict = google_shopping_serp_merchant_serp_element_item.from_dict(google_shopping_serp_merchant_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AmazonSerpElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**domain** | **str** | Amazon domain | [optional] 
**title** | **str** | product title | [optional] 
**url** | **str** | the URL of the product page | [optional] 
**image_url** | **str** | URL of the product image featured in the results | [optional] 
**bought_past_month** | **int** | number of product purchases in the past month | [optional] 
**price_from** | **float** | the regular price of a product example: 49.98 | [optional] 
**price_to** | **float** | the upper limit of the product price range example: 384.99 | [optional] 
**currency** | **str** | currency in the ISO format example: USD | [optional] 
**special_offers** | **List[Optional[str]]** | special offer details contains special offer details, including coupon and Subscribe &amp; Save discounts | [optional] 
**data_asin** | **str** | unique product identifier on Amazon note that there is no full list of possible values as the data_asin is a dynamic value assigned by Amazon example: B07G82D89J | [optional] 
**rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**is_amazon_choice** | **bool** | “Amazon’s choice” label if the value is true, the product is marked with the “Amazon’s choice” label | [optional] 
**is_best_seller** | **bool** | “Best Seller” label if the value is true, the product is marked with the “Best Seller” label | [optional] 
**delivery_info** | [**AmazonDeliveryInfo**](AmazonDeliveryInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.amazon_serp_element import AmazonSerpElement

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonSerpElement from a JSON string
amazon_serp_element_instance = AmazonSerpElement.from_json(json)
# print the JSON string representation of the object
print(AmazonSerpElement.to_json())

# convert the object into a dict
amazon_serp_element_dict = amazon_serp_element_instance.to_dict()
# create an instance of AmazonSerpElement from a dict
amazon_serp_element_from_dict = AmazonSerpElement.from_dict(amazon_serp_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



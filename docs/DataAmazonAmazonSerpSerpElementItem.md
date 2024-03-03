# DataAmazonAmazonSerpSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in Amazon SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in Amazon SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**domain** | **str** | Amazon domain | [optional] 
**title** | **str** | product title | [optional] 
**url** | **str** | URL of the product page | [optional] 
**description** | **str** | description of the product | [optional] 
**asin** | **str** | ASIN of the product learn more about ASIN in this help center guide | [optional] 
**image_url** | **str** | URL of the product image featured in the results | [optional] 
**price_from** | **float** | the regular price of a product example: 49.98 | [optional] 
**price_to** | **float** | the upper limit of the product price range example: 384.99 | [optional] 
**currency** | **str** | currency in the ISO format example: USD | [optional] 
**special_offers** | **List[Optional[str]]** | special offer details contains special offer details, including coupon and Subscribe &amp; Save discounts | [optional] 
**is_best_seller** | **bool** | “Best Seller” label if the value is true, the product is marked with the “Best Seller” label | [optional] 
**is_amazon_choice** | **bool** | “Amazon’s choice” label if the value is true, the product is marked with the “Amazon’s choice” label | [optional] 
**rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**delivery_info** | [**AmazonDeliveryInfo**](AmazonDeliveryInfo.md) |  | [optional] 
**bought_past_month** | **int** | number of product purchases in the past month | [optional] 
**data_asin** | **str** | unique product identifier on Amazon note that there is no full list of possible values as the data_asin is a dynamic value assigned by Amazon example: B07G82D89J | [optional] 

## Example

```python
from dataforseo_client.models.data_amazon_amazon_serp_serp_element_item import DataAmazonAmazonSerpSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAmazonAmazonSerpSerpElementItem from a JSON string
data_amazon_amazon_serp_serp_element_item_instance = DataAmazonAmazonSerpSerpElementItem.from_json(json)
# print the JSON string representation of the object
print DataAmazonAmazonSerpSerpElementItem.to_json()

# convert the object into a dict
data_amazon_amazon_serp_serp_element_item_dict = data_amazon_amazon_serp_serp_element_item_instance.to_dict()
# create an instance of DataAmazonAmazonSerpSerpElementItem from a dict
data_amazon_amazon_serp_serp_element_item_form_dict = data_amazon_amazon_serp_serp_element_item.from_dict(data_amazon_amazon_serp_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ProductInfoElementMerchantSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank on the product specification page absolute position among all the elements found on the product specification page | [optional] 
**position** | **str** | alignment of the element on the product specification page can take the following values: right, left | [optional] 
**product_id** | **str** | product_id received in a POST array ilearn more about the parameter in this help center guide | [optional] 
**title** | **str** | title of the product | [optional] 
**description** | **str** | description of the product | [optional] 
**url** | **str** | product url url of the product on Google Shopping | [optional] 
**images** | **List[Optional[str]]** | product images contains urls to product images | [optional] 
**features** | **List[Optional[str]]** | product features contains snippets with the description of product features | [optional] 
**rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**seller_reviews_count** | **int** | number of seller reviews number of reviews on the product seller’s account | [optional] 
**sellers** | [**List[ProductSeller]**](ProductSeller.md) | sellers of the product number of reviews on the product seller’s account | [optional] 
**variations** | [**List[ProductVariation]**](ProductVariation.md) | variations of the product contains brief information about different product variations | [optional] 

## Example

```python
from dataforseo_client.models.product_info_element_merchant_serp_element_item import ProductInfoElementMerchantSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInfoElementMerchantSerpElementItem from a JSON string
product_info_element_merchant_serp_element_item_instance = ProductInfoElementMerchantSerpElementItem.from_json(json)
# print the JSON string representation of the object
print ProductInfoElementMerchantSerpElementItem.to_json()

# convert the object into a dict
product_info_element_merchant_serp_element_item_dict = product_info_element_merchant_serp_element_item_instance.to_dict()
# create an instance of ProductInfoElementMerchantSerpElementItem from a dict
product_info_element_merchant_serp_element_item_form_dict = product_info_element_merchant_serp_element_item.from_dict(product_info_element_merchant_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



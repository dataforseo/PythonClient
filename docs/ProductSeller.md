# ProductSeller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | product title | [optional] 
**url** | **str** | seller url url of the page where the product is sold | [optional] 
**seller_rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**seller_review_count** | **int** | number of seller reviews number of reviews on the product seller’s account | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 
**delivery_info** | [**DeliveryInfo**](DeliveryInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.product_seller import ProductSeller

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSeller from a JSON string
product_seller_instance = ProductSeller.from_json(json)
# print the JSON string representation of the object
print(ProductSeller.to_json())

# convert the object into a dict
product_seller_dict = product_seller_instance.to_dict()
# create an instance of ProductSeller from a dict
product_seller_from_dict = ProductSeller.from_dict(product_seller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



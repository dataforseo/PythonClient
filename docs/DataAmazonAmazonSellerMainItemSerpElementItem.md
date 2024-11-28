# DataAmazonAmazonSellerMainItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | alignment of the element in SERP possible values: left, right | [optional] 
**seller_name** | **str** | business name of the seller | [optional] 
**seller_url** | **str** | url forwarding to the seller’s page on Amazon | [optional] 
**ships_from** | **str** | sender company name | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 
**rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**condition** | **str** | product condition condition of the product offered by the seller | [optional] 
**condition_description** | **str** | product condition details expanded details on the condition of the product offered by the seller | [optional] 
**delivery_info** | [**AmazonDeliveryInfo**](AmazonDeliveryInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.data_amazon_amazon_seller_main_item_serp_element_item import DataAmazonAmazonSellerMainItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAmazonAmazonSellerMainItemSerpElementItem from a JSON string
data_amazon_amazon_seller_main_item_serp_element_item_instance = DataAmazonAmazonSellerMainItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(DataAmazonAmazonSellerMainItemSerpElementItem.to_json())

# convert the object into a dict
data_amazon_amazon_seller_main_item_serp_element_item_dict = data_amazon_amazon_seller_main_item_serp_element_item_instance.to_dict()
# create an instance of DataAmazonAmazonSellerMainItemSerpElementItem from a dict
data_amazon_amazon_seller_main_item_serp_element_item_from_dict = DataAmazonAmazonSellerMainItemSerpElementItem.from_dict(data_amazon_amazon_seller_main_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



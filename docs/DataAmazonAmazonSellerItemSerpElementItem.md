[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataAmazonAmazonSellerItemSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements found in Amazon Sellers SERP | [optional]
**position** | **str** | alignment of the element in SERP possible values: left, right | [optional]
**xpath** | **str** | XPath of the element | [optional]
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
from dataforseo_client.models.data_amazon_amazon_seller_item_serp_element_item import DataAmazonAmazonSellerItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAmazonAmazonSellerItemSerpElementItem from a JSON string
data_amazon_amazon_seller_item_serp_element_item_instance = DataAmazonAmazonSellerItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print DataAmazonAmazonSellerItemSerpElementItem.to_json()

# convert the object into a dict
data_amazon_amazon_seller_item_serp_element_item_dict = data_amazon_amazon_seller_item_serp_element_item_instance.to_dict()
# create an instance of DataAmazonAmazonSellerItemSerpElementItem from a dict
data_amazon_amazon_seller_item_serp_element_item_form_dict = data_amazon_amazon_seller_item_serp_element_item.from_dict(data_amazon_amazon_seller_item_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
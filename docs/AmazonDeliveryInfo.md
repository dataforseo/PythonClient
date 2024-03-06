[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AmazonDeliveryInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_message** | **str** | message accompanying the delivery information as posted by the seller | [optional]
**delivery_date_from** | **str** | the earliest date when the product can be shipped | [optional]
**delivery_date_to** | **str** | the latest date when the product can be delivered | [optional]
**fastest_delivery_date_from** | **str** | the earliest date when the product can be delivered with a fast delivery option | [optional]
**fastest_delivery_date_to** | **str** | the latest date when the product can be delivered with a fast delivery option | [optional]
**delivery_price** | [**PriceInfo**](PriceInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.amazon_delivery_info import AmazonDeliveryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonDeliveryInfo from a JSON string
amazon_delivery_info_instance = AmazonDeliveryInfo.from_json(json)
# print the JSON string representation of the object
print AmazonDeliveryInfo.to_json()

# convert the object into a dict
amazon_delivery_info_dict = amazon_delivery_info_instance.to_dict()
# create an instance of AmazonDeliveryInfo from a dict
amazon_delivery_info_form_dict = amazon_delivery_info.from_dict(amazon_delivery_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
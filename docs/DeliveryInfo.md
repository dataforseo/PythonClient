[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DeliveryInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_message** | **str** | delivery information message accompanying the delivery information as posted by the seller | [optional]
**delivery_price** | [**PriceInfo**](PriceInfo.md) |  | [optional]
**stores_count_info** | [**StoresCountInfo**](StoresCountInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.delivery_info import DeliveryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryInfo from a JSON string
delivery_info_instance = DeliveryInfo.from_json(json)
# print the JSON string representation of the object
print DeliveryInfo.to_json()

# convert the object into a dict
delivery_info_dict = delivery_info_instance.to_dict()
# create an instance of DeliveryInfo from a dict
delivery_info_form_dict = delivery_info.from_dict(delivery_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
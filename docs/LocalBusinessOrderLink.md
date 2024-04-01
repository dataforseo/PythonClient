# LocalBusinessOrderLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_services** | [**List[LocalBusinessDeliveryServiceInfo]**](LocalBusinessDeliveryServiceInfo.md) | lists available delivery services | [optional] 

## Example

```python
from dataforseo_client.models.local_business_order_link import LocalBusinessOrderLink

# TODO update the JSON string below
json = "{}"
# create an instance of LocalBusinessOrderLink from a JSON string
local_business_order_link_instance = LocalBusinessOrderLink.from_json(json)
# print the JSON string representation of the object
print(LocalBusinessOrderLink.to_json())

# convert the object into a dict
local_business_order_link_dict = local_business_order_link_instance.to_dict()
# create an instance of LocalBusinessOrderLink from a dict
local_business_order_link_form_dict = local_business_order_link.from_dict(local_business_order_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



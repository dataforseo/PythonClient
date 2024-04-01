# LocalBusinessDeliveryServiceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the element domain of the online food ordering system | [optional] 
**url** | **str** | URL to place an order | [optional] 

## Example

```python
from dataforseo_client.models.local_business_delivery_service_info import LocalBusinessDeliveryServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LocalBusinessDeliveryServiceInfo from a JSON string
local_business_delivery_service_info_instance = LocalBusinessDeliveryServiceInfo.from_json(json)
# print the JSON string representation of the object
print(LocalBusinessDeliveryServiceInfo.to_json())

# convert the object into a dict
local_business_delivery_service_info_dict = local_business_delivery_service_info_instance.to_dict()
# create an instance of LocalBusinessDeliveryServiceInfo from a dict
local_business_delivery_service_info_form_dict = local_business_delivery_service_info.from_dict(local_business_delivery_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



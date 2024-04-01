# LocalBusinessReservationLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the element domain of the reservation software | [optional] 
**url** | **str** | URL to make a reservation | [optional] 

## Example

```python
from dataforseo_client.models.local_business_reservation_link import LocalBusinessReservationLink

# TODO update the JSON string below
json = "{}"
# create an instance of LocalBusinessReservationLink from a JSON string
local_business_reservation_link_instance = LocalBusinessReservationLink.from_json(json)
# print the JSON string representation of the object
print(LocalBusinessReservationLink.to_json())

# convert the object into a dict
local_business_reservation_link_dict = local_business_reservation_link_instance.to_dict()
# create an instance of LocalBusinessReservationLink from a dict
local_business_reservation_link_form_dict = local_business_reservation_link.from_dict(local_business_reservation_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



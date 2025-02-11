# HotelAmenityItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenity** | **str** | standardised amenity name | [optional] 
**amenity_label** | **str** | displayed amenity name | [optional] 
**hint** | **str** | standardised details about the amenity | [optional] 
**hint_label** | **str** | displayed details about the amenity | [optional] 
**is_available** | **bool** | indicates whether the amenity is available in the hotel | [optional] 

## Example

```python
from dataforseo_client.models.hotel_amenity_item_info import HotelAmenityItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HotelAmenityItemInfo from a JSON string
hotel_amenity_item_info_instance = HotelAmenityItemInfo.from_json(json)
# print the JSON string representation of the object
print(HotelAmenityItemInfo.to_json())

# convert the object into a dict
hotel_amenity_item_info_dict = hotel_amenity_item_info_instance.to_dict()
# create an instance of HotelAmenityItemInfo from a dict
hotel_amenity_item_info_from_dict = HotelAmenityItemInfo.from_dict(hotel_amenity_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



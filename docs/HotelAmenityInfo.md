[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# HotelAmenityInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | standardised category of the ammenity | [optional]
**category_label** | **str** | label of the category | [optional]
**items** | [**List[HotelAmenityItemInfo]**](HotelAmenityItemInfo.md) | specific amenities and details | [optional]

## Example

```python
from dataforseo_client.models.hotel_amenity_info import HotelAmenityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HotelAmenityInfo from a JSON string
hotel_amenity_info_instance = HotelAmenityInfo.from_json(json)
# print the JSON string representation of the object
print HotelAmenityInfo.to_json()

# convert the object into a dict
hotel_amenity_info_dict = hotel_amenity_info_instance.to_dict()
# create an instance of HotelAmenityInfo from a dict
hotel_amenity_info_form_dict = hotel_amenity_info.from_dict(hotel_amenity_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
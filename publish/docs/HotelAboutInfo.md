# HotelAboutInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description of the hotel the description of the hotel entity for which the results are collected | [optional] 
**sub_descriptions** | **List[Optional[str]]** | additional description of the hotel details about the hotel provided in addition to the description | [optional] 
**check_in_time** | [**WorkTimeInfo**](WorkTimeInfo.md) |  | [optional] 
**check_out_time** | [**WorkTimeInfo**](WorkTimeInfo.md) |  | [optional] 
**full_address** | **str** | full address of the hotel address of the hotel indicated in the standardised format | [optional] 
**domain** | **str** | hotel domain domain of the hotel’s website | [optional] 
**url** | **str** | hotel url URL to the hotel’s website indicated in the listing | [optional] 
**amenities** | [**List[HotelAmenityInfo]**](HotelAmenityInfo.md) | hotel amenities information about hotel amenities | [optional] 
**popular_amenities** | [**List[HotelAmenityItemInfo]**](HotelAmenityItemInfo.md) | hotel amenities information about hotel amenities labelled as “popular” | [optional] 

## Example

```python
from dataforseo_client.models.hotel_about_info import HotelAboutInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HotelAboutInfo from a JSON string
hotel_about_info_instance = HotelAboutInfo.from_json(json)
# print the JSON string representation of the object
print HotelAboutInfo.to_json()

# convert the object into a dict
hotel_about_info_dict = hotel_about_info_instance.to_dict()
# create an instance of HotelAboutInfo from a dict
hotel_about_info_form_dict = hotel_about_info.from_dict(hotel_about_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



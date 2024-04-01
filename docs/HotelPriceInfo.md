# HotelPriceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **int** | price per night | [optional] 
**price_without_discount** | **int** | full price per night without a discount applied | [optional] 
**currency** | **str** | price currency USD is applied by default, unless specified in the POST array | [optional] 
**discount_text** | **str** | text about a discount applied | [optional] 
**check_in** | **str** | check-in date and time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**check_out** | **str** | check-out date and time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**visitors** | **int** | number of hotel visitors for this price | [optional] 
**items** | [**List[HotelPriceItemInfo]**](HotelPriceItemInfo.md) | encountered item types types of search engine results encountered in the items array; possible item types: hotel_search_item | [optional] 

## Example

```python
from dataforseo_client.models.hotel_price_info import HotelPriceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HotelPriceInfo from a JSON string
hotel_price_info_instance = HotelPriceInfo.from_json(json)
# print the JSON string representation of the object
print(HotelPriceInfo.to_json())

# convert the object into a dict
hotel_price_info_dict = hotel_price_info_instance.to_dict()
# create an instance of HotelPriceInfo from a dict
hotel_price_info_form_dict = hotel_price_info.from_dict(hotel_price_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BusinessDataGoogleHotelSearchesItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**hotel_identifier** | **str** | unique identifier of a hotel entity in Google search example: CgoI-KWyzenM_MV3EAE | [optional] 
**title** | **str** | title of the hotel | [optional] 
**stars** | **int** | hotel class rating class rating that ranges between 1-5 stars | [optional] 
**is_paid** | **bool** | indicates a paid hotel listing if true, related hotel_search_item is a paid ad if false, related hotel_search_item is an organic hotel listing | [optional] 
**location** | [**GpsCoordinatesLocationInfo**](GpsCoordinatesLocationInfo.md) |  | [optional] 
**reviews** | [**HotelReviewInfo**](HotelReviewInfo.md) |  | [optional] 
**overview_images** | **List[Optional[str]]** | featured images for a hotel | [optional] 
**prices** | [**HotelPriceInfo**](HotelPriceInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_hotel_searches_item import BusinessDataGoogleHotelSearchesItem

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleHotelSearchesItem from a JSON string
business_data_google_hotel_searches_item_instance = BusinessDataGoogleHotelSearchesItem.from_json(json)
# print the JSON string representation of the object
print(BusinessDataGoogleHotelSearchesItem.to_json())

# convert the object into a dict
business_data_google_hotel_searches_item_dict = business_data_google_hotel_searches_item_instance.to_dict()
# create an instance of BusinessDataGoogleHotelSearchesItem from a dict
business_data_google_hotel_searches_item_from_dict = BusinessDataGoogleHotelSearchesItem.from_dict(business_data_google_hotel_searches_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BusinessDataGoogleHotelInfoLiveAdvancedResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | identifier received in a POST array this field will contain the hotel_identifier parameter specified when setting a task; example: CgoI-KWyzenM_MV3EAE | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional]
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**title** | **str** | hotel title the title of the hotel entity for which the results are collected | [optional]
**stars** | **int** | hotel class rating class rating that ranges between 1-5 stars and displayed after review ratings in hotel summary | [optional]
**stars_description** | **str** | hotel class rating class rating that ranges between 1-5 stars and displayed after review ratings in the hotel summary | [optional]
**address** | **str** | hotel address physical address of the hotel | [optional]
**phone** | **str** | hotel phone number contact phone number of the hotel | [optional]
**about** | [**HotelAboutInfo**](HotelAboutInfo.md) |  | [optional]
**location** | [**Location**](Location.md) |  | [optional]
**reviews** | [**HotelReviewInfo**](HotelReviewInfo.md) |  | [optional]
**overview_images** | **List[Optional[str]]** | images displayed in the hotel overview array containing URLs to images displayed in the hotel overview | [optional]
**prices** | [**HotelPriceInfo**](HotelPriceInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.business_data_google_hotel_info_live_advanced_result_info import BusinessDataGoogleHotelInfoLiveAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleHotelInfoLiveAdvancedResultInfo from a JSON string
business_data_google_hotel_info_live_advanced_result_info_instance = BusinessDataGoogleHotelInfoLiveAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataGoogleHotelInfoLiveAdvancedResultInfo.to_json()

# convert the object into a dict
business_data_google_hotel_info_live_advanced_result_info_dict = business_data_google_hotel_info_live_advanced_result_info_instance.to_dict()
# create an instance of BusinessDataGoogleHotelInfoLiveAdvancedResultInfo from a dict
business_data_google_hotel_info_live_advanced_result_info_form_dict = business_data_google_hotel_info_live_advanced_result_info.from_dict(business_data_google_hotel_info_live_advanced_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
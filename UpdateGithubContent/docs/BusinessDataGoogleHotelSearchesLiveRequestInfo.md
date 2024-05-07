# BusinessDataGoogleHotelSearchesLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword optional field the keyword you specify is used to search for the list of hotels; if you don’t use this field, we will return the list of hotels found in a specified location; you can specify up to 700 symbols in the keyword filed all %## will be decoded (plus symbol ‘+’ will be decoded to a space character) if you need to use the “%” symbol for your keyword, please specify it as “%25”; Note: in order to obtain accurate search results, the location name is appended to the keyword automatically | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations with location_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/locations example: London,England,United Kingdom Note: in order to obtain accurate search results, the location_name you specify will be automatically appended to the keyword | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/google/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude” format the maximum number of decimal digits for “latitude” and “longitude”: 7 Note: if the coordinates are used to set a location, the search will occur in the nearest settlement example: 53.476225,-2.243572 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages with language_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages example: en | [optional] 
**depth** | **int** | parsing depth optional field number of results in Google Hotels default value: 20 organic results max value: 140 Note: your account will be billed per each 20 organic results regardless of paid listings in the response; thus, setting a depth above 20 may result in additional charges if Google Hotels return more than 20 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional] 
**check_in** | **str** | check-in date optional field if you don’t specify this field, tomorrow’s date will be used by default; date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; Note: the value cannot precede the today’s date | [optional] 
**check_out** | **str** | check-out date optional field if you don’t specify this field, our system will apply the date of two days from now by default; date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; Note: the value cannot be less than or equal to check_in; the range between check_in and check_out values cannot exceed 30 days | [optional] 
**currency** | **str** | currency optional field example: \&quot;USD\&quot; | [optional] 
**adults** | **int** | number of adults optional field if you don’t specify this field, the default value of 2 will be applied; note that you can specify up to 6 persons including both adults and children example: 1 | [optional] 
**children** | **List[str]** | number and age of children optional field if you don’t specify this field, no children will be included in the search; age of child can be from 0 to 17; note that you can specify up to 6 persons including both adults and children set the following value if you want to include one 14-year-old child: [14] set the following value if you want to include one 13-year-old child and one 8-year-old child: [13,8] | [optional] 
**stars** | **List[str]** | hotel stars optional field set this field to [5] if you want to get the list of 5-star hotels only example: [3,4,5] | [optional] 
**min_rating** | **float** | minimum rating optional field you can use this field to specify guest rating higher than a certain value example: 2.5 | [optional] 
**sort_by** | **str** | results sorting parameters optional field you can use this field to sort the results possible types of sorting: relevance – sort by most relevant lowest_price – sort by the lowest price highest_rating – sort by highest rating most_reviewed – sort by most reviewed default value: relevance | [optional] 
**min_price** | **int** | minimum price per night optional field the currency of this value depends on the currency field example: 100 | [optional] 
**max_price** | **int** | maximum price per night optional field the currency of this value depends on the currency field example: 600 | [optional] 
**free_cancellation** | **bool** | hotels with a free cancellation optional field set this field to true if you want to get the list of hotels with free cancellation of reservations default value: false | [optional] 
**is_vacation_rentals** | **bool** | search for vacation rentals optional field set this field to true if you want to get the list of vacation rentals instead of hotels default value: false | [optional] 
**amenities** | **List[str]** | hotel amenities optional field you can use this field to specify different hotel amenities example:   [             \&quot;free_parking\&quot;,             \&quot;pets_allowed\&quot;         ]  possible values: \&quot;air_conditioning\&quot;, \&quot;all_inclusive_available\&quot;, \&quot;bar\&quot;, \&quot;free_breakfast\&quot;, \&quot;fitness_center\&quot;, \&quot;kid_friendly\&quot;, \&quot;free_parking\&quot;, \&quot;pets_allowed\&quot;, \&quot;pool\&quot;, \&quot;restaurant\&quot;, \&quot;room_service\&quot;, \&quot;spa\&quot;, \&quot;free_wifi\&quot;, \&quot;parking\&quot;, \&quot;indoor_pool\&quot;, \&quot;outdoor_pool\&quot;, \&quot;wheelchair_accessible\&quot;, \&quot;beach_access\&quot; | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_hotel_searches_live_request_info import BusinessDataGoogleHotelSearchesLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleHotelSearchesLiveRequestInfo from a JSON string
business_data_google_hotel_searches_live_request_info_instance = BusinessDataGoogleHotelSearchesLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataGoogleHotelSearchesLiveRequestInfo.to_json()

# convert the object into a dict
business_data_google_hotel_searches_live_request_info_dict = business_data_google_hotel_searches_live_request_info_instance.to_dict()
# create an instance of BusinessDataGoogleHotelSearchesLiveRequestInfo from a dict
business_data_google_hotel_searches_live_request_info_form_dict = business_data_google_hotel_searches_live_request_info.from_dict(business_data_google_hotel_searches_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



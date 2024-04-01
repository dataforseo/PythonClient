# BusinessDataGoogleHotelInfoTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field the keyword you specify should indicate the name of the local establishment you can specify up to 700 symbols in the keyword filed all %## will be decoded (plus symbol ‘+’ will be decoded to a space character) if you need to use the “%” symbol for your keyword, please specify it as “%25”;  this field can also be used to pass the following parameters: cid – a unique, google-defined id of the business entity; place_id – an identifier of the business entity in Google Maps; spp – a unique identifier of local services featured in the local_pack element of Google SERP example: cid:194604053573767737 place_id:GhIJQWDl0CIeQUARxks3icF8U8A spp:CgsvZy8xdGN4cWRraBoUChIJPZDrEzLsZIgRoNrpodC5P30 learn more about the cid and place_id identifiers in this help center article | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations with location_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/google/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 199.9 example: 53.476225,-2.243572,200 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages with language_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages example: en | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 
**hotel_identifier** | **str** | unique hotel identifier required field if you don’t specify keyword if you use this field, you don’t need to specify keyword unique identifier of a hotel entity in Google search; you can obtain the value by making a request to Advanced Google SERP API (enclosed in the hotels_pack element of the response), or the Hotel Searches endpoint of Business Data API example: ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE | [optional] 
**check_in** | **str** | check-in date optional field if you don’t specify this field, tomorrow’s date will be used by default; the value must not be earlier than today’s date date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**check_out** | **str** | check-out date optional field if you don’t specify this field, our system will apply the date of two days from now by default; Note: the value cannot be less than or equal to check_in; the range between check_in and check_out values cannot exceed 30 days date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**currency** | **str** | currency optional field example: \&quot;USD\&quot; | [optional] 
**adults** | **int** | number of adults optional field if you don’t specify this field, two adults will be used by default example: 1 | [optional] 
**children** | **List[str]** | number and age of children optional field if you don’t specify this field, no children will be included in the search; set the following value if you want to include one 14-years-old child: [14] set the following value if you want to include one 13-years-old child and one 8-years-old child: [13,8] | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible values: advanced, html | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_hotel_info_task_post_request_info import BusinessDataGoogleHotelInfoTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleHotelInfoTaskPostRequestInfo from a JSON string
business_data_google_hotel_info_task_post_request_info_instance = BusinessDataGoogleHotelInfoTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataGoogleHotelInfoTaskPostRequestInfo.to_json())

# convert the object into a dict
business_data_google_hotel_info_task_post_request_info_dict = business_data_google_hotel_info_task_post_request_info_instance.to_dict()
# create an instance of BusinessDataGoogleHotelInfoTaskPostRequestInfo from a dict
business_data_google_hotel_info_task_post_request_info_form_dict = business_data_google_hotel_info_task_post_request_info.from_dict(business_data_google_hotel_info_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | keywords required field The maximum number of keywords you can specify: 1000 The maximum number of characters for each keyword: 100 the specified keywords will be converted to lowercase, data will be provided in a separate array learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/search_volume_history/locations_and_languages example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/search_volume_history/locations_and_languages example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude” format the data will be provided for the country the specified coordinates belong to example: 52.6178549,-155.352142 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engines with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/search_volume_history/locations_and_languages | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engines with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/search_volume_history/locations_and_languages | [optional] 
**device** | **str** | device type optional field specify this field if you want to get the data for a particular device type possible values: mobile, desktop, tablet, non_smartphones default value:  mobile, desktop, tablet, non_smartphones | [optional] 
**period** | **str** | aggregates the returned data to a certain time period optional field specify this field if you want to get the data in monthly, weekly or daily format possible values: monthly, weekly, daily monthly – returns data up to past 24 months weekly – returns data up to past 15 weeks daily – returns data up to past 45 days default value:  monthly | [optional] 
**date_from** | **str** | starting date of the time range optional field minimum value: two years back from today’s date maximum value: one day from today’s date date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2020-01-01\&quot; Note: we do not recommend using a custom time range Note 2: if date_from and date_to parameters are not specified, the data will be returned for the past 24 months if you specify the period parameter: with value weekly, you will get results for the past 15 weeks with value daily, you will get results for the past 45 days | [optional] 
**date_to** | **str** | ending date of the time range optional field minimum value: two years back from today’s date; maximum value: one day from today’s date; date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2020-03-15\&quot; Note: we do not recommend using a custom time range Note 2: if date_from and date_to parameters are not specified, the data will be returned for the past 24 months if you specify the period parameter: with value weekly, you will get results for the past 15 weeks with value daily, you will get results for the past 45 days | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_search_volume_history_task_post_request_info import KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo from a JSON string
keywords_data_bing_search_volume_history_task_post_request_info_instance = KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo.to_json())

# convert the object into a dict
keywords_data_bing_search_volume_history_task_post_request_info_dict = keywords_data_bing_search_volume_history_task_post_request_info_instance.to_dict()
# create an instance of KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo from a dict
keywords_data_bing_search_volume_history_task_post_request_info_from_dict = KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo.from_dict(keywords_data_bing_search_volume_history_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



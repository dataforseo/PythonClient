# KeywordsDataBingKeywordsForSiteTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain or URL required field the URL of the webpage or the domain to scan for possible keywords | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude” format the data will be provided for the country the specified coordinates belong to example: 52.6178549,-155.352142 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code supported languages: English, French, German | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name supported languages: en, fr, de | [optional] 
**keywords_negative** | **List[str]** | keywords negative array optional field These keywords will be ignored in the results array; You can specify a maximum of 200 terms that you want to exclude from the results; the specified keywords will be converted to lowercase format | [optional] 
**device** | **str** | device type optional field specify this field if you want to get the data for a particular device type possible values: all, mobile, desktop, tablet default value: all | [optional] 
**sort_by** | **str** | results sorting parameters optional field Use these parameters to sort the results by search_volume, cpc, competition or relevance in the descending order default value: relevance | [optional] 
**date_from** | **str** | starting date of the time range optional field if you don’t specify this field, data will be provided for the last 12 months date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2020-01-01\&quot; Note: we do not recommend using a custom time range for the past year’s dates | [optional] 
**date_to** | **str** | ending date of the time range optional field if you don’t specify this field, data will be provided for the last 12 months; minimum value: two years back from today’s date; maximum value: one month from today’s date; date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2020-03-15\&quot; Note: we do not recommend using a custom time range for the past year’s dates | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 
**search_partners** | **bool** | Bing search partners type optional field if you specify true, the results will be delivered for owned, operated, and syndicated networks across Bing, Yahoo, AOL and partner sites that host Bing, AOL, and Yahoo search. default value: false – results are returned for Bing, AOL, and Yahoo search networks | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_keywords_for_site_task_post_request_info import KeywordsDataBingKeywordsForSiteTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingKeywordsForSiteTaskPostRequestInfo from a JSON string
keywords_data_bing_keywords_for_site_task_post_request_info_instance = KeywordsDataBingKeywordsForSiteTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataBingKeywordsForSiteTaskPostRequestInfo.to_json()

# convert the object into a dict
keywords_data_bing_keywords_for_site_task_post_request_info_dict = keywords_data_bing_keywords_for_site_task_post_request_info_instance.to_dict()
# create an instance of KeywordsDataBingKeywordsForSiteTaskPostRequestInfo from a dict
keywords_data_bing_keywords_for_site_task_post_request_info_form_dict = keywords_data_bing_keywords_for_site_task_post_request_info.from_dict(keywords_data_bing_keywords_for_site_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



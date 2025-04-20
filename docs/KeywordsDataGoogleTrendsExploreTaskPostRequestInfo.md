# KeywordsDataGoogleTrendsExploreTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | keywords required field the maximum number of keywords you can specify: 5 the maximum number of characters you can specify in a keyword: 100 the minimum number of characters must be greater than 1 comma characters (,) in the specified keywords will be unset and ignored Note: keywords cannot consist of a combination of the following characters: &lt; &gt; | \\ \&quot; - + &#x3D; ~ ! : * ( ) [ ] { } Note: to obtain google_trends_topics_list and google_trends_queries_list items, specify no more than 1 keyword learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **List[Optional[str]]** | full name of search engine location optional field if you don’t use this field, you will recieve global results if you use this field, you don’t need to specify location_code you can use this field as an array to set several locations, each corresponding to a specific keyword – learn more; you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/locations example: United Kingdom | [optional] 
**location_code** | **List[Optional[int]]** | search engine location code optional field if you don’t use this field, you will recieve global results if you use this field, you don’t need to specify location_name you can use this field as an array to set several locations, each corresponding to a specific keyword – learn more; you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/locations example: 2840 | [optional] 
**language_name** | **str** | full name of search engine language optional field default value: English if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/languages example: English | [optional] 
**language_code** | **str** | search engine language code optional field default value: en if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/languages example: en | [optional] 
**type** | **str** | type of element | [optional] 
**category_code** | **int** | google trends search category optional field if you don’t specify this field, the 0 value will be applied by default and the search will be carried out across all available categories you can receive the list of available categories with their category_code by making a separate request to the https://api.dataforseo.com/v3/keywords_data/google_trends/categories | [optional] 
**date_from** | **str** | starting date of the time range optional field if you don’t specify this field, the current day and month of the preceding year will be used by default minimal value for the web type: 2004-01-01 minimal value for other types: 2008-01-01 date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**date_to** | **str** | ending date of the time range optional field if you don’t specify this field, the today’s date will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**time_range** | **str** | preset time ranges optional field if you specify date_from or date_to parameters, this field will be ignored when setting a task possible values for all type parameters: past_hour, past_4_hours, past_day, past_7_days, past_30_days, past_90_days, past_12_months, past_5_years possible values for web only: 2004_present possible values for news, youtube, images, froogle: 2008_present | [optional] 
**item_types** | **List[str]** | types of items returned optional field to speed up the execution of the request, specify one item at a time; possible values: \&quot;google_trends_graph\&quot;, \&quot;google_trends_map\&quot;, \&quot;google_trends_topics_list\&quot;,\&quot;google_trends_queries_list\&quot; default value: \&quot;google_trends_graph\&quot; Note: to obtain google_trends_topics_list and google_trends_queries_list items, specify no more than 1 keyword in the keywords field | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_google_trends_explore_task_post_request_info import KeywordsDataGoogleTrendsExploreTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleTrendsExploreTaskPostRequestInfo from a JSON string
keywords_data_google_trends_explore_task_post_request_info_instance = KeywordsDataGoogleTrendsExploreTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataGoogleTrendsExploreTaskPostRequestInfo.to_json())

# convert the object into a dict
keywords_data_google_trends_explore_task_post_request_info_dict = keywords_data_google_trends_explore_task_post_request_info_instance.to_dict()
# create an instance of KeywordsDataGoogleTrendsExploreTaskPostRequestInfo from a dict
keywords_data_google_trends_explore_task_post_request_info_from_dict = KeywordsDataGoogleTrendsExploreTaskPostRequestInfo.from_dict(keywords_data_google_trends_explore_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



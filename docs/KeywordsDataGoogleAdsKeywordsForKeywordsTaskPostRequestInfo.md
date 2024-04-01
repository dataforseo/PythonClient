# KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | keywords required field The maximum number of keywords you can specify: 1000 The maximum number of characters for each keyword: 80 The maximum number of words for each keyword phrase: 10 the keywords you specify will be converted to a lowercase format Note #1: Google Ads may return no data for certain groups of keywords; Note #2: Google Ads provides combined search volume values for groups of similar keywords to obtain search volume for similar keywords, we recommend submitting such keywords in separate requests; Note #3: Google Ads doesn’t allow using certain symbols and characters (e.g., UTF symbols, emojis), so you can’t use them when setting a task; to learn more about which symbols can be used, please refer to this article | [optional] 
**location_name** | **str** | full name of search engine location optional field if you do not indicate the location, you will receive worldwide results, i.e., for all available locations; if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code optional field if you do not indicate the location, you will receive worldwide results, i.e., for all available locations; if you use this field, you don’t need to specify location_name or location_coordinate; you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location optional field if you do not indicate the location, you will receive worldwide results, i.e., for all available locations; if you use this field, you don’t need to specify location_name or location_code; location_coordinate parameter should be specified in the “latitude,longitude” format; the data will be provided for the country the specified coordinates belong to; example: 52.6178549,-155.352142 | [optional] 
**language_name** | **str** | full name of search engine language optional field you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages example: English | [optional] 
**language_code** | **str** | search engine language code optional field you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages example: en | [optional] 
**search_partners** | **bool** | include Google search partners optional field if you specify true, the results will be delivered for owned, operated, and syndicated networks across Google and partner sites that host Google search; default value: false – results are returned for Google search sites | [optional] 
**date_from** | **str** | starting date of the time range optional field date format: \&quot;yyyy-mm-dd\&quot; minimal value: 4 years from the current date by default, data is returned for the past 12 months; Note: the indicated date cannot be greater than that specified in date_to and/or yesterday’s date;if Status endpoint returns false in the actual_data field, date_from can be set to the month before last and prior; if Status endpoint returns true in the actual_data field, date_from can be set to the last month and prior | [optional] 
**date_to** | **str** | ending date of the time range optional field Note: the indicated date cannot be greater than the past month, Google Ads does not return data on the current month; if you don’t specify this field, yesterday’s date will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2022-11-30\&quot; | [optional] 
**include_adult_keywords** | **bool** | include keywords associated with adult content optional field if set to true, adult keywords will be included in the response default value: false note that the API may return no data for such keywords due to Google Ads restrictions | [optional] 
**sort_by** | **str** | results sorting parameters optional field use these parameters to sort the results by relevance, search_volume, competition_index, low_top_of_page_bid, or high_top_of_page_bid in the descending order default value: relevance | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data array of the response | [optional] 
**target** | **str** | target website optional field specify a website or URL to get a list of keywords relevant to it; Note: if a website url is specified, you will still get keywords relevant for the entire website | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_google_ads_keywords_for_keywords_task_post_request_info import KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo from a JSON string
keywords_data_google_ads_keywords_for_keywords_task_post_request_info_instance = KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo.to_json())

# convert the object into a dict
keywords_data_google_ads_keywords_for_keywords_task_post_request_info_dict = keywords_data_google_ads_keywords_for_keywords_task_post_request_info_instance.to_dict()
# create an instance of KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo from a dict
keywords_data_google_ads_keywords_for_keywords_task_post_request_info_form_dict = keywords_data_google_ads_keywords_for_keywords_task_post_request_info.from_dict(keywords_data_google_ads_keywords_for_keywords_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



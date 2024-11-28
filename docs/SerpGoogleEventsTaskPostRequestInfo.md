# SerpGoogleEventsTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field you can specify up to 700 characters in the keyword field all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B” learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default); 2 – high execution priority You will be additionally charged for the tasks with high execution priority; The cost can be calculated on the Pricing page | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/events/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/events/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius” format data will be provided for the country the specified coordinates belong to the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 199.9 (mm) the maximum value for “radius”: 199999 (mm) example: 53.476225,-2.243572,200 | [optional] 
**language_name** | **str** | full name of search engine language optional field if you use this field, you don’t need to specify language_code by default, language settings correspond to one of the local official languages of the specified location you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code optional field if you use this field, you don’t need to specify language_name by default, language settings correspond to one of the local official languages of the specified location you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: en | [optional] 
**date_range** | **str** | date range to get events for optional field if you do not use this field, we will return all events possible values: today, tomorrow, week, weekend, next_week, month, next_month | [optional] 
**os** | **str** | device operating system optional field note that this API provides results for desktop only choose from the following values: windows, macos default value: windows | [optional] 
**se_domain** | **str** | search engine domain optional field we choose the relevant search engine domain automatically according to the location you specify however, you can set a custom search engine domain in this field example: google.co.uk, google.com.au, google.de, etc. | [optional] 
**depth** | **int** | parsing depth optional field number of results in SERP default value: 10 max value: 700 Note: your account will be billed per each SERP containing up to 10 results; thus, setting a depth above 10 may result in additional charges if the search engine returns more than 10 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional] 
**max_crawl_pages** | **int** | page crawl limit optional field number of search results pages to crawl max value: 100 Note: the max_crawl_pages and depth parameters complement each other; learn more at our help center | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible values: advanced | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_events_task_post_request_info import SerpGoogleEventsTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleEventsTaskPostRequestInfo from a JSON string
serp_google_events_task_post_request_info_instance = SerpGoogleEventsTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleEventsTaskPostRequestInfo.to_json())

# convert the object into a dict
serp_google_events_task_post_request_info_dict = serp_google_events_task_post_request_info_instance.to_dict()
# create an instance of SerpGoogleEventsTaskPostRequestInfo from a dict
serp_google_events_task_post_request_info_from_dict = SerpGoogleEventsTaskPostRequestInfo.from_dict(serp_google_events_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



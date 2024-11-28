# SerpSeznamOrganicTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field you can specify up to 700 characters in the keyword field all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B” learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code if you use this field, you don’t need to specify location_code you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/seznam/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name if you use this field, you don’t need to specify location_name you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/seznam/locations example: 2840 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/seznam/languages example: Czech | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/seznam/languages example: cs | [optional] 
**url** | **str** | direct URL of the search query optional field you can specify a direct URL and we will sort it out to the necessary fields; note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL; in most cases, we wouldn’t recommend using this method. | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**depth** | **int** | parsing depth optional field number of results in SERP default value: 10; maximum value: 500; Note: your account will be billed per each SERP containing up to 10 results; thus, setting a depth above 10 may result in additional charges if the search engine returns more than 10 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional] 
**max_crawl_pages** | **int** | page crawl limit optional field number of search results pages to crawl max value: 10 Note: the max_crawl_pages and depth parameters complement each other; learn more at our help center | [optional] 
**device** | **str** | device type optional field can take the values:desktop, mobile default value: desktop | [optional] 
**os** | **str** | device operating system optional field if you specify desktop in the device field, choose from the following values: windows, macos default value: windows if you specify mobile in the device field, choose from the following values: android, ios default value: android | [optional] 
**se_domain** | **str** | search engine domain optional field we choose the relevant search engine domain automatically however, you can set a custom search engine domain in this field example: search.seznam.cz | [optional] 
**search_param** | **str** | additional parameters of the search query optional field | [optional] 
**calculate_rectangles** | **bool** | calcualte pixel rankings for SERP elements in advanced results optional field pixel ranking refers to the distance between the result snippet and top left corner of the screen; Visit Help Center to learn more&gt;&gt; by default, the parameter is set to false Note: if set to true, the charge per task will be multiplied by 2 | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the function you used for setting a task possible values: regular, advanced, html | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.serp_seznam_organic_task_post_request_info import SerpSeznamOrganicTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpSeznamOrganicTaskPostRequestInfo from a JSON string
serp_seznam_organic_task_post_request_info_instance = SerpSeznamOrganicTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpSeznamOrganicTaskPostRequestInfo.to_json())

# convert the object into a dict
serp_seznam_organic_task_post_request_info_dict = serp_seznam_organic_task_post_request_info_instance.to_dict()
# create an instance of SerpSeznamOrganicTaskPostRequestInfo from a dict
serp_seznam_organic_task_post_request_info_from_dict = SerpSeznamOrganicTaskPostRequestInfo.from_dict(serp_seznam_organic_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



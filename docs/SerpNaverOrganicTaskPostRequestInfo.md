# SerpNaverOrganicTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field you can specify up to 700 characters in the keyword field all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B” learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**url** | **str** | direct URL of the search query optional field you can specify a direct URL and we will sort it out to the necessary fields in most cases, we wouldn’t recommend using this method; example: https://search.naver.com/search.naver?where&#x3D;nexearch&amp;sm&#x3D;top_hty&amp;fbm&#x3D;1&amp;ie&#x3D;utf8&amp;query&#x3D;iphone | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**depth** | **int** | parsing depth optional field number of results in SERP default value: 100 max value: 700 Note: your account will be billed per each SERP containing up to 100 results; thus, setting a depth above 100 may result in additional charges if the search engine returns more than 100 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional] 
**max_crawl_pages** | **int** | page crawl limit optional field number of search results pages to crawl max value: 100 Note: the max_crawl_pages and depth parameters complement each other; learn more at our help center | [optional] 
**device** | **str** | device type optional field can take the values:desktop, mobile default value: desktop | [optional] 
**os** | **str** | device operating system optional field if you specify desktop in the device field, choose from the following values: windows, macos default value: windows if you specify mobile in the device field, choose from the following values: android, ios default value: android | [optional] 
**se_domain** | **str** | search engine domain optional field we choose the relevant search engine domain automatically however, you can set a custom search engine domain in this field example: search.naver.com | [optional] 
**search_param** | **str** | additional parameters of the search query optional field get the list of available parameters and additional details here | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the function you used for setting a task possible values: regular, advanced, html | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.serp_naver_organic_task_post_request_info import SerpNaverOrganicTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpNaverOrganicTaskPostRequestInfo from a JSON string
serp_naver_organic_task_post_request_info_instance = SerpNaverOrganicTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpNaverOrganicTaskPostRequestInfo.to_json())

# convert the object into a dict
serp_naver_organic_task_post_request_info_dict = serp_naver_organic_task_post_request_info_instance.to_dict()
# create an instance of SerpNaverOrganicTaskPostRequestInfo from a dict
serp_naver_organic_task_post_request_info_from_dict = SerpNaverOrganicTaskPostRequestInfo.from_dict(serp_naver_organic_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



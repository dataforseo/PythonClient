# SerpBingOrganicLiveRegularRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | direct URL of the search query optional field you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method. example: https://www.bing.com/search?q&#x3D;rank%20checker&amp;count&#x3D;50&amp;first&#x3D;1&amp;setlang&#x3D;en&amp;cc&#x3D;US&amp;safesearch&#x3D;Moderate&amp;FORM&#x3D;SEPAGE | [optional] 
**keyword** | **str** | keyword required field you can specify up to 700 characters in the keyword field all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B”; if this field contains such parameters as ‘allinanchor:’, ‘allintext:’, ‘allintitle:’, ‘allinurl:’, ‘define:’, ‘filetype:’, ‘id:’, ‘inanchor:’, ‘info:’, ‘intext:’, ‘intitle:’, ‘inurl:’, ‘link:’, ‘related:’, ‘site:’ the charge per task will be multiplied by 5 learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/bing/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/bing/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude” format the maximum number of decimal digits for “latitude” and “longitude”: 7 example: 53.476225,-2.243572 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/bing/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/bing/languages example: en | [optional] 
**device** | **str** | device type optional field can take the values:desktop, mobile default value: desktop | [optional] 
**os** | **str** | device operating system optional field if you specify desktop in the device field, choose from the following values: windows, macos default value: windows if you specify mobile in the device field, choose from the following values: android, ios default value: android | [optional] 
**depth** | **int** | parsing depth optional field number of results in SERP default value: 100 max value: 700 Note: your account will be billed per each SERP containing up to 100 results; thus, setting a depth above 100 may result in additional charges if the search engine returns more than 100 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional] 
**max_crawl_pages** | **int** | page crawl limit optional field number of search results pages to crawl max value: 100 Note: the max_crawl_pages and depth parameters complement each other; learn more at our help center | [optional] 
**search_param** | **str** | additional parameters of the search query optional field get the list of available parameters and additional details here | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.serp_bing_organic_live_regular_request_info import SerpBingOrganicLiveRegularRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpBingOrganicLiveRegularRequestInfo from a JSON string
serp_bing_organic_live_regular_request_info_instance = SerpBingOrganicLiveRegularRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpBingOrganicLiveRegularRequestInfo.to_json())

# convert the object into a dict
serp_bing_organic_live_regular_request_info_dict = serp_bing_organic_live_regular_request_info_instance.to_dict()
# create an instance of SerpBingOrganicLiveRegularRequestInfo from a dict
serp_bing_organic_live_regular_request_info_from_dict = SerpBingOrganicLiveRegularRequestInfo.from_dict(serp_bing_organic_live_regular_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



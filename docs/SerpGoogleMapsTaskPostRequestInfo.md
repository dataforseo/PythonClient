# SerpGoogleMapsTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | direct URL of the search query optional field you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method. example: https://google.com/maps/search/pizza/@37.09024,-95.712891,4z | [optional] 
**keyword** | **str** | keyword required field you can specify up to 700 symbols in the keyword field all %## will be decoded (plus symbol ‘+’ will be decoded to a space character) if you need to use the “%” symbol for your keyword, please specify it as “%25”; if you need to use the “+” symbol for your keyword, please specify it as “%2B”; if this field contains such parameters as ‘allinanchor:’, ‘allintext:’, ‘allintitle:’, ‘allinurl:’, ‘define:’, ‘filetype:’, ‘id:’, ‘inanchor:’, ‘info:’, ‘intext:’, ‘intitle:’, ‘inurl:’, ‘link:’, ‘related:’, ‘site:’, the charge per task will be multiplied by 5 Note: queries containing the ‘cache:’ parameter are not supported and will return a validation error learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,zoom” format if “zoom” is not specified, 17z will be applied as a default value the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “zoom”: 3z the maximum value for “zoom”: 21z example: 52.6178549,-155.352142,20z | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: en | [optional] 
**device** | **str** | device type optional field can take the values:desktop, mobile default value: desktop note: for mobile device, only 20 results are returned for every SERP | [optional] 
**os** | **str** | device operating system optional field if you specify desktop in the device field, choose from the following values: windows, macos default value: windows if you specify mobile in the device field, choose from the following values: android, ios default value: android | [optional] 
**se_domain** | **str** | search engine domain optional field we choose the relevant search engine domain automatically according to the location and language you specify however, you can set a custom search engine domain in this field example: google.co.uk, google.com.au, google.de, etc. | [optional] 
**depth** | **int** | parsing depth optional field number of results in SERP default value: 100 max value: 700 Note: your account will be billed per each SERP containing up to 100 results; thus, setting a depth above 100 may result in additional charges if the search engine returns more than 100 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional] 
**max_crawl_pages** | **int** | page crawl limit optional field number of search results pages to crawl max value: 100 Note: the max_crawl_pages and depth parameters complement each other; learn more at our help center | [optional] 
**search_this_area** | **bool** | search this area optional field can take the values:true, false default value: trueif set to false, the search_this_area mode will be turned off Note: if the search_this_area mode is turned off, Google Maps listings might contain results beyond the displayed area | [optional] 
**search_places** | **bool** | search places mode optional field the search places mode allows to obtain Google Maps results on a certain place (e.g., Apple Store in New York) however, due to the pecularities of our data mining algorithm, this mode might interfere with some local-intent queries – and display results for a location that is different from that specified in the request; to prevent this interference and obtain correct results for keywords with local intent you may set this parameter to false;default value: true Note: if the search_places mode is turned off and no results were found in the search area, the results array will be empty | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the function you used for setting a task possible values: advanced | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_maps_task_post_request_info import SerpGoogleMapsTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleMapsTaskPostRequestInfo from a JSON string
serp_google_maps_task_post_request_info_instance = SerpGoogleMapsTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print SerpGoogleMapsTaskPostRequestInfo.to_json()

# convert the object into a dict
serp_google_maps_task_post_request_info_dict = serp_google_maps_task_post_request_info_instance.to_dict()
# create an instance of SerpGoogleMapsTaskPostRequestInfo from a dict
serp_google_maps_task_post_request_info_form_dict = serp_google_maps_task_post_request_info.from_dict(serp_google_maps_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



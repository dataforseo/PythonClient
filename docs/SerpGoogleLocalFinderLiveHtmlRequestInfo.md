# SerpGoogleLocalFinderLiveHtmlRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field you can specify up to 700 symbols in the keyword field all %## will be decoded (plus symbol ‘+’ will be decoded to a space character) if you need to use the “%” symbol for your keyword, please specify it as “%25”; if you need to use the “+” symbol for your keyword, please specify it as “%2B” | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,zoom” format if “zoom” is not specified, 9z will be applied as a default value the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “zoom”: 4z the maximum value for “zoom”: 18z example: 52.6178549,-155.352142,20z | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example:en | [optional] 
**device** | **str** | device type optional field can take the values:desktop, mobile default value: desktop | [optional] 
**os** | **str** | device operating system optional field if you specify desktop in the device field, choose from the following values: windows, macos default value: windows if you specify mobile in the device field, choose from the following values: android, ios default value: android | [optional] 
**depth** | **int** | parsing depth optional field number of results in SERP default value for desktop: 20 max value for desktop: 100 default value for mobile: 10 max value for mobile: 100 Note: your account will be billed per each SERP containing up to 20 results for desktop or up to 10 results for a mobile device; thus, setting a depth above 20 for desktop or above 10 for mobile may result in additional charges if the search engine returns more than 20 or 10 results respectively; if the specified depth is higher than the number of results in the response, the difference will be refunded to your account balance automatically | [optional] 
**min_rating** | **float** | filter results by minimum rating optional field possible values for desktop: 3.5, 4, 4.5; possible values for mobile: 2, 2.5, 3, 3.5, 4, 4.5 | [optional] 
**time_filter** | **str** | filter results by open hours optional field using this field, you can filter places in the results by the time a place is open for visitors note that Google may also provide results that do not match this filter possible values: \&quot;open_now\&quot;, \&quot;24_hours\&quot;, \&quot;$day_value\&quot;, \&quot;$day_value;$time_value\&quot;; instead of $day_value use one of these values: \&quot;monday\&quot;, \&quot;tuesday\&quot;, \&quot;wednesday\&quot;, \&quot;thursday\&quot;, \&quot;friday\&quot;, \&quot;saturday\&quot;, \&quot;sunday\&quot;; instead of $time_value use one of these values: \&quot;00\&quot;, \&quot;01\&quot;, \&quot;02\&quot;, \&quot;03\&quot;, \&quot;04\&quot;, \&quot;05\&quot;, \&quot;06\&quot;, \&quot;07\&quot;, \&quot;08\&quot;, \&quot;09\&quot;, \&quot;10\&quot;, \&quot;11\&quot;, \&quot;12\&quot;, \&quot;13\&quot;, \&quot;14\&quot;, \&quot;15\&quot;, \&quot;16\&quot;, \&quot;17\&quot;, \&quot;18\&quot;, \&quot;19\&quot;, \&quot;20\&quot;, \&quot;21\&quot;, \&quot;22\&quot;, \&quot;23\&quot; example: \&quot;tuesday;18\&quot; | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_local_finder_live_html_request_info import SerpGoogleLocalFinderLiveHtmlRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleLocalFinderLiveHtmlRequestInfo from a JSON string
serp_google_local_finder_live_html_request_info_instance = SerpGoogleLocalFinderLiveHtmlRequestInfo.from_json(json)
# print the JSON string representation of the object
print SerpGoogleLocalFinderLiveHtmlRequestInfo.to_json()

# convert the object into a dict
serp_google_local_finder_live_html_request_info_dict = serp_google_local_finder_live_html_request_info_instance.to_dict()
# create an instance of SerpGoogleLocalFinderLiveHtmlRequestInfo from a dict
serp_google_local_finder_live_html_request_info_form_dict = serp_google_local_finder_live_html_request_info.from_dict(serp_google_local_finder_live_html_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



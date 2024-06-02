# SerpGoogleAutocompleteLiveAdvancedRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field you can specify up to 700 symbols in the keyword field all %## will be decoded (plus symbol ‘+’ will be decoded to a space character) if you need to use the “%” symbol for your keyword, please specify it as “%25”; if you need to use the “+” symbol for your keyword, please specify it as “%2B”; | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code if you use this field, you don’t need to specify location_code; you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/serp/google/autocomplete/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name; you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/locations example: 2840 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code; you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/serp/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name; you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: en | [optional] 
**cursor_pointer** | **int** | search bar cursor pointer optional field the horizontal numerical position of the cursor pointer within the keyword in the search bar; by modifying the position of the cursor pointer, you will obtain different autocomplete suggestions for the same seed keyword; minimal value: 0 default value: the number of the last symbol of the specified keyword example: |which query are s – \&quot;cursor_pointer\&quot;: 0 which query is s| – \&quot;cursor_pointer\&quot;: 16 which que|ry is s – \&quot;cursor_pointer\&quot;: 9 | [optional] 
**client** | **str** | search client for autocomplete optional field autocomplete results may differ depending on the search client; possible values: chrome — used when google search is opened in google chrome; chrome-omni — used in the address bar in chrome; gws-wiz — used in google search home page; gws-wiz-serp — used in google search engine results page; safari — used when google search is opened in safari browser; firefox — used when google search is opened in firefox browser; psy-ab — may be used when google search is opened in google chrome browser; toolbar — returns XML; youtube — returns JSONP; gws-wiz-local — used in google local; img — used in google’s image search; products-cc — used in google shopping search | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_autocomplete_live_advanced_request_info import SerpGoogleAutocompleteLiveAdvancedRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleAutocompleteLiveAdvancedRequestInfo from a JSON string
serp_google_autocomplete_live_advanced_request_info_instance = SerpGoogleAutocompleteLiveAdvancedRequestInfo.from_json(json)
# print the JSON string representation of the object
print SerpGoogleAutocompleteLiveAdvancedRequestInfo.to_json()

# convert the object into a dict
serp_google_autocomplete_live_advanced_request_info_dict = serp_google_autocomplete_live_advanced_request_info_instance.to_dict()
# create an instance of SerpGoogleAutocompleteLiveAdvancedRequestInfo from a dict
serp_google_autocomplete_live_advanced_request_info_form_dict = serp_google_autocomplete_live_advanced_request_info.from_dict(serp_google_autocomplete_live_advanced_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



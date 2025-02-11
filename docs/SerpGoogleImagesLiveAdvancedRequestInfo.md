# SerpGoogleImagesLiveAdvancedRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | direct URL of the search query optional field you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method. example: https://www.google.co.uk/search?q&#x3D;%20rank%20tracker%20api&amp;hl&#x3D;en&amp;gl&#x3D;GB&amp;uule&#x3D;w+CAIQIFISCXXeIa8LoNhHEZkq1d1aOpZS | [optional] 
**keyword** | **str** | keyword required field you can specify up to 700 characters in the keyword field all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B”; if this field contains such parameters as ‘allinanchor:’, ‘allintext:’, ‘allintitle:’, ‘allinurl:’, ‘define:’, ‘filetype:’, ‘id:’, ‘inanchor:’, ‘info:’, ‘intext:’, ‘intitle:’, ‘inurl:’, ‘link:’, ‘related:’, ‘site:’, the charge per task will be multiplied by 5 Note: queries containing the ‘cache:’ parameter are not supported and will return a validation error learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 199.9 (mm) the maximum value for “radius”: 199999 (mm) example: 53.476225,-2.243572,200 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: en | [optional] 
**os** | **str** | device operating system optional field note that this API provides results for desktop only choose from the following values: windows, macos default value: windows | [optional] 
**se_domain** | **str** | search engine domain optional field We choose the relevant search engine domain automatically according to the location and language you specify. However, you can set a custom search engine domain in this field example: google.co.uk, google.com.au, google.de, etc. | [optional] 
**depth** | **int** | parsing depth optional field number of results in SERP default value: 100 max value: 700 Note: your account will be billed per each SERP containing up to 100 results; thus, setting a depth above 100 may result in additional charges if the search engine returns more than 100 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional] 
**max_crawl_pages** | **int** | page crawl limit optional field number of search results pages to crawl max value: 100 Note: the max_crawl_pages and depth parameters complement each other; learn more at our help center | [optional] 
**search_param** | **str** | additional parameters of the search query optional field Get the list of available parameters and additional details here. | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_images_live_advanced_request_info import SerpGoogleImagesLiveAdvancedRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleImagesLiveAdvancedRequestInfo from a JSON string
serp_google_images_live_advanced_request_info_instance = SerpGoogleImagesLiveAdvancedRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleImagesLiveAdvancedRequestInfo.to_json())

# convert the object into a dict
serp_google_images_live_advanced_request_info_dict = serp_google_images_live_advanced_request_info_instance.to_dict()
# create an instance of SerpGoogleImagesLiveAdvancedRequestInfo from a dict
serp_google_images_live_advanced_request_info_from_dict = SerpGoogleImagesLiveAdvancedRequestInfo.from_dict(serp_google_images_live_advanced_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



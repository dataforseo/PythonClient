# SerpGoogleAdsAdvertisersTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field you can specify up to 700 characters in the keyword field all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B” learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of search engine location optional field if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/ads_advertisers/locations example: London,England,United Kingdom Note: if you don’t specify location_name, location_code, or location_coordinate, advertisers will be searched across all the available locations | [optional] 
**location_code** | **int** | search engine location code optional field if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/ads_advertisers/locations example: 2840 Note: if you don’t specify location_name, location_code, or location_coordinate, advertisers will be searched across all the available locations | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location optional field if you use this field, you don’t need to specify location_name or location_code example: 52.6178549,-155.352142 Note: if you don’t specify location_name, location_code, or location_coordinate, advertisers will be searched across all the available locations | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the function you used for setting a task possible values: advanced | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_ads_advertisers_task_post_request_info import SerpGoogleAdsAdvertisersTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleAdsAdvertisersTaskPostRequestInfo from a JSON string
serp_google_ads_advertisers_task_post_request_info_instance = SerpGoogleAdsAdvertisersTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleAdsAdvertisersTaskPostRequestInfo.to_json())

# convert the object into a dict
serp_google_ads_advertisers_task_post_request_info_dict = serp_google_ads_advertisers_task_post_request_info_instance.to_dict()
# create an instance of SerpGoogleAdsAdvertisersTaskPostRequestInfo from a dict
serp_google_ads_advertisers_task_post_request_info_from_dict = SerpGoogleAdsAdvertisersTaskPostRequestInfo.from_dict(serp_google_ads_advertisers_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



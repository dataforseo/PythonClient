# BusinessDataGoogleExtendedReviewsTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field if you don’t specify cid or place_id the keyword you specify should indicate the name of the local establishment; you can specify up to 700 characters in the keyword filed; all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if this field contains such parameters as ‘allinanchor:’, ‘allintext:’, ‘allintitle:’, ‘allinurl:’, ‘define:’, ‘filetype:’, ‘id:’, ‘inanchor:’, ‘info:’, ‘intext:’, ‘intitle:’, ‘inurl:’, ‘link:’, ‘related:’, ‘site:’, the charge per task will be multiplied by 5 Note: queries containing the ‘cache:’ parameter are not supported and will return a validation error learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article Note: if you use this field, your account will be charged three times the standard rate for tasks involving the Google Reviews API | [optional] 
**cid** | **str** | unique, google-defined id of the business entity required field if you don’t specify keyword or place_id example: 194604053573767737 learn more about the identifier in this help center article Note: if you use this field, your account will be charged two times the standard rate for tasks involving the Google Reviews API | [optional] 
**place_id** | **str** | identifier of the business entity in Google Maps required field if you don’t specify keyword or cid example: GhIJQWDl0CIeQUARxks3icF8U8A learn more about the identifier in this help center article Note: if you use this field, your account will be charged two times the standard rate for tasks involving the Google Reviews API | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations with location_name by making a separate request to the https://api.dataforseo.com/v3/business_data/google/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/google/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 199.9 example: 53.476225,-2.243572,200 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages with language_name by making a separate request to the https://api.dataforseo.com/v3/business_data/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/business_data/google/languages example: en | [optional] 
**depth** | **int** | parsing depth optional field number of reviews in SERP we strongly recommend setting the parsing depth in the multiples of twenty, because our systems processes twenty reviews in a row default value: 20 maximum value: 700 | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_extended_reviews_task_post_request_info import BusinessDataGoogleExtendedReviewsTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleExtendedReviewsTaskPostRequestInfo from a JSON string
business_data_google_extended_reviews_task_post_request_info_instance = BusinessDataGoogleExtendedReviewsTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataGoogleExtendedReviewsTaskPostRequestInfo.to_json())

# convert the object into a dict
business_data_google_extended_reviews_task_post_request_info_dict = business_data_google_extended_reviews_task_post_request_info_instance.to_dict()
# create an instance of BusinessDataGoogleExtendedReviewsTaskPostRequestInfo from a dict
business_data_google_extended_reviews_task_post_request_info_from_dict = BusinessDataGoogleExtendedReviewsTaskPostRequestInfo.from_dict(business_data_google_extended_reviews_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MerchantGoogleProductInfoTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | unique product identifier on Google Shopping required field if data_docid is not specified you can get this value for a certain product by making a separate request to the Google Shopping Products endpoint example: 4485466949985702538 learn more about the parameter in this help center guide | [optional] 
**data_docid** | **str** | unique identifier of the SERP data element required field if product_id is not specified you can get this value for a certain element by making a separate request to the Google Shopping Products endpoint example: 13071766526042404278 | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available Google Shopping locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/merchant/google/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available Google Shopping locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/merchant/google/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 199.9 example: 53.476225,-2.243572,200 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available Google Shopping languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/merchant/google/languages example: English | [optional] 
**language_code** | **str** | language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available Google Shopping languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/merchant/google/languages example: en | [optional] 
**se_domain** | **str** | search engine domain optional field we choose the relevant search engine domain automatically according to the location and language you specify however, you can set a custom search engine domain in this field example: google.co.uk, google.com.au, google.de, etc. | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible values: advanced, html | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.merchant_google_product_info_task_post_request_info import MerchantGoogleProductInfoTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGoogleProductInfoTaskPostRequestInfo from a JSON string
merchant_google_product_info_task_post_request_info_instance = MerchantGoogleProductInfoTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantGoogleProductInfoTaskPostRequestInfo.to_json())

# convert the object into a dict
merchant_google_product_info_task_post_request_info_dict = merchant_google_product_info_task_post_request_info_instance.to_dict()
# create an instance of MerchantGoogleProductInfoTaskPostRequestInfo from a dict
merchant_google_product_info_task_post_request_info_from_dict = MerchantGoogleProductInfoTaskPostRequestInfo.from_dict(merchant_google_product_info_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppDataGoogleAppInfoTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | id of the app required field ID of the mobile application on Google Play; you can find the ID in the URL of every app listed on Google Play; example: in the URL https://play.google.com/store/apps/details?id&#x3D;org.telegram.messenger the id is org.telegram.messenger | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code if you use this field, you don’t need to specify location_code you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/app_data/google/locations example: West Los Angeles,California,United States | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name if you use this field, you don’t need to specify location_name you can receive the list of available locations of the search engine with their location_code by making a separate request to https://api.dataforseo.com/v3/app_data/google/locations example: 9061121 | [optional] 
**language_name** | **str** | full name of search engine language required field if language_code is not specified if you use this field, you don’t need to specify language_code you can receive the list of available languages with language_name by making a separate request to https://api.dataforseo.com/v3/app_data/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if language_name is not specified if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/app_data/google/languages example: en | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible values: advanced, html | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 | [optional] 

## Example

```python
from dataforseo_client.models.app_data_google_app_info_task_post_request_info import AppDataGoogleAppInfoTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataGoogleAppInfoTaskPostRequestInfo from a JSON string
app_data_google_app_info_task_post_request_info_instance = AppDataGoogleAppInfoTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataGoogleAppInfoTaskPostRequestInfo.to_json())

# convert the object into a dict
app_data_google_app_info_task_post_request_info_dict = app_data_google_app_info_task_post_request_info_instance.to_dict()
# create an instance of AppDataGoogleAppInfoTaskPostRequestInfo from a dict
app_data_google_app_info_task_post_request_info_from_dict = AppDataGoogleAppInfoTaskPostRequestInfo.from_dict(app_data_google_app_info_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



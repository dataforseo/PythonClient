# SerpGoogleDatasetInfoTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | ID of the dataset required field you can find dataset ID in the dataset URL or dataset item of Google Dataset Search result example: L2cvMTFqbl85ZHN6MQ&#x3D;&#x3D; | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**language_name** | **str** | full name of search engine language optional field if you use this field, you don’t need to specify language_code possible value: English | [optional] 
**language_code** | **str** | search engine language code optional field if you use this field, you don’t need to specify language_name possible value: en | [optional] 
**device** | **str** | device type optional field possible value: desktop | [optional] 
**os** | **str** | device operating system optional field choose from the following values: windows, macos default value: windows | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible value: advanced | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_dataset_info_task_post_request_info import SerpGoogleDatasetInfoTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleDatasetInfoTaskPostRequestInfo from a JSON string
serp_google_dataset_info_task_post_request_info_instance = SerpGoogleDatasetInfoTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleDatasetInfoTaskPostRequestInfo.to_json())

# convert the object into a dict
serp_google_dataset_info_task_post_request_info_dict = serp_google_dataset_info_task_post_request_info_instance.to_dict()
# create an instance of SerpGoogleDatasetInfoTaskPostRequestInfo from a dict
serp_google_dataset_info_task_post_request_info_from_dict = SerpGoogleDatasetInfoTaskPostRequestInfo.from_dict(serp_google_dataset_info_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



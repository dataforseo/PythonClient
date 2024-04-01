# BusinessDataTrustpilotSearchTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field the keyword you specify should indicate a business category or company name; you can specify up to 700 symbols in the keyword filed; all %## will be decoded (plus symbol ‘+’ will be decoded to a space character); if you need to use the “%” symbol for your keyword, please specify it as “%25” | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**depth** | **int** | parsing depth optional field number of search results to be returned from the API response we strongly recommend setting the parsing depth in the multiples of twenty because our systems processes twenty search results in a row; default value: 10; maximum value: 140 Note: your account will be charged for every 10 search results returned, e.g. if you specify depth: 11, you will be charged as per 20 search results | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 

## Example

```python
from dataforseo_client.models.business_data_trustpilot_search_task_post_request_info import BusinessDataTrustpilotSearchTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataTrustpilotSearchTaskPostRequestInfo from a JSON string
business_data_trustpilot_search_task_post_request_info_instance = BusinessDataTrustpilotSearchTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataTrustpilotSearchTaskPostRequestInfo.to_json())

# convert the object into a dict
business_data_trustpilot_search_task_post_request_info_dict = business_data_trustpilot_search_task_post_request_info_instance.to_dict()
# create an instance of BusinessDataTrustpilotSearchTaskPostRequestInfo from a dict
business_data_trustpilot_search_task_post_request_info_form_dict = business_data_trustpilot_search_task_post_request_info.from_dict(business_data_trustpilot_search_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



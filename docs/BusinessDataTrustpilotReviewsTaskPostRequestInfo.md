# BusinessDataTrustpilotReviewsTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | domain of the local establishment required field domain of the local establishment on Trustpilot; you can find the domain in the URL of every business listed on Trustpilot example: www.thepearlsource.com https://www.trustpilot.com/review/www.thepearlsource.com | [optional] 
**sort_by** | **str** | results sorting parameter optional field you can use this field to sort the results; possible sorting parameters: recency — most recent reviews first; relevance — most relevant reviews first; default value: relevance | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**depth** | **int** | parsing depth optional field number of reviews to be returned from the API response we strongly recommend setting the parsing depth in the multiples of twenty, because our system processes twenty reviews in a row default value: 20 maximum value: 25000 | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 learn more on our Help Center | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.business_data_trustpilot_reviews_task_post_request_info import BusinessDataTrustpilotReviewsTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataTrustpilotReviewsTaskPostRequestInfo from a JSON string
business_data_trustpilot_reviews_task_post_request_info_instance = BusinessDataTrustpilotReviewsTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataTrustpilotReviewsTaskPostRequestInfo.to_json()

# convert the object into a dict
business_data_trustpilot_reviews_task_post_request_info_dict = business_data_trustpilot_reviews_task_post_request_info_instance.to_dict()
# create an instance of BusinessDataTrustpilotReviewsTaskPostRequestInfo from a dict
business_data_trustpilot_reviews_task_post_request_info_form_dict = business_data_trustpilot_reviews_task_post_request_info.from_dict(business_data_trustpilot_reviews_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



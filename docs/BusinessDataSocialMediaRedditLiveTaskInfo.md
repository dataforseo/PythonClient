# BusinessDataSocialMediaRedditLiveTaskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier unique task identifier in our system in the UUID format | [optional] 
**status_code** | **int** | status code of the task generated by DataForSEO, can be within the following range: 10000-60000 you can find the full list of the response codes here | [optional] 
**status_message** | **str** | informational message of the task you can find the full list of general informational messages here | [optional] 
**time** | **str** | execution time, seconds | [optional] 
**cost** | **float** | total tasks cost, USD | [optional] 
**result_count** | **int** | number of elements in the result array | [optional] 
**path** | **List[Optional[str]]** | URL path | [optional] 
**data** | **object** | contains the same parameters that you specified in the POST request | [optional] 
**result** | [**List[BusinessDataSocialMediaRedditLiveResultInfo]**](BusinessDataSocialMediaRedditLiveResultInfo.md) | array of results | [optional] 

## Example

```python
from dataforseo_client.models.business_data_social_media_reddit_live_task_info import BusinessDataSocialMediaRedditLiveTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataSocialMediaRedditLiveTaskInfo from a JSON string
business_data_social_media_reddit_live_task_info_instance = BusinessDataSocialMediaRedditLiveTaskInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataSocialMediaRedditLiveTaskInfo.to_json())

# convert the object into a dict
business_data_social_media_reddit_live_task_info_dict = business_data_social_media_reddit_live_task_info_instance.to_dict()
# create an instance of BusinessDataSocialMediaRedditLiveTaskInfo from a dict
business_data_social_media_reddit_live_task_info_from_dict = BusinessDataSocialMediaRedditLiveTaskInfo.from_dict(business_data_social_media_reddit_live_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



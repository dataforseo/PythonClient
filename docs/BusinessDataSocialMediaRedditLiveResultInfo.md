# BusinessDataSocialMediaRedditLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**page_url** | **str** | URL of the page the data is provided for corresponding URL you specified in the targets array when setting a task | [optional] 
**reddit_reviews** | [**List[RedditReviews]**](RedditReviews.md) | reddit reviews for the page_url | [optional] 

## Example

```python
from dataforseo_client.models.business_data_social_media_reddit_live_result_info import BusinessDataSocialMediaRedditLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataSocialMediaRedditLiveResultInfo from a JSON string
business_data_social_media_reddit_live_result_info_instance = BusinessDataSocialMediaRedditLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataSocialMediaRedditLiveResultInfo.to_json())

# convert the object into a dict
business_data_social_media_reddit_live_result_info_dict = business_data_social_media_reddit_live_result_info_instance.to_dict()
# create an instance of BusinessDataSocialMediaRedditLiveResultInfo from a dict
business_data_social_media_reddit_live_result_info_from_dict = BusinessDataSocialMediaRedditLiveResultInfo.from_dict(business_data_social_media_reddit_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



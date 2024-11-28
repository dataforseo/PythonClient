# BusinessDataSocialMediaFacebookLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**page_url** | **str** | URL of the page the data is provided for corresponding URL you specified in the targets array when setting a task | [optional] 
**like_count** | **int** | number of likes for the related page_url this field shows the number of likes a page received through the Facebook Like Button embed | [optional] 

## Example

```python
from dataforseo_client.models.business_data_social_media_facebook_live_result_info import BusinessDataSocialMediaFacebookLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataSocialMediaFacebookLiveResultInfo from a JSON string
business_data_social_media_facebook_live_result_info_instance = BusinessDataSocialMediaFacebookLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataSocialMediaFacebookLiveResultInfo.to_json())

# convert the object into a dict
business_data_social_media_facebook_live_result_info_dict = business_data_social_media_facebook_live_result_info_instance.to_dict()
# create an instance of BusinessDataSocialMediaFacebookLiveResultInfo from a dict
business_data_social_media_facebook_live_result_info_from_dict = BusinessDataSocialMediaFacebookLiveResultInfo.from_dict(business_data_social_media_facebook_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



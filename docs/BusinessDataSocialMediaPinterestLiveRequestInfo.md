# BusinessDataSocialMediaPinterestLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | **List[str]** | target URLs required field target page should be specified with its absolute URL (including http:// or https://) example: https://dataforseo.com/ Note: you can specify 10 targets maximum. You will be charged per earch URL you specify in this array | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.business_data_social_media_pinterest_live_request_info import BusinessDataSocialMediaPinterestLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataSocialMediaPinterestLiveRequestInfo from a JSON string
business_data_social_media_pinterest_live_request_info_instance = BusinessDataSocialMediaPinterestLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataSocialMediaPinterestLiveRequestInfo.to_json())

# convert the object into a dict
business_data_social_media_pinterest_live_request_info_dict = business_data_social_media_pinterest_live_request_info_instance.to_dict()
# create an instance of BusinessDataSocialMediaPinterestLiveRequestInfo from a dict
business_data_social_media_pinterest_live_request_info_form_dict = business_data_social_media_pinterest_live_request_info.from_dict(business_data_social_media_pinterest_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



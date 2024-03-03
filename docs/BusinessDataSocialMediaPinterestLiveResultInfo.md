# BusinessDataSocialMediaPinterestLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**page_url** | **str** | URL of the page the data is provided for corresponding URL you specified in the targets array when setting a task | [optional] 
**pins_count** | **int** | number of pins for the related page_url pins on Pinterest correspond to content saves; this field shows the number of content saves made from the related page_url using the Pinterest Save Button | [optional] 

## Example

```python
from dataforseo_client.models.business_data_social_media_pinterest_live_result_info import BusinessDataSocialMediaPinterestLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataSocialMediaPinterestLiveResultInfo from a JSON string
business_data_social_media_pinterest_live_result_info_instance = BusinessDataSocialMediaPinterestLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataSocialMediaPinterestLiveResultInfo.to_json()

# convert the object into a dict
business_data_social_media_pinterest_live_result_info_dict = business_data_social_media_pinterest_live_result_info_instance.to_dict()
# create an instance of BusinessDataSocialMediaPinterestLiveResultInfo from a dict
business_data_social_media_pinterest_live_result_info_form_dict = business_data_social_media_pinterest_live_result_info.from_dict(business_data_social_media_pinterest_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppUserProfileInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_name** | **str** | profile name of the reviewer | [optional] 
**profile_image_url** | **str** | URL to the reviewer’s profile image | [optional] 

## Example

```python
from dataforseo_client.models.app_user_profile_info import AppUserProfileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserProfileInfo from a JSON string
app_user_profile_info_instance = AppUserProfileInfo.from_json(json)
# print the JSON string representation of the object
print(AppUserProfileInfo.to_json())

# convert the object into a dict
app_user_profile_info_dict = app_user_profile_info_instance.to_dict()
# create an instance of AppUserProfileInfo from a dict
app_user_profile_info_from_dict = AppUserProfileInfo.from_dict(app_user_profile_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



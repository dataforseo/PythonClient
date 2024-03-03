# UserProfileInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the name of the reviewer | [optional] 
**avatar** | **str** | URL to the profile picture of the reviewer | [optional] 
**url** | **str** | URL to the reviewer’s profile | [optional] 
**reviews_count** | **int** | total number of reviews submitted by the reviewer | [optional] 
**locations** | **str** | country of the reviewer | [optional] 

## Example

```python
from dataforseo_client.models.user_profile_info import UserProfileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileInfo from a JSON string
user_profile_info_instance = UserProfileInfo.from_json(json)
# print the JSON string representation of the object
print UserProfileInfo.to_json()

# convert the object into a dict
user_profile_info_dict = user_profile_info_instance.to_dict()
# create an instance of UserProfileInfo from a dict
user_profile_info_form_dict = user_profile_info.from_dict(user_profile_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



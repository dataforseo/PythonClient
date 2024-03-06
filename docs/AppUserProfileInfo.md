[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

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
print AppUserProfileInfo.to_json()

# convert the object into a dict
app_user_profile_info_dict = app_user_profile_info_instance.to_dict()
# create an instance of AppUserProfileInfo from a dict
app_user_profile_info_form_dict = app_user_profile_info.from_dict(app_user_profile_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
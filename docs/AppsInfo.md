# AppsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | ID of the app | [optional] 
**title** | **str** | title of the app | [optional] 
**url** | **str** | URL to the app page on Google Play | [optional] 

## Example

```python
from dataforseo_client.models.apps_info import AppsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppsInfo from a JSON string
apps_info_instance = AppsInfo.from_json(json)
# print the JSON string representation of the object
print AppsInfo.to_json()

# convert the object into a dict
apps_info_dict = apps_info_instance.to_dict()
# create an instance of AppsInfo from a dict
apps_info_form_dict = apps_info.from_dict(apps_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



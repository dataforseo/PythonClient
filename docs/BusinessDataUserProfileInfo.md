# BusinessDataUserProfileInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the name of the reviewer | [optional] 
**url** | **str** | URL to the reviewer’s profile | [optional] 
**image_url** | **str** | URL to the reviewer’s profile picture | [optional] 
**location** | **str** | country of the reviewer | [optional] 
**reviews_count** | **int** | total number of reviews submitted by the reviewer | [optional] 

## Example

```python
from dataforseo_client.models.business_data_user_profile_info import BusinessDataUserProfileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataUserProfileInfo from a JSON string
business_data_user_profile_info_instance = BusinessDataUserProfileInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataUserProfileInfo.to_json())

# convert the object into a dict
business_data_user_profile_info_dict = business_data_user_profile_info_instance.to_dict()
# create an instance of BusinessDataUserProfileInfo from a dict
business_data_user_profile_info_from_dict = BusinessDataUserProfileInfo.from_dict(business_data_user_profile_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



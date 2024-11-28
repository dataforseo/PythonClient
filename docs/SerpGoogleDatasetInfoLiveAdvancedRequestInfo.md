# SerpGoogleDatasetInfoLiveAdvancedRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | ID of the dataset required field you can find dataset ID in the dataset URL or dataset item of Google Dataset Search result example: L2cvMTFqbl85ZHN6MQ&#x3D;&#x3D; | [optional] 
**language_name** | **str** | full name of search engine language optional field if you use this field, you don’t need to specify language_code possible value: English | [optional] 
**language_code** | **str** | search engine language code optional field if you use this field, you don’t need to specify language_name possible value: en | [optional] 
**device** | **str** | device type optional field possible value: desktop | [optional] 
**os** | **str** | device operating system optional field possible values: windows, macos default value: windows | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_dataset_info_live_advanced_request_info import SerpGoogleDatasetInfoLiveAdvancedRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleDatasetInfoLiveAdvancedRequestInfo from a JSON string
serp_google_dataset_info_live_advanced_request_info_instance = SerpGoogleDatasetInfoLiveAdvancedRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleDatasetInfoLiveAdvancedRequestInfo.to_json())

# convert the object into a dict
serp_google_dataset_info_live_advanced_request_info_dict = serp_google_dataset_info_live_advanced_request_info_instance.to_dict()
# create an instance of SerpGoogleDatasetInfoLiveAdvancedRequestInfo from a dict
serp_google_dataset_info_live_advanced_request_info_from_dict = SerpGoogleDatasetInfoLiveAdvancedRequestInfo.from_dict(serp_google_dataset_info_live_advanced_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



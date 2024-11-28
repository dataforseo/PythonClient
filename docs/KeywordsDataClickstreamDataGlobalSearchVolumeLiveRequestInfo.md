# KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | target keywords required field UTF-8 encoding maximum number of keywords you can specify in this array: 1000; each keyword should be at least 3 characters long; the keywords will be converted to lowercase format; Note: certain symbols and characters (e.g., UTF symbols, emojis) are not allowed to learn more about which symbols and characters can be used, please refer to this article learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_global_search_volume_live_request_info import KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo from a JSON string
keywords_data_clickstream_data_global_search_volume_live_request_info_instance = KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo.to_json())

# convert the object into a dict
keywords_data_clickstream_data_global_search_volume_live_request_info_dict = keywords_data_clickstream_data_global_search_volume_live_request_info_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo from a dict
keywords_data_clickstream_data_global_search_volume_live_request_info_from_dict = KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo.from_dict(keywords_data_clickstream_data_global_search_volume_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



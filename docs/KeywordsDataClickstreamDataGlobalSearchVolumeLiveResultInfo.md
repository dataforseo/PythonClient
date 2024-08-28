# KeywordsDataClickstreamDataGlobalSearchVolumeLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem]**](KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem.md) | contains keywords and related data | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_global_search_volume_live_result_info import KeywordsDataClickstreamDataGlobalSearchVolumeLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataGlobalSearchVolumeLiveResultInfo from a JSON string
keywords_data_clickstream_data_global_search_volume_live_result_info_instance = KeywordsDataClickstreamDataGlobalSearchVolumeLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataClickstreamDataGlobalSearchVolumeLiveResultInfo.to_json()

# convert the object into a dict
keywords_data_clickstream_data_global_search_volume_live_result_info_dict = keywords_data_clickstream_data_global_search_volume_live_result_info_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataGlobalSearchVolumeLiveResultInfo from a dict
keywords_data_clickstream_data_global_search_volume_live_result_info_form_dict = keywords_data_clickstream_data_global_search_volume_live_result_info.from_dict(keywords_data_clickstream_data_global_search_volume_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



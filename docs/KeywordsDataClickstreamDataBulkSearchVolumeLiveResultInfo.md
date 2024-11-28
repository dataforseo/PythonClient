# KeywordsDataClickstreamDataBulkSearchVolumeLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code in a POST array | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[KeywordsDataClickstreamDataSearchVolumeLiveItem]**](KeywordsDataClickstreamDataSearchVolumeLiveItem.md) | contains keywords and related data | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_bulk_search_volume_live_result_info import KeywordsDataClickstreamDataBulkSearchVolumeLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataBulkSearchVolumeLiveResultInfo from a JSON string
keywords_data_clickstream_data_bulk_search_volume_live_result_info_instance = KeywordsDataClickstreamDataBulkSearchVolumeLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataClickstreamDataBulkSearchVolumeLiveResultInfo.to_json())

# convert the object into a dict
keywords_data_clickstream_data_bulk_search_volume_live_result_info_dict = keywords_data_clickstream_data_bulk_search_volume_live_result_info_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataBulkSearchVolumeLiveResultInfo from a dict
keywords_data_clickstream_data_bulk_search_volume_live_result_info_from_dict = KeywordsDataClickstreamDataBulkSearchVolumeLiveResultInfo.from_dict(keywords_data_clickstream_data_bulk_search_volume_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



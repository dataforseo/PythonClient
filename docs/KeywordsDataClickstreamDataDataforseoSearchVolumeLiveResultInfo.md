# KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **str** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array  Note:if the keyword in the POST array appears to be misspelled, data will be returned for the correctly spelled keyword; we use the functionality of Google Ads API to check and validate the spelling of keywords, learn more by this link | [optional] 
**use_clickstream** | **bool** | indicates if the use_clickstream parameter is active possible values: true, false | [optional] 
**items_count** | **str** | ithe number of results returned in the items array | [optional] 
**items** | [**List[KeywordsDataClickstreamDataSearchVolumeLiveItem]**](KeywordsDataClickstreamDataSearchVolumeLiveItem.md) | array of keywords contains keywords and their search volume rates | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_dataforseo_search_volume_live_result_info import KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResultInfo from a JSON string
keywords_data_clickstream_data_dataforseo_search_volume_live_result_info_instance = KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResultInfo.to_json())

# convert the object into a dict
keywords_data_clickstream_data_dataforseo_search_volume_live_result_info_dict = keywords_data_clickstream_data_dataforseo_search_volume_live_result_info_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResultInfo from a dict
keywords_data_clickstream_data_dataforseo_search_volume_live_result_info_from_dict = KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResultInfo.from_dict(keywords_data_clickstream_data_dataforseo_search_volume_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



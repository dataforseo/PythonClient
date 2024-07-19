# KeywordsDataBingSearchVolumeHistoryLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword in a POST array | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**device** | **List[Optional[str]]** |  | [optional] 
**period** | **str** | time period indicates if returned data is aggregated to a certain time period default value monthly | [optional] 
**searches** | [**SearchVolumeHistorySearchInfo**](SearchVolumeHistorySearchInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_search_volume_history_live_result_info import KeywordsDataBingSearchVolumeHistoryLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingSearchVolumeHistoryLiveResultInfo from a JSON string
keywords_data_bing_search_volume_history_live_result_info_instance = KeywordsDataBingSearchVolumeHistoryLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataBingSearchVolumeHistoryLiveResultInfo.to_json()

# convert the object into a dict
keywords_data_bing_search_volume_history_live_result_info_dict = keywords_data_bing_search_volume_history_live_result_info_instance.to_dict()
# create an instance of KeywordsDataBingSearchVolumeHistoryLiveResultInfo from a dict
keywords_data_bing_search_volume_history_live_result_info_form_dict = keywords_data_bing_search_volume_history_live_result_info.from_dict(keywords_data_bing_search_volume_history_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



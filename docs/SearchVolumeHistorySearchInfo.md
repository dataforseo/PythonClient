# SearchVolumeHistorySearchInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desktop** | [**List[SearchVolumeHistoryItemInfo]**](SearchVolumeHistoryItemInfo.md) | device type &#x3D; desktop contains historical search volume data for searches made from desktop devices | [optional] 
**non_smartphones** | [**List[SearchVolumeHistoryItemInfo]**](SearchVolumeHistoryItemInfo.md) | device type &#x3D; non-smartphones contains historical search volume data for searches made from feature phones (non-smartphone mobile devices) | [optional] 
**mobile** | [**List[SearchVolumeHistoryItemInfo]**](SearchVolumeHistoryItemInfo.md) | device type &#x3D; mobile contains historical search volume data for searches made from mobile devices | [optional] 
**tablet** | [**List[SearchVolumeHistoryItemInfo]**](SearchVolumeHistoryItemInfo.md) | device type &#x3D; tablet contains historical search volume data for searches made from tablets | [optional] 

## Example

```python
from dataforseo_client.models.search_volume_history_search_info import SearchVolumeHistorySearchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SearchVolumeHistorySearchInfo from a JSON string
search_volume_history_search_info_instance = SearchVolumeHistorySearchInfo.from_json(json)
# print the JSON string representation of the object
print SearchVolumeHistorySearchInfo.to_json()

# convert the object into a dict
search_volume_history_search_info_dict = search_volume_history_search_info_instance.to_dict()
# create an instance of SearchVolumeHistorySearchInfo from a dict
search_volume_history_search_info_form_dict = search_volume_history_search_info.from_dict(search_volume_history_search_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



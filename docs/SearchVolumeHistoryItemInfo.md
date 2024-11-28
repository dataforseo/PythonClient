# SearchVolumeHistoryItemInfo

device type = desktop contains historical search volume data for searches made from desktop devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | year | [optional] 
**month** | **int** | month | [optional] 
**day** | **int** | day of the month | [optional] 
**search_volume** | **int** | search volume rate | [optional] 

## Example

```python
from dataforseo_client.models.search_volume_history_item_info import SearchVolumeHistoryItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SearchVolumeHistoryItemInfo from a JSON string
search_volume_history_item_info_instance = SearchVolumeHistoryItemInfo.from_json(json)
# print the JSON string representation of the object
print(SearchVolumeHistoryItemInfo.to_json())

# convert the object into a dict
search_volume_history_item_info_dict = search_volume_history_item_info_instance.to_dict()
# create an instance of SearchVolumeHistoryItemInfo from a dict
search_volume_history_item_info_from_dict = SearchVolumeHistoryItemInfo.from_dict(search_volume_history_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



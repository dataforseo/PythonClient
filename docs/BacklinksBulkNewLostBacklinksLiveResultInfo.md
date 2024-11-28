# BacklinksBulkNewLostBacklinksLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BacklinksBulkNewLostBacklinksLiveItem]**](BacklinksBulkNewLostBacklinksLiveItem.md) | contains relevant backlinks and referring domains data | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_bulk_new_lost_backlinks_live_result_info import BacklinksBulkNewLostBacklinksLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkNewLostBacklinksLiveResultInfo from a JSON string
backlinks_bulk_new_lost_backlinks_live_result_info_instance = BacklinksBulkNewLostBacklinksLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksBulkNewLostBacklinksLiveResultInfo.to_json())

# convert the object into a dict
backlinks_bulk_new_lost_backlinks_live_result_info_dict = backlinks_bulk_new_lost_backlinks_live_result_info_instance.to_dict()
# create an instance of BacklinksBulkNewLostBacklinksLiveResultInfo from a dict
backlinks_bulk_new_lost_backlinks_live_result_info_from_dict = BacklinksBulkNewLostBacklinksLiveResultInfo.from_dict(backlinks_bulk_new_lost_backlinks_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



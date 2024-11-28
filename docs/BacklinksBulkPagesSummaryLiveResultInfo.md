# BacklinksBulkPagesSummaryLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | total number of relevant items in the database | [optional] 
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[BacklinksBulkPagesSummaryLiveItem]**](BacklinksBulkPagesSummaryLiveItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_bulk_pages_summary_live_result_info import BacklinksBulkPagesSummaryLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkPagesSummaryLiveResultInfo from a JSON string
backlinks_bulk_pages_summary_live_result_info_instance = BacklinksBulkPagesSummaryLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksBulkPagesSummaryLiveResultInfo.to_json())

# convert the object into a dict
backlinks_bulk_pages_summary_live_result_info_dict = backlinks_bulk_pages_summary_live_result_info_instance.to_dict()
# create an instance of BacklinksBulkPagesSummaryLiveResultInfo from a dict
backlinks_bulk_pages_summary_live_result_info_from_dict = BacklinksBulkPagesSummaryLiveResultInfo.from_dict(backlinks_bulk_pages_summary_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DataforseoLabsleBulkAppMetricsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**app_id** | **str** | id of the app in a POST array | [optional] 
**metrics** | [**Dict[str, AppMetricsInfo]**](AppMetricsInfo.md) | metrics for the ranking keywords of the app ranking data relevant to the keywords that the provided application ranks for on Google Play | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labsle_bulk_app_metrics_live_item import DataforseoLabsleBulkAppMetricsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsleBulkAppMetricsLiveItem from a JSON string
dataforseo_labsle_bulk_app_metrics_live_item_instance = DataforseoLabsleBulkAppMetricsLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsleBulkAppMetricsLiveItem.to_json())

# convert the object into a dict
dataforseo_labsle_bulk_app_metrics_live_item_dict = dataforseo_labsle_bulk_app_metrics_live_item_instance.to_dict()
# create an instance of DataforseoLabsleBulkAppMetricsLiveItem from a dict
dataforseo_labsle_bulk_app_metrics_live_item_from_dict = DataforseoLabsleBulkAppMetricsLiveItem.from_dict(dataforseo_labsle_bulk_app_metrics_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



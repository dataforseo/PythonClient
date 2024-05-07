# DataforseoLabsBBulkTrafficEstimationLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**target** | **str** | target domain in a POST array | [optional] 
**metrics** | [**Dict[str, BulkMetricsInfo]**](BulkMetricsInfo.md) | traffic data relevant to the specified domain | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_b_bulk_traffic_estimation_live_item import DataforseoLabsBBulkTrafficEstimationLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBBulkTrafficEstimationLiveItem from a JSON string
dataforseo_labs_b_bulk_traffic_estimation_live_item_instance = DataforseoLabsBBulkTrafficEstimationLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBBulkTrafficEstimationLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_b_bulk_traffic_estimation_live_item_dict = dataforseo_labs_b_bulk_traffic_estimation_live_item_instance.to_dict()
# create an instance of DataforseoLabsBBulkTrafficEstimationLiveItem from a dict
dataforseo_labs_b_bulk_traffic_estimation_live_item_form_dict = dataforseo_labs_b_bulk_traffic_estimation_live_item.from_dict(dataforseo_labs_b_bulk_traffic_estimation_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



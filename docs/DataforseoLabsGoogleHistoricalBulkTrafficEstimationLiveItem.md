# DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**target** | **str** | target domain in a POST array | [optional] 
**metrics** | [**HistoricalMetricsBundleInfo**](HistoricalMetricsBundleInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_historical_bulk_traffic_estimation_live_item import DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveItem from a JSON string
dataforseo_labs_google_historical_bulk_traffic_estimation_live_item_instance = DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_google_historical_bulk_traffic_estimation_live_item_dict = dataforseo_labs_google_historical_bulk_traffic_estimation_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveItem from a dict
dataforseo_labs_google_historical_bulk_traffic_estimation_live_item_form_dict = dataforseo_labs_google_historical_bulk_traffic_estimation_live_item.from_dict(dataforseo_labs_google_historical_bulk_traffic_estimation_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



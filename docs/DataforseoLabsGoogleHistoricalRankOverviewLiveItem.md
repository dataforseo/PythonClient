# DataforseoLabsGoogleHistoricalRankOverviewLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**year** | **int** | year for which the data is provided | [optional] 
**month** | **int** | month for which the data is provided | [optional] 
**metrics** | [**Dict[str, DataforseoLabsMetricsInfo]**](DataforseoLabsMetricsInfo.md) | ranking data relevant to the specified domain | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_historical_rank_overview_live_item import DataforseoLabsGoogleHistoricalRankOverviewLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleHistoricalRankOverviewLiveItem from a JSON string
dataforseo_labs_google_historical_rank_overview_live_item_instance = DataforseoLabsGoogleHistoricalRankOverviewLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleHistoricalRankOverviewLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_google_historical_rank_overview_live_item_dict = dataforseo_labs_google_historical_rank_overview_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleHistoricalRankOverviewLiveItem from a dict
dataforseo_labs_google_historical_rank_overview_live_item_from_dict = DataforseoLabsGoogleHistoricalRankOverviewLiveItem.from_dict(dataforseo_labs_google_historical_rank_overview_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



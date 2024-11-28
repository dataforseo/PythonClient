# BacklinksTimeseriesNewLostSummaryLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | target from a POST array | [optional] 
**date_from** | **str** | starting date of the time range in the UTC format: “yyyy-mm-dd” example: 2019-01-01 | [optional] 
**date_to** | **str** | ending date of the time range in the UTC format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**group_range** | **str** | group_range from the POST array | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BacklinksTimeseriesNewLostSummaryLiveItem]**](BacklinksTimeseriesNewLostSummaryLiveItem.md) | contains relevant backlinks and referring domains data | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_timeseries_new_lost_summary_live_result_info import BacklinksTimeseriesNewLostSummaryLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksTimeseriesNewLostSummaryLiveResultInfo from a JSON string
backlinks_timeseries_new_lost_summary_live_result_info_instance = BacklinksTimeseriesNewLostSummaryLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksTimeseriesNewLostSummaryLiveResultInfo.to_json())

# convert the object into a dict
backlinks_timeseries_new_lost_summary_live_result_info_dict = backlinks_timeseries_new_lost_summary_live_result_info_instance.to_dict()
# create an instance of BacklinksTimeseriesNewLostSummaryLiveResultInfo from a dict
backlinks_timeseries_new_lost_summary_live_result_info_from_dict = BacklinksTimeseriesNewLostSummaryLiveResultInfo.from_dict(backlinks_timeseries_new_lost_summary_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



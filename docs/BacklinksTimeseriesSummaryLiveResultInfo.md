# BacklinksTimeseriesSummaryLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | target from a POST array | [optional] 
**date_from** | **str** | starting date of the time range in the UTC format: “yyyy-mm-dd” example: 2019-01-01 | [optional] 
**date_to** | **str** | ending date of the time range in the UTC format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**group_range** | **str** | group_range from a POST array | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BacklinksTimeseriesSummaryLiveItem]**](BacklinksTimeseriesSummaryLiveItem.md) | contains relevant summary data | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_timeseries_summary_live_result_info import BacklinksTimeseriesSummaryLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksTimeseriesSummaryLiveResultInfo from a JSON string
backlinks_timeseries_summary_live_result_info_instance = BacklinksTimeseriesSummaryLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksTimeseriesSummaryLiveResultInfo.to_json()

# convert the object into a dict
backlinks_timeseries_summary_live_result_info_dict = backlinks_timeseries_summary_live_result_info_instance.to_dict()
# create an instance of BacklinksTimeseriesSummaryLiveResultInfo from a dict
backlinks_timeseries_summary_live_result_info_form_dict = backlinks_timeseries_summary_live_result_info.from_dict(backlinks_timeseries_summary_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



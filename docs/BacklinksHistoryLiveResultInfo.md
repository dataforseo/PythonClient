# BacklinksHistoryLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | target from the POST array | [optional] 
**date_from** | **str** | starting date of the time range in the UTC format: “yyyy-mm-dd” example: 2019-01-01 | [optional] 
**date_to** | **str** | ending date of the time range in the UTC format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BacklinksHistoryLiveItem]**](BacklinksHistoryLiveItem.md) | contains historical backlink data for the specified domain the data is provided month-by-month; the metrics are aggregated according to the backlinks the specified domain had on the first day of each given month | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_history_live_result_info import BacklinksHistoryLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksHistoryLiveResultInfo from a JSON string
backlinks_history_live_result_info_instance = BacklinksHistoryLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksHistoryLiveResultInfo.to_json())

# convert the object into a dict
backlinks_history_live_result_info_dict = backlinks_history_live_result_info_instance.to_dict()
# create an instance of BacklinksHistoryLiveResultInfo from a dict
backlinks_history_live_result_info_from_dict = BacklinksHistoryLiveResultInfo.from_dict(backlinks_history_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



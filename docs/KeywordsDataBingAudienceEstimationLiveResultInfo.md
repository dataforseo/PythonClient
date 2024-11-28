# KeywordsDataBingAudienceEstimationLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**est_impressions** | [**EstInfo**](EstInfo.md) |  | [optional] 
**est_audience_size** | [**EstInfo**](EstInfo.md) |  | [optional] 
**est_clicks** | [**EstInfo**](EstInfo.md) |  | [optional] 
**est_spend** | [**EstInfo**](EstInfo.md) |  | [optional] 
**est_cost_per_event** | [**EstCInfo**](EstCInfo.md) |  | [optional] 
**est_ctr** | [**EstCInfo**](EstCInfo.md) |  | [optional] 
**suggested_bid** | **float** | suggested bid value under the current targeting | [optional] 
**suggested_budget** | **float** | suggested daily budget value under the current targeting and bid | [optional] 
**events_lost_to_bid** | **int** | indicates event lost count due to insufficient input bid | [optional] 
**events_lost_to_budget** | **int** | indicates the event lost count due to insufficient input budget | [optional] 
**est_reach_audience_size** | **int** | monthly estimated user count | [optional] 
**est_reach_impressions** | **int** | monthly estimated impressions | [optional] 
**currency** | **str** | currency name example: USDollar | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_audience_estimation_live_result_info import KeywordsDataBingAudienceEstimationLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingAudienceEstimationLiveResultInfo from a JSON string
keywords_data_bing_audience_estimation_live_result_info_instance = KeywordsDataBingAudienceEstimationLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataBingAudienceEstimationLiveResultInfo.to_json())

# convert the object into a dict
keywords_data_bing_audience_estimation_live_result_info_dict = keywords_data_bing_audience_estimation_live_result_info_instance.to_dict()
# create an instance of KeywordsDataBingAudienceEstimationLiveResultInfo from a dict
keywords_data_bing_audience_estimation_live_result_info_from_dict = KeywordsDataBingAudienceEstimationLiveResultInfo.from_dict(keywords_data_bing_audience_estimation_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword in a POST array | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**date_interval** | **str** | forecasting date interval in a POST array | [optional] 
**search_partners** | **bool** | include Google search partners the value you specified when setting the task if true, the results are returned for owned, operated, and syndicated networks across Google and partner sites that host Google search; if false, the results are returned for Google search sites only | [optional] 
**bid** | **int** | the maximum custom bid the bid you have specified when setting the task represents the price you are willing to pay for an ad the higher value you have specified, the higher metrics and cost you receive in response learn more in this help center article | [optional] 
**match** | **str** | keywords match-type can take the following values: exact, broad, phrase | [optional] 
**impressions** | **float** | projected number of ad impressions number of impressions an ad is projected to get within the specified time period if there is no data, then the value is null learn more about impressions in this help center article | [optional] 
**ctr** | **float** | projected click through rate (CTR) of the advertisement number of clicks an ad is projected to receive divided by the number of ad impressions; the CTR is projected for the specified time period if there is no data, then the value is null | [optional] 
**average_cpc** | **float** | the average cost-per-click value represents the cost-per-click (USD) estimated for a keyword based on the specified time period and historical data; if there is no data, then the value is null | [optional] 
**cost** | **float** | charge for an ad amount that will be charged for running an ad within the specified time period if there is no data, then the value is null | [optional] 
**clicks** | **float** | number of clicks on an ad number of clicks an ad is projected to get within the specified time period if there is no data, then the value is null | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_google_ads_ad_traffic_by_keywords_live_result_info import KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResultInfo from a JSON string
keywords_data_google_ads_ad_traffic_by_keywords_live_result_info_instance = KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResultInfo.to_json())

# convert the object into a dict
keywords_data_google_ads_ad_traffic_by_keywords_live_result_info_dict = keywords_data_google_ads_ad_traffic_by_keywords_live_result_info_instance.to_dict()
# create an instance of KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResultInfo from a dict
keywords_data_google_ads_ad_traffic_by_keywords_live_result_info_from_dict = KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResultInfo.from_dict(keywords_data_google_ads_ad_traffic_by_keywords_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



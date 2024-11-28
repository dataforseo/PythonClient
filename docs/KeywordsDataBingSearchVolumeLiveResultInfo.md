# KeywordsDataBingSearchVolumeLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword in a POST array | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**search_partners** | **bool** | indicates whether data from partner networks included in the response | [optional] 
**device** | **str** | device type in a POST array if there is no data, then the value is null | [optional] 
**competition** | **float** | competition represents the relative amount of competition associated with the given keyword in paid SERP only. This value is based on Bing Ads data. Possible values: 0.1, 0.5,0.90.1 – low competition, 0.5 – medium competition, 0.9 – high competition; if there is no data the value is null | [optional] 
**cpc** | **float** | cost-per-click represents the average cost per click (USD) historically paid for the keyword. if there is no data then the value is null | [optional] 
**search_volume** | **int** | monthly average search volume rate represents either the (approximate) number of searches for the given keyword idea on bing search engine depending on the user’s targeting; search volume is rounded to the nearest tens; if there is no data, the value is null | [optional] 
**categories** | **List[Optional[str]]** | product and service categories our API doesn’t return categories for this endpoint: the parameter will always equal null | [optional] 
**monthly_searches** | [**List[MonthlySearches]**](MonthlySearches.md) | monthly searches represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations if there is no data then the value is null | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_search_volume_live_result_info import KeywordsDataBingSearchVolumeLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingSearchVolumeLiveResultInfo from a JSON string
keywords_data_bing_search_volume_live_result_info_instance = KeywordsDataBingSearchVolumeLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataBingSearchVolumeLiveResultInfo.to_json())

# convert the object into a dict
keywords_data_bing_search_volume_live_result_info_dict = keywords_data_bing_search_volume_live_result_info_instance.to_dict()
# create an instance of KeywordsDataBingSearchVolumeLiveResultInfo from a dict
keywords_data_bing_search_volume_live_result_info_from_dict = KeywordsDataBingSearchVolumeLiveResultInfo.from_dict(keywords_data_bing_search_volume_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# KeywordsDataBingKeywordsForKeywordsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword in a POST array | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**search_partners** | **bool** | indicates whether data from partner networks is included in the response | [optional] 
**device** | **str** | device type indicates for what device type the data is provided; possible values: all, mobile, desktop, tablet | [optional] 
**competition** | **float** | competition represents the relative amount of competition associated with the given keyword in paid SERP only. This value is based on Bing Ads data. Possible values: 0.1, 0.5,0.90.1 – low competition, 0.5 – medium competition, 0.9 – high competition; if there is no data the value is null | [optional] 
**cpc** | **float** | cost-per-click represents the average cost per click (USD) historically paid for the keyword. if there is no data, then the value is null | [optional] 
**search_volume** | **int** | monthly average search volume rate represents the (approximate) number of searches for the keyword on the Bing search engine, depending on the user’s targetingsearch volume is rounded to the closest decimal values if there is no data, then the value is null | [optional] 
**categories** | **List[Optional[str]]** | product and service categories legacy field, the value will always be null | [optional] 
**monthly_searches** | [**List[MonthlySearches]**](MonthlySearches.md) | monthly searches represents the (approximate) number of searches on this keyword (as available for the past twelve months), targeted to the specified geographic locations. if there is no data, then the value is null | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_keywords_for_keywords_live_result_info import KeywordsDataBingKeywordsForKeywordsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingKeywordsForKeywordsLiveResultInfo from a JSON string
keywords_data_bing_keywords_for_keywords_live_result_info_instance = KeywordsDataBingKeywordsForKeywordsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataBingKeywordsForKeywordsLiveResultInfo.to_json()

# convert the object into a dict
keywords_data_bing_keywords_for_keywords_live_result_info_dict = keywords_data_bing_keywords_for_keywords_live_result_info_instance.to_dict()
# create an instance of KeywordsDataBingKeywordsForKeywordsLiveResultInfo from a dict
keywords_data_bing_keywords_for_keywords_live_result_info_form_dict = keywords_data_bing_keywords_for_keywords_live_result_info.from_dict(keywords_data_bing_keywords_for_keywords_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# KeywordsDataGoogleAdsSearchVolumeTaskGetResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) | [optional] 
**spell** | [**SpellInfo**](SpellInfo.md) |  | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**search_partners** | **bool** | indicates whether data from partner networks included in the response | [optional] 
**competition** | **str** | competition represents the relative amount of competition associated with the given keyword in paid SERP only; this value is based on Google Ads data and can take the following values: HIGH, MEDIUM, LOW; if there is no data the value is null; learn more about the metric in this help center article | [optional] 
**competition_index** | **int** | competition represents the relative amount of competition associated with the given keyword in paid SERP only; this value is based on Google Ads data and can be between 0 and 100 (inclusive); if there is no data the value is null; learn more about the metric in this help center article | [optional] 
**search_volume** | **int** | monthly average search volume rate; represents either the (approximate) number of searches for the given keyword idea on google.com or google.com and partners, depending on the user’s targeting; if there is no data then the value is null | [optional] 
**low_top_of_page_bid** | **float** | minimum bid for the ad to be displayed at the top of the first page indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers); the value may differ depending on the location specified in a POST request | [optional] 
**high_top_of_page_bid** | **float** | maximum bid for the ad to be displayed at the top of the first page indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers); the value may differ depending on the location specified in a POST request | [optional] 
**cpc** | **float** | cost per click indicates the amount paid for each click on the ad displayed for a given keyword | [optional] 
**monthly_searches** | [**List[MonthlySearches]**](MonthlySearches.md) | monthly searches represents the (approximate) number of searches on this keyword idea (as available for the past twelve months by default), targeted to the specified geographic locations; if there is no data then the value is null | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_google_ads_search_volume_task_get_result_info import KeywordsDataGoogleAdsSearchVolumeTaskGetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleAdsSearchVolumeTaskGetResultInfo from a JSON string
keywords_data_google_ads_search_volume_task_get_result_info_instance = KeywordsDataGoogleAdsSearchVolumeTaskGetResultInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataGoogleAdsSearchVolumeTaskGetResultInfo.to_json()

# convert the object into a dict
keywords_data_google_ads_search_volume_task_get_result_info_dict = keywords_data_google_ads_search_volume_task_get_result_info_instance.to_dict()
# create an instance of KeywordsDataGoogleAdsSearchVolumeTaskGetResultInfo from a dict
keywords_data_google_ads_search_volume_task_get_result_info_form_dict = keywords_data_google_ads_search_volume_task_get_result_info.from_dict(keywords_data_google_ads_search_volume_task_get_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



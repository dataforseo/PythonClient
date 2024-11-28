# KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword in a POST array | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, the value is null | [optional] 
**search_partners** | **bool** | include Google search partners the value you specified when setting the task if true, the results are returned for owned, operated, and syndicated networks across Google and partner sites that host Google search; if false, the results are returned for Google search sites only | [optional] 
**competition** | **str** | competition represents the relative level of competition associated with the given keyword in paid SERP only possible values: LOW, MEDIUM, HIGH if competition level is unknown, the value is null; learn more about the metric in this help center article | [optional] 
**competition_index** | **int** | competition index the competition index for the query indicating how competitive ad placement is for the keyword can take values from 0 to 100 the level of competition from 0 to 100 is determined by the number of ad slots filled divided by the total number of ad slots available if not enough data is available, the value is null; learn more about the metric in this help center article | [optional] 
**search_volume** | **int** | monthly average search volume rate represents the (approximate) number of searches for the given keyword idea either on google.com or google.com and partners, depending on the user’s targeting if there is no data, the value is null | [optional] 
**low_top_of_page_bid** | **float** | minimum bid for the ad to be displayed at the top of the first page indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers) the value may differ depending on the location specified in a POST request | [optional] 
**high_top_of_page_bid** | **float** | maximum bid for the ad to be displayed at the top of the first page indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers) the value may differ depending on the location specified in a POST request | [optional] 
**cpc** | **float** | cost per click indicates the amount paid for each click on the ad displayed for a given keyword | [optional] 
**monthly_searches** | [**List[MonthlySearches]**](MonthlySearches.md) | monthly searches represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations if there is no data, the value is null | [optional] 
**keyword_annotations** | [**KeywordAnnotations**](KeywordAnnotations.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_google_ads_keywords_for_keywords_task_get_result_info import KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResultInfo from a JSON string
keywords_data_google_ads_keywords_for_keywords_task_get_result_info_instance = KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResultInfo.to_json())

# convert the object into a dict
keywords_data_google_ads_keywords_for_keywords_task_get_result_info_dict = keywords_data_google_ads_keywords_for_keywords_task_get_result_info_instance.to_dict()
# create an instance of KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResultInfo from a dict
keywords_data_google_ads_keywords_for_keywords_task_get_result_info_from_dict = KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResultInfo.from_dict(keywords_data_google_ads_keywords_for_keywords_task_get_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



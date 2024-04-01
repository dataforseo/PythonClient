# KeywordInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**last_updated_time** | **str** | date and time when keyword data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**competition** | **float** | competition represents the relative amount of competition associated with the given keyword. This value is based on Google Ads data and can be between 0 and 1 (inclusive) | [optional] 
**competition_level** | **str** | competition level represents the relative level of competition associated with the given keyword in paid SERP only; possible values: LOW, MEDIUM, HIGH if competition level is unknown, the value is null; learn more about the metric in this help center article | [optional] 
**cpc** | **float** | cost-per-click represents the average cost per click (USD) historically paid for the keyword | [optional] 
**search_volume** | **int** | average monthly search volume rate represents the (approximate) number of searches for the given keyword idea on google.com | [optional] 
**low_top_of_page_bid** | **float** | minimum bid for the ad to be displayed at the top of the first page indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers) the value may differ depending on the location specified in a POST request | [optional] 
**high_top_of_page_bid** | **float** | maximum bid for the ad to be displayed at the top of the first page indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers) the value may differ depending on the location specified in a POST request | [optional] 
**categories** | **List[int]** | product and service categories you can download the full list of possible categories | [optional] 
**monthly_searches** | [**List[MonthlySearches]**](MonthlySearches.md) | monthly searches represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations | [optional] 

## Example

```python
from dataforseo_client.models.keyword_info import KeywordInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordInfo from a JSON string
keyword_info_instance = KeywordInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordInfo.to_json())

# convert the object into a dict
keyword_info_dict = keyword_info_instance.to_dict()
# create an instance of KeywordInfo from a dict
keyword_info_form_dict = keyword_info.from_dict(keyword_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



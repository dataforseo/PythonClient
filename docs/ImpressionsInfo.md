# ImpressionsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**last_updated_time** | **str** | date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**bid** | **int** | the maximum CPC it stands for the price you are willing to pay for an ad. The higher value, the higher positions and price you will getwe return the results for the 999 bid value to provide the highest number of impressions and level down the account-specific factors | [optional] 
**match_type** | **str** | type of keyword match can take the following values: exact, broad, phrase | [optional] 
**ad_position_min** | **float** | the minimum ad position represents the minimum position of the advertisement | [optional] 
**ad_position_max** | **float** | the maximum ad position represents the maximum position of the advertisement | [optional] 
**ad_position_average** | **float** | the average ad position represents the average position of the advertisement | [optional] 
**cpc_min** | **float** | the minimum value of cost-per-click the minimum cost-per-click (USD) for the keyword given that a bid is set to 999; note: this field does not represent an actual CPC value; you can find an actual CPC value for a keyword in the cpc field of the keyword_info object | [optional] 
**cpc_max** | **float** | the maximum value of cost-per-click the maximum cost-per-click (USD) for the keyword given that a bid is set to 999; note: this field does not represent an actual CPC value; you can find an actual CPC value for a keyword in the cpc field of the keyword_info object | [optional] 
**cpc_average** | **float** | the average value of cost-per-click the average cost-per-click (USD) for the keyword given that a bid is set to 999; note: this field does not represent an actual CPC value; you can find an actual CPC value for a keyword in the cpc field of the keyword_info object | [optional] 
**daily_impressions_min** | **float** | the minimum value of daily impressions represents the minimum number of daily impressions of the advertisement given that that a bid is set to 999; provides a more accurate alternative to Google search volume data | [optional] 
**daily_impressions_max** | **float** | the maximum value of daily impressions represents the maximum number of daily impressions of the advertisement given that that a bid is set to 999; provides a more accurate alternative to Google search volume data | [optional] 
**daily_impressions_average** | **float** | the average value of daily impressions represents the average number of daily impressions of the advertisement given that that a bid is set to 999; provides a more accurate alternative to Google search volume data | [optional] 
**daily_clicks_min** | **float** | the minimum value of daily clicks represents the minimum number of daily clicks on the advertisement | [optional] 
**daily_clicks_max** | **float** | the maximum value of daily clicks represents the maximum number of daily clicks on the advertisement | [optional] 
**daily_clicks_average** | **float** | the average value of daily clicks represents the average number of daily clicks on the advertisement | [optional] 
**daily_cost_min** | **float** | the minimum daily charge value represents the minimum daily cost of the advertisement (USD) | [optional] 
**daily_cost_max** | **float** | the maximum daily charge value represents the maximum daily cost of the advertisement (USD) | [optional] 
**daily_cost_average** | **float** | the average daily charge value represents the average daily cost of the advertisement (USD) | [optional] 

## Example

```python
from dataforseo_client.models.impressions_info import ImpressionsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionsInfo from a JSON string
impressions_info_instance = ImpressionsInfo.from_json(json)
# print the JSON string representation of the object
print(ImpressionsInfo.to_json())

# convert the object into a dict
impressions_info_dict = impressions_info_instance.to_dict()
# create an instance of ImpressionsInfo from a dict
impressions_info_from_dict = ImpressionsInfo.from_dict(impressions_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



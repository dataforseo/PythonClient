# SerpGoogleFinanceExploreAdvancedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**most_active** | [**List[GoogleFinanceMarketTrendsElement]**](GoogleFinanceMarketTrendsElement.md) | array of items this array can take the following names: most_active, gainers, losers | [optional] 
**gainers** | [**List[GoogleFinanceMarketTrendsElement]**](GoogleFinanceMarketTrendsElement.md) |  | [optional] 
**losers** | [**List[GoogleFinanceMarketTrendsElement]**](GoogleFinanceMarketTrendsElement.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_finance_explore_advanced_item import SerpGoogleFinanceExploreAdvancedItem

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleFinanceExploreAdvancedItem from a JSON string
serp_google_finance_explore_advanced_item_instance = SerpGoogleFinanceExploreAdvancedItem.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleFinanceExploreAdvancedItem.to_json())

# convert the object into a dict
serp_google_finance_explore_advanced_item_dict = serp_google_finance_explore_advanced_item_instance.to_dict()
# create an instance of SerpGoogleFinanceExploreAdvancedItem from a dict
serp_google_finance_explore_advanced_item_from_dict = SerpGoogleFinanceExploreAdvancedItem.from_dict(serp_google_finance_explore_advanced_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



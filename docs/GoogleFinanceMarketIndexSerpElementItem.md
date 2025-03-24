# GoogleFinanceMarketIndexSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | ticker of the market index example: DAX | [optional] 
**market_identifier** | **str** | market identifier example: INDEXDB | [optional] 
**index_value** | **float** | value of the market index numerical value of the index at a given timestamp | [optional] 
**index_value_delta** | **float** | change in value of the market index change in the index_value at a given timestamp | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_market_index_serp_element_item import GoogleFinanceMarketIndexSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceMarketIndexSerpElementItem from a JSON string
google_finance_market_index_serp_element_item_instance = GoogleFinanceMarketIndexSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceMarketIndexSerpElementItem.to_json())

# convert the object into a dict
google_finance_market_index_serp_element_item_dict = google_finance_market_index_serp_element_item_instance.to_dict()
# create an instance of GoogleFinanceMarketIndexSerpElementItem from a dict
google_finance_market_index_serp_element_item_from_dict = GoogleFinanceMarketIndexSerpElementItem.from_dict(google_finance_market_index_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



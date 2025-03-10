# GoogleFinanceEarningsCalendarSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GoogleFinanceEarningsCalendarElement]**](GoogleFinanceEarningsCalendarElement.md) | market indexes data array of items containing market indexes data; possible type of items: google_finance_asset_pair_element, google_finance_market_instrument_element, google_finance_market_index_element | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_earnings_calendar_serp_element_item import GoogleFinanceEarningsCalendarSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceEarningsCalendarSerpElementItem from a JSON string
google_finance_earnings_calendar_serp_element_item_instance = GoogleFinanceEarningsCalendarSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceEarningsCalendarSerpElementItem.to_json())

# convert the object into a dict
google_finance_earnings_calendar_serp_element_item_dict = google_finance_earnings_calendar_serp_element_item_instance.to_dict()
# create an instance of GoogleFinanceEarningsCalendarSerpElementItem from a dict
google_finance_earnings_calendar_serp_element_item_from_dict = GoogleFinanceEarningsCalendarSerpElementItem.from_dict(google_finance_earnings_calendar_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



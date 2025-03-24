# GoogleFinanceMarketInstrumentSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | ticker of the market index example: DAX | [optional] 
**price** | **float** | value of the base asset compared to the quote asset | [optional] 
**price_delta** | **float** | change in price change in price at a given timestamp | [optional] 
**price_currency** | **str** | price currency example: USD | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_market_instrument_serp_element_item import GoogleFinanceMarketInstrumentSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceMarketInstrumentSerpElementItem from a JSON string
google_finance_market_instrument_serp_element_item_instance = GoogleFinanceMarketInstrumentSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceMarketInstrumentSerpElementItem.to_json())

# convert the object into a dict
google_finance_market_instrument_serp_element_item_dict = google_finance_market_instrument_serp_element_item_instance.to_dict()
# create an instance of GoogleFinanceMarketInstrumentSerpElementItem from a dict
google_finance_market_instrument_serp_element_item_from_dict = GoogleFinanceMarketInstrumentSerpElementItem.from_dict(google_finance_market_instrument_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



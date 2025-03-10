# GoogleFinanceMarketInstrumentElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**ticker** | **str** | ticker of the market index example: DAX | [optional] 
**price** | **float** | value of the base asset compared to the quote asset | [optional] 
**price_delta** | **float** | change in price change in price at a given timestamp | [optional] 
**price_currency** | **str** | price currency example: USD | [optional] 
**identifier** | **str** | identifier of the element full identifier of the element that consists from ticker and market_identifier example: PX1:INDEXDB | [optional] 
**displayed_name** | **str** | name of the market index as displayed on Google Finance example: CAC 40 | [optional] 
**url** | **str** | URL to the page of the market index on Google Finance | [optional] 
**location** | **str** | location of the market index example: Europe/Paris | [optional] 
**trend** | **str** | growth trend of the market index possible values: up, down, stable | [optional] 
**timestamp** | **str** | date and time of the value readout in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2025-02-10 09:40:00 +00:00 | [optional] 
**percentage_delta** | **float** | percentage of change in value of the market index | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_market_instrument_element import GoogleFinanceMarketInstrumentElement

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceMarketInstrumentElement from a JSON string
google_finance_market_instrument_element_instance = GoogleFinanceMarketInstrumentElement.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceMarketInstrumentElement.to_json())

# convert the object into a dict
google_finance_market_instrument_element_dict = google_finance_market_instrument_element_instance.to_dict()
# create an instance of GoogleFinanceMarketInstrumentElement from a dict
google_finance_market_instrument_element_from_dict = GoogleFinanceMarketInstrumentElement.from_dict(google_finance_market_instrument_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



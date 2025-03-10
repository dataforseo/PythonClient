# GoogleFinanceEarningsCalendarElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the news article | [optional] 
**url** | **str** | URL to the page of the market index on Google Finance | [optional] 
**timestamp** | **str** | date and time of the value readout in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2025-02-10 09:40:00 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_earnings_calendar_element import GoogleFinanceEarningsCalendarElement

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceEarningsCalendarElement from a JSON string
google_finance_earnings_calendar_element_instance = GoogleFinanceEarningsCalendarElement.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceEarningsCalendarElement.to_json())

# convert the object into a dict
google_finance_earnings_calendar_element_dict = google_finance_earnings_calendar_element_instance.to_dict()
# create an instance of GoogleFinanceEarningsCalendarElement from a dict
google_finance_earnings_calendar_element_from_dict = GoogleFinanceEarningsCalendarElement.from_dict(google_finance_earnings_calendar_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



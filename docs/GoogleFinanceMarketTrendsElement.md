# GoogleFinanceMarketTrendsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**quote** | [**GoogleFinanceAssetPairElement**](GoogleFinanceAssetPairElement.md) |  | [optional] 
**news** | [**List[GoogleFinanceNewsElement]**](GoogleFinanceNewsElement.md) | array of items array contains the following type of items: google_finance_news_element | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_market_trends_element import GoogleFinanceMarketTrendsElement

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceMarketTrendsElement from a JSON string
google_finance_market_trends_element_instance = GoogleFinanceMarketTrendsElement.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceMarketTrendsElement.to_json())

# convert the object into a dict
google_finance_market_trends_element_dict = google_finance_market_trends_element_instance.to_dict()
# create an instance of GoogleFinanceMarketTrendsElement from a dict
google_finance_market_trends_element_from_dict = GoogleFinanceMarketTrendsElement.from_dict(google_finance_market_trends_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



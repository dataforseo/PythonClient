# GoogleFinanceNewsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the news element example: In the news | [optional] 
**sub_title** | **str** | sub-title of the news element example: Based on Europe, Middle East, and Africa | [optional] 
**items** | [**List[GoogleFinanceNewsElement]**](GoogleFinanceNewsElement.md) | market indexes data array of items containing market indexes data; possible type of items: google_finance_asset_pair_element, google_finance_market_instrument_element, google_finance_market_index_element | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_news_serp_element_item import GoogleFinanceNewsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceNewsSerpElementItem from a JSON string
google_finance_news_serp_element_item_instance = GoogleFinanceNewsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceNewsSerpElementItem.to_json())

# convert the object into a dict
google_finance_news_serp_element_item_dict = google_finance_news_serp_element_item_instance.to_dict()
# create an instance of GoogleFinanceNewsSerpElementItem from a dict
google_finance_news_serp_element_item_from_dict = GoogleFinanceNewsSerpElementItem.from_dict(google_finance_news_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



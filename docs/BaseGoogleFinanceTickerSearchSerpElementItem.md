# BaseGoogleFinanceTickerSearchSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**identifier** | **str** | identifier of the element full identifier of the element that consists from ticker and market_identifier example: PX1:INDEXDB | [optional] 
**displayed_name** | **str** | name of the market index as displayed on Google Finance example: CAC 40 | [optional] 
**url** | **str** | URL to the page of the market index on Google Finance | [optional] 
**location** | **str** | location of the market index example: Europe/Paris | [optional] 
**trend** | **str** | growth trend of the market index possible values: up, down, stable | [optional] 
**timestamp** | **str** | date and time of the value readout in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2025-02-10 09:40:00 +00:00 | [optional] 
**percentage_delta** | **float** | percentage of change in value of the market index | [optional] 

## Example

```python
from dataforseo_client.models.base_google_finance_ticker_search_serp_element_item import BaseGoogleFinanceTickerSearchSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseGoogleFinanceTickerSearchSerpElementItem from a JSON string
base_google_finance_ticker_search_serp_element_item_instance = BaseGoogleFinanceTickerSearchSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(BaseGoogleFinanceTickerSearchSerpElementItem.to_json())

# convert the object into a dict
base_google_finance_ticker_search_serp_element_item_dict = base_google_finance_ticker_search_serp_element_item_instance.to_dict()
# create an instance of BaseGoogleFinanceTickerSearchSerpElementItem from a dict
base_google_finance_ticker_search_serp_element_item_from_dict = BaseGoogleFinanceTickerSearchSerpElementItem.from_dict(base_google_finance_ticker_search_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



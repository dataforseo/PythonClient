# StocksBoxDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**source** | **str** | source of the element indicates the source of information included in the shopping_element | [optional] 
**snippet** | **str** | text alongside the link title | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 
**url** | **str** | relevant URL | [optional] 
**domain** | **str** | domain where a link points | [optional] 
**table** | [**Table**](Table.md) |  | [optional] 
**graph** | [**Graph**](Graph.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.stocks_box_dataforseo_labs_serp_element_item import StocksBoxDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of StocksBoxDataforseoLabsSerpElementItem from a JSON string
stocks_box_dataforseo_labs_serp_element_item_instance = StocksBoxDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(StocksBoxDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
stocks_box_dataforseo_labs_serp_element_item_dict = stocks_box_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of StocksBoxDataforseoLabsSerpElementItem from a dict
stocks_box_dataforseo_labs_serp_element_item_from_dict = StocksBoxDataforseoLabsSerpElementItem.from_dict(stocks_box_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



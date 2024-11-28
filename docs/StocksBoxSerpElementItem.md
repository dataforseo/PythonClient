# StocksBoxSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**source** | **str** | source of the element indicates the source of the video | [optional] 
**snippet** | **str** | text alongside the link title | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 
**url** | **str** | source URL | [optional] 
**domain** | **str** | source domain | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 
**table** | [**Table**](Table.md) |  | [optional] 
**graph** | [**Graph**](Graph.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.stocks_box_serp_element_item import StocksBoxSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of StocksBoxSerpElementItem from a JSON string
stocks_box_serp_element_item_instance = StocksBoxSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(StocksBoxSerpElementItem.to_json())

# convert the object into a dict
stocks_box_serp_element_item_dict = stocks_box_serp_element_item_instance.to_dict()
# create an instance of StocksBoxSerpElementItem from a dict
stocks_box_serp_element_item_from_dict = StocksBoxSerpElementItem.from_dict(stocks_box_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



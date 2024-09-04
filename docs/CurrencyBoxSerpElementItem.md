# CurrencyBoxSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | the value of the rating | [optional] 
**converted_value** | **float** | value converted to a requested currency indicates the exact value based on Google Fincance data at the time when our API pulled the results note that exchange rates displayed in the currency_box element may be delayed according to the Google Finance disclaimer | [optional] 
**currency** | **str** | currency of the listed price ISO code of the currency applied to the price | [optional] 
**converted_currency** | **str** | converted currency | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**table** | [**Table**](Table.md) |  | [optional] 
**graph** | [**Graph**](Graph.md) |  | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.currency_box_serp_element_item import CurrencyBoxSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyBoxSerpElementItem from a JSON string
currency_box_serp_element_item_instance = CurrencyBoxSerpElementItem.from_json(json)
# print the JSON string representation of the object
print CurrencyBoxSerpElementItem.to_json()

# convert the object into a dict
currency_box_serp_element_item_dict = currency_box_serp_element_item_instance.to_dict()
# create an instance of CurrencyBoxSerpElementItem from a dict
currency_box_serp_element_item_form_dict = currency_box_serp_element_item.from_dict(currency_box_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



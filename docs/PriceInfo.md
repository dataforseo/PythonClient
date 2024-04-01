# PriceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **float** | current price indicates the current price of the product or service featured in the result | [optional] 
**regular** | **float** | regular price indicates the regular price of the product or service with no discounts applied | [optional] 
**max_value** | **float** | the maximum price the maximum price of the product or service as indicated in the result | [optional] 
**currency** | **str** | currency of the listed price ISO code of the currency applied to the price | [optional] 
**is_price_range** | **bool** | price is provided as a range indicates whether a price is provided in a range | [optional] 
**displayed_price** | **str** | price string in the result raw price string as provided in the result | [optional] 

## Example

```python
from dataforseo_client.models.price_info import PriceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PriceInfo from a JSON string
price_info_instance = PriceInfo.from_json(json)
# print the JSON string representation of the object
print(PriceInfo.to_json())

# convert the object into a dict
price_info_dict = price_info_instance.to_dict()
# create an instance of PriceInfo from a dict
price_info_form_dict = price_info.from_dict(price_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



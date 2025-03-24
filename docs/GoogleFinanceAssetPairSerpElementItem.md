# GoogleFinanceAssetPairSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_symbol** | **str** | identifier of the base asset in a pair example: EUR | [optional] 
**quote_symbol** | **str** | identifier of the quote asset in a pair example: USD | [optional] 
**base_display_name** | **str** | full name of the base asset in a pair example: Euro | [optional] 
**quote_display_name** | **str** | full name of the base asset in a pair example: Euro | [optional] 
**price** | **float** | value of the base asset compared to the quote asset | [optional] 
**price_delta** | **float** | change in price change in price at a given timestamp | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_asset_pair_serp_element_item import GoogleFinanceAssetPairSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceAssetPairSerpElementItem from a JSON string
google_finance_asset_pair_serp_element_item_instance = GoogleFinanceAssetPairSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceAssetPairSerpElementItem.to_json())

# convert the object into a dict
google_finance_asset_pair_serp_element_item_dict = google_finance_asset_pair_serp_element_item_instance.to_dict()
# create an instance of GoogleFinanceAssetPairSerpElementItem from a dict
google_finance_asset_pair_serp_element_item_from_dict = GoogleFinanceAssetPairSerpElementItem.from_dict(google_finance_asset_pair_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



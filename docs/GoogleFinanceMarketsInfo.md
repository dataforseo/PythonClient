# GoogleFinanceMarketsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market** | **str** | financial market identifier possible values: US, Europe, Asia, Currencies, Crypto, Futures | [optional] 
**items** | [**List[GoogleFinanceAssetPairElement]**](GoogleFinanceAssetPairElement.md) | elements of search results found in SERP | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_markets_info import GoogleFinanceMarketsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceMarketsInfo from a JSON string
google_finance_markets_info_instance = GoogleFinanceMarketsInfo.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceMarketsInfo.to_json())

# convert the object into a dict
google_finance_markets_info_dict = google_finance_markets_info_instance.to_dict()
# create an instance of GoogleFinanceMarketsInfo from a dict
google_finance_markets_info_from_dict = GoogleFinanceMarketsInfo.from_dict(google_finance_markets_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



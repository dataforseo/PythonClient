# DataforseoLabsGoogleHistoricalKeywordDataLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword** | **str** | keyword keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**history** | [**List[History]**](History.md) | array of objects with historical data for the keyword | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_historical_keyword_data_live_item import DataforseoLabsGoogleHistoricalKeywordDataLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleHistoricalKeywordDataLiveItem from a JSON string
dataforseo_labs_google_historical_keyword_data_live_item_instance = DataforseoLabsGoogleHistoricalKeywordDataLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleHistoricalKeywordDataLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_google_historical_keyword_data_live_item_dict = dataforseo_labs_google_historical_keyword_data_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleHistoricalKeywordDataLiveItem from a dict
dataforseo_labs_google_historical_keyword_data_live_item_from_dict = DataforseoLabsGoogleHistoricalKeywordDataLiveItem.from_dict(dataforseo_labs_google_historical_keyword_data_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



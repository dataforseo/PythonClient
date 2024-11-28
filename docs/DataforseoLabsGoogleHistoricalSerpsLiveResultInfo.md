# DataforseoLabsGoogleHistoricalSerpsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword** | **str** | keyword received in a POST array the keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**total_count** | **int** | the number of results returned in the items array | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoLabsGoogleHistoricalSerpsLiveItem]**](DataforseoLabsGoogleHistoricalSerpsLiveItem.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_historical_serps_live_result_info import DataforseoLabsGoogleHistoricalSerpsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleHistoricalSerpsLiveResultInfo from a JSON string
dataforseo_labs_google_historical_serps_live_result_info_instance = DataforseoLabsGoogleHistoricalSerpsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleHistoricalSerpsLiveResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_historical_serps_live_result_info_dict = dataforseo_labs_google_historical_serps_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleHistoricalSerpsLiveResultInfo from a dict
dataforseo_labs_google_historical_serps_live_result_info_from_dict = DataforseoLabsGoogleHistoricalSerpsLiveResultInfo.from_dict(dataforseo_labs_google_historical_serps_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DataforseoLabsGoogleSearchIntentLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoLabsGoogleSearchIntentLiveItem]**](DataforseoLabsGoogleSearchIntentLiveItem.md) | array of items with relevant traffic estimation data | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_search_intent_live_result_info import DataforseoLabsGoogleSearchIntentLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleSearchIntentLiveResultInfo from a JSON string
dataforseo_labs_google_search_intent_live_result_info_instance = DataforseoLabsGoogleSearchIntentLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleSearchIntentLiveResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_search_intent_live_result_info_dict = dataforseo_labs_google_search_intent_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleSearchIntentLiveResultInfo from a dict
dataforseo_labs_google_search_intent_live_result_info_form_dict = dataforseo_labs_google_search_intent_live_result_info.from_dict(dataforseo_labs_google_search_intent_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



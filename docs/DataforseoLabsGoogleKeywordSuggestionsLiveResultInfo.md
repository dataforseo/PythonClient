# DataforseoLabsGoogleKeywordSuggestionsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**seed_keyword** | **str** | keyword in a POST array | [optional] 
**seed_keyword_data** | [**KeywordDataInfo**](KeywordDataInfo.md) |  | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**offset** | **int** | current offset value | [optional] 
**offset_token** | **str** | offset token for subsequent requests you can use the string provided in this field to get the subsequent results of the initial task; note: offset_token values are unique for each subsequent task | [optional] 
**items** | [**List[KeywordDataInfo]**](KeywordDataInfo.md) | contains keywords and related data | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_keyword_suggestions_live_result_info import DataforseoLabsGoogleKeywordSuggestionsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleKeywordSuggestionsLiveResultInfo from a JSON string
dataforseo_labs_google_keyword_suggestions_live_result_info_instance = DataforseoLabsGoogleKeywordSuggestionsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleKeywordSuggestionsLiveResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_keyword_suggestions_live_result_info_dict = dataforseo_labs_google_keyword_suggestions_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleKeywordSuggestionsLiveResultInfo from a dict
dataforseo_labs_google_keyword_suggestions_live_result_info_from_dict = DataforseoLabsGoogleKeywordSuggestionsLiveResultInfo.from_dict(dataforseo_labs_google_keyword_suggestions_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



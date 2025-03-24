# DataforseoLabsGoogleKeywordOverviewLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoLabsGoogleKeywordOverviewLiveItem]**](DataforseoLabsGoogleKeywordOverviewLiveItem.md) | contains keywords and related data | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_keyword_overview_live_result_info import DataforseoLabsGoogleKeywordOverviewLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleKeywordOverviewLiveResultInfo from a JSON string
dataforseo_labs_google_keyword_overview_live_result_info_instance = DataforseoLabsGoogleKeywordOverviewLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleKeywordOverviewLiveResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_keyword_overview_live_result_info_dict = dataforseo_labs_google_keyword_overview_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleKeywordOverviewLiveResultInfo from a dict
dataforseo_labs_google_keyword_overview_live_result_info_from_dict = DataforseoLabsGoogleKeywordOverviewLiveResultInfo.from_dict(dataforseo_labs_google_keyword_overview_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



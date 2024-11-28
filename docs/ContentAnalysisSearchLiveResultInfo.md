# ContentAnalysisSearchLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset_token** | **str** | offset token for subsequent requests you can use the string provided in this field to get the subsequent results of the initial task; note: offset_token values are unique for each subsequent task | [optional] 
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[ContentAnalysisSearchLiveItem]**](ContentAnalysisSearchLiveItem.md) | contains citations and related data | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_search_live_result_info import ContentAnalysisSearchLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisSearchLiveResultInfo from a JSON string
content_analysis_search_live_result_info_instance = ContentAnalysisSearchLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(ContentAnalysisSearchLiveResultInfo.to_json())

# convert the object into a dict
content_analysis_search_live_result_info_dict = content_analysis_search_live_result_info_instance.to_dict()
# create an instance of ContentAnalysisSearchLiveResultInfo from a dict
content_analysis_search_live_result_info_from_dict = ContentAnalysisSearchLiveResultInfo.from_dict(content_analysis_search_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



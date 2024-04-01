# KeywordsDataBingKeywordPerformanceTaskGetResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword in a POST array | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**year** | **int** | indicates the year for which the data is provided for example: 2020 | [optional] 
**month** | **int** | indicates the month for which the data is provided for example: 10 | [optional] 
**keyword_kpi** | [**KeywordKpi**](KeywordKpi.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_keyword_performance_task_get_result_info import KeywordsDataBingKeywordPerformanceTaskGetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingKeywordPerformanceTaskGetResultInfo from a JSON string
keywords_data_bing_keyword_performance_task_get_result_info_instance = KeywordsDataBingKeywordPerformanceTaskGetResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataBingKeywordPerformanceTaskGetResultInfo.to_json())

# convert the object into a dict
keywords_data_bing_keyword_performance_task_get_result_info_dict = keywords_data_bing_keyword_performance_task_get_result_info_instance.to_dict()
# create an instance of KeywordsDataBingKeywordPerformanceTaskGetResultInfo from a dict
keywords_data_bing_keyword_performance_task_get_result_info_form_dict = keywords_data_bing_keyword_performance_task_get_result_info.from_dict(keywords_data_bing_keyword_performance_task_get_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



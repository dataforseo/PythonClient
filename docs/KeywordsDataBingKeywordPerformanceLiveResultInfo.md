[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# KeywordsDataBingKeywordPerformanceLiveResultInfo

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
from dataforseo_client.models.keywords_data_bing_keyword_performance_live_result_info import KeywordsDataBingKeywordPerformanceLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingKeywordPerformanceLiveResultInfo from a JSON string
keywords_data_bing_keyword_performance_live_result_info_instance = KeywordsDataBingKeywordPerformanceLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataBingKeywordPerformanceLiveResultInfo.to_json()

# convert the object into a dict
keywords_data_bing_keyword_performance_live_result_info_dict = keywords_data_bing_keyword_performance_live_result_info_instance.to_dict()
# create an instance of KeywordsDataBingKeywordPerformanceLiveResultInfo from a dict
keywords_data_bing_keyword_performance_live_result_info_form_dict = keywords_data_bing_keyword_performance_live_result_info.from_dict(keywords_data_bing_keyword_performance_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
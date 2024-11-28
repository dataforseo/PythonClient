# KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **int** | language name | [optional] 
**language_code** | **str** | language code | [optional] 
**available_locations** | [**List[AvailableLocations]**](AvailableLocations.md) | supported locations contains locations supported in combination with a specific language | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_keyword_performance_locations_and_languages_result_info import KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResultInfo from a JSON string
keywords_data_bing_keyword_performance_locations_and_languages_result_info_instance = KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResultInfo.to_json())

# convert the object into a dict
keywords_data_bing_keyword_performance_locations_and_languages_result_info_dict = keywords_data_bing_keyword_performance_locations_and_languages_result_info_instance.to_dict()
# create an instance of KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResultInfo from a dict
keywords_data_bing_keyword_performance_locations_and_languages_result_info_from_dict = KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResultInfo.from_dict(keywords_data_bing_keyword_performance_locations_and_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



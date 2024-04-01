# KeywordsDataBingLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_languages_result_info import KeywordsDataBingLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingLanguagesResultInfo from a JSON string
keywords_data_bing_languages_result_info_instance = KeywordsDataBingLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataBingLanguagesResultInfo.to_json())

# convert the object into a dict
keywords_data_bing_languages_result_info_dict = keywords_data_bing_languages_result_info_instance.to_dict()
# create an instance of KeywordsDataBingLanguagesResultInfo from a dict
keywords_data_bing_languages_result_info_form_dict = keywords_data_bing_languages_result_info.from_dict(keywords_data_bing_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



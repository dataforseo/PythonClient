# ContentAnalysisLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_languages_result_info import ContentAnalysisLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisLanguagesResultInfo from a JSON string
content_analysis_languages_result_info_instance = ContentAnalysisLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print ContentAnalysisLanguagesResultInfo.to_json()

# convert the object into a dict
content_analysis_languages_result_info_dict = content_analysis_languages_result_info_instance.to_dict()
# create an instance of ContentAnalysisLanguagesResultInfo from a dict
content_analysis_languages_result_info_form_dict = content_analysis_languages_result_info.from_dict(content_analysis_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



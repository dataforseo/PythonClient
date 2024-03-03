# ContentGenerationTextSummaryLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 

## Example

```python
from dataforseo_client.models.content_generation_text_summary_languages_result_info import ContentGenerationTextSummaryLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationTextSummaryLanguagesResultInfo from a JSON string
content_generation_text_summary_languages_result_info_instance = ContentGenerationTextSummaryLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print ContentGenerationTextSummaryLanguagesResultInfo.to_json()

# convert the object into a dict
content_generation_text_summary_languages_result_info_dict = content_generation_text_summary_languages_result_info_instance.to_dict()
# create an instance of ContentGenerationTextSummaryLanguagesResultInfo from a dict
content_generation_text_summary_languages_result_info_form_dict = content_generation_text_summary_languages_result_info.from_dict(content_generation_text_summary_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



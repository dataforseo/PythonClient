# ContentGenerationTextSummaryLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sentences** | **int** | number of sentences found in the target text | [optional] 
**paragraphs** | **int** | number of paragraphs found in the target text | [optional] 
**words** | **int** | number of words found in the target text | [optional] 
**characters_without_spaces** | **int** | number of characters without spaces found in the target text | [optional] 
**characters_with_spaces** | **int** | number of characters with spaces found in the target text | [optional] 
**words_per_sentence** | **float** | average number of words per sentence in the target text | [optional] 
**characters_per_word** | **float** | average number of characters per word in the target text | [optional] 
**vocabulary_density** | **float** | vocabulary density of the target text | [optional] 
**keyword_density** | **Dict[str, Optional[int]]** | keyword density of the target text contains most common words and their count | [optional] 
**automated_readability_index** | **float** | Automated Readability Index | [optional] 
**coleman_liau_index** | **float** | Coleman–Liau Index | [optional] 
**flesch_kincaid_grade_level** | **float** | Flesch–Kincaid Readability Index | [optional] 
**smog_readability_index** | **float** | SMOG Readability Index | [optional] 
**spelling_errors** | **int** | number of spelling errors found in the target text | [optional] 
**grammar_errors** | **int** | number of grammar errors found in the target text | [optional] 

## Example

```python
from dataforseo_client.models.content_generation_text_summary_live_result_info import ContentGenerationTextSummaryLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationTextSummaryLiveResultInfo from a JSON string
content_generation_text_summary_live_result_info_instance = ContentGenerationTextSummaryLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(ContentGenerationTextSummaryLiveResultInfo.to_json())

# convert the object into a dict
content_generation_text_summary_live_result_info_dict = content_generation_text_summary_live_result_info_instance.to_dict()
# create an instance of ContentGenerationTextSummaryLiveResultInfo from a dict
content_generation_text_summary_live_result_info_form_dict = content_generation_text_summary_live_result_info.from_dict(content_generation_text_summary_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



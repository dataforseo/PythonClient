# ContentGenerationCheckGrammarLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** | number of input tokens in the POST request | [optional] 
**output_tokens** | **int** | number of output tokens in the response | [optional] 
**new_tokens** | **int** | number of new tokens in the response | [optional] 
**initial_text** | **str** | initial text in the POST request | [optional] 
**language_code** | **str** | language code in the POST request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[ContentGenerationCheckGrammarLiveItem]**](ContentGenerationCheckGrammarLiveItem.md) | contains grammar or spelling errors and related data | [optional] 

## Example

```python
from dataforseo_client.models.content_generation_check_grammar_live_result_info import ContentGenerationCheckGrammarLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationCheckGrammarLiveResultInfo from a JSON string
content_generation_check_grammar_live_result_info_instance = ContentGenerationCheckGrammarLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(ContentGenerationCheckGrammarLiveResultInfo.to_json())

# convert the object into a dict
content_generation_check_grammar_live_result_info_dict = content_generation_check_grammar_live_result_info_instance.to_dict()
# create an instance of ContentGenerationCheckGrammarLiveResultInfo from a dict
content_generation_check_grammar_live_result_info_from_dict = ContentGenerationCheckGrammarLiveResultInfo.from_dict(content_generation_check_grammar_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



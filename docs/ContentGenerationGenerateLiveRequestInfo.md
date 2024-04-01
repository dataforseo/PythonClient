# ContentGenerationGenerateLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | initial target text required field text input for content generation; can contain from 1 to 500 tokens learn more about tokens on our help center | [optional] 
**max_new_tokens** | **int** | generation limit for new tokens required field if max_tokens is not specified the maximum number of new tokens for generated content; maximum value: 300; Note: the number does not include tokens specified in the text field; learn more about this parameter on our help center | [optional] 
**max_tokens** | **int** | generation limit for all tokens required field if max_new_tokens is not specified the maximum total number of tokens for generated content; maximum value: 1024; Note: the number includes tokens specified in the text field learn more about this parameter on our help center | [optional] 
**creativity_index** | **float** | creativity of content generation optional field if you use this field, you don’t need to use top_k / top_p / temperature the randomness of the selection of equally probable subsequent tokens; can take values from 0 to 1 default value: 0.8 learn more about this parameter on our help center | [optional] 
**token_repetition_penalty** | **float** | token repetition optional field limits the repetition of the same tokens in the generated content; can take values from 0.5 to 2; default value: 1 | [optional] 
**top_k** | **int** | the number of initial tokens in each iteration for choosing a subsequent word optional field if you use creativity_index, this field will be ignored the higher the number, the more high-probability tokens will be shortlisted for generation; can take values from 1 to 100; default value: 40 learn more about this parameter on our help center | [optional] 
**top_p** | **float** | excludes initial tokens with probability lower than one optional field if you use creativity_index, this field will be ignored the higher the value, the less low-probability tokens may be shortlisted for generation; can take values from 0 to 1 default value: 0.9 Note:if both top_k and top_p are used, top_k acts first; learn more about this parameter on our help center | [optional] 
**temperature** | **float** | controls the randomness in the output optional field if you use creativity_index, this field will be ignored the lower the temperature, the more likely the model will choose words with a higher probability of occurrence; can take values from 0 to 1; default value: 0.7 learn more about this parameter on our help center | [optional] 
**avoid_words** | **List[str]** | words or phrases to avoid when generating a text optional field you can specify up to 50 terms; example: [\&quot;term\&quot;, \&quot;optimization\&quot;] | [optional] 
**avoid_starting_words** | **List[str]** | words or phrases to avoid in the beginning of the generated text optional field you can specify up to 50 terms; example: [\&quot;SEO\&quot;, \&quot;search engine optimization\&quot;] | [optional] 
**stop_words** | **List[str]** | words or phrases to end the text optional field you can specify up to 50 terms; example: [\&quot;now\&quot;,\&quot;subscribe\&quot;] | [optional] 
**supplement_token** | **str** | token for generating subsequent results optional field provided in the identical filed of the response to each request; you can use this parameter to continue the generation of text from the initial response supplement_token values are unique for each subsequent task | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.content_generation_generate_live_request_info import ContentGenerationGenerateLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationGenerateLiveRequestInfo from a JSON string
content_generation_generate_live_request_info_instance = ContentGenerationGenerateLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(ContentGenerationGenerateLiveRequestInfo.to_json())

# convert the object into a dict
content_generation_generate_live_request_info_dict = content_generation_generate_live_request_info_instance.to_dict()
# create an instance of ContentGenerationGenerateLiveRequestInfo from a dict
content_generation_generate_live_request_info_form_dict = content_generation_generate_live_request_info.from_dict(content_generation_generate_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



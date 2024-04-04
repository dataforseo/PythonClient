# ContentGenerationParaphraseLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** | number of input tokens in the POST request | [optional] 
**output_tokens** | **int** | number of output tokens in the response | [optional] 
**new_tokens** | **int** | number of new tokens in the response | [optional] 
**generated_text** | **str** | paraphrased version of the given text | [optional] 

## Example

```python
from dataforseo_client.models.content_generation_paraphrase_live_result_info import ContentGenerationParaphraseLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationParaphraseLiveResultInfo from a JSON string
content_generation_paraphrase_live_result_info_instance = ContentGenerationParaphraseLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print ContentGenerationParaphraseLiveResultInfo.to_json()

# convert the object into a dict
content_generation_paraphrase_live_result_info_dict = content_generation_paraphrase_live_result_info_instance.to_dict()
# create an instance of ContentGenerationParaphraseLiveResultInfo from a dict
content_generation_paraphrase_live_result_info_form_dict = content_generation_paraphrase_live_result_info.from_dict(content_generation_paraphrase_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentGenerationGenerateLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** | number of input tokens | [optional] 
**output_tokens** | **int** | number of output tokens | [optional] 
**new_tokens** | **int** | number of new tokens | [optional] 
**generated_text** | **str** | resulting text | [optional] 
**supplement_token** | **str** | token for generating subsequent results you can use this parameter to continue the generation from the end of the current result; supplement_token values are unique for each subsequent task | [optional] 

## Example

```python
from dataforseo_client.models.content_generation_generate_live_result_info import ContentGenerationGenerateLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationGenerateLiveResultInfo from a JSON string
content_generation_generate_live_result_info_instance = ContentGenerationGenerateLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print ContentGenerationGenerateLiveResultInfo.to_json()

# convert the object into a dict
content_generation_generate_live_result_info_dict = content_generation_generate_live_result_info_instance.to_dict()
# create an instance of ContentGenerationGenerateLiveResultInfo from a dict
content_generation_generate_live_result_info_form_dict = content_generation_generate_live_result_info.from_dict(content_generation_generate_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



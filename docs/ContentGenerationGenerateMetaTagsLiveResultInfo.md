# ContentGenerationGenerateMetaTagsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** | number of input tokens | [optional] 
**output_tokens** | **int** | number of output tokens | [optional] 
**new_tokens** | **int** | number of new tokens | [optional] 
**title** | **str** | generated title | [optional] 
**description** | **str** | generated description | [optional] 

## Example

```python
from dataforseo_client.models.content_generation_generate_meta_tags_live_result_info import ContentGenerationGenerateMetaTagsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationGenerateMetaTagsLiveResultInfo from a JSON string
content_generation_generate_meta_tags_live_result_info_instance = ContentGenerationGenerateMetaTagsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(ContentGenerationGenerateMetaTagsLiveResultInfo.to_json())

# convert the object into a dict
content_generation_generate_meta_tags_live_result_info_dict = content_generation_generate_meta_tags_live_result_info_instance.to_dict()
# create an instance of ContentGenerationGenerateMetaTagsLiveResultInfo from a dict
content_generation_generate_meta_tags_live_result_info_from_dict = ContentGenerationGenerateMetaTagsLiveResultInfo.from_dict(content_generation_generate_meta_tags_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



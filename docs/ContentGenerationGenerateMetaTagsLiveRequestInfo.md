# ContentGenerationGenerateMetaTagsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | initial target text required field text input for generating content; can contain from 1 to 500 tokens learn more about tokens on our help center | [optional] 
**creativity_index** | **float** | creativity of content generation optional field the randomness of the selection of equally probable subsequent tokens; can take values from 0 to 1; default value: 0.8 learn more about this parameter on our help center | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.content_generation_generate_meta_tags_live_request_info import ContentGenerationGenerateMetaTagsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationGenerateMetaTagsLiveRequestInfo from a JSON string
content_generation_generate_meta_tags_live_request_info_instance = ContentGenerationGenerateMetaTagsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(ContentGenerationGenerateMetaTagsLiveRequestInfo.to_json())

# convert the object into a dict
content_generation_generate_meta_tags_live_request_info_dict = content_generation_generate_meta_tags_live_request_info_instance.to_dict()
# create an instance of ContentGenerationGenerateMetaTagsLiveRequestInfo from a dict
content_generation_generate_meta_tags_live_request_info_form_dict = content_generation_generate_meta_tags_live_request_info.from_dict(content_generation_generate_meta_tags_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ContentGenerationGenerateSubTopicsLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** | number of input tokens | [optional]
**output_tokens** | **int** | number of output tokens | [optional]
**new_tokens** | **int** | number of new tokens | [optional]
**sub_topics** | **List[Optional[str]]** | resulting subtopics | [optional]

## Example

```python
from dataforseo_client.models.content_generation_generate_sub_topics_live_result_info import ContentGenerationGenerateSubTopicsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationGenerateSubTopicsLiveResultInfo from a JSON string
content_generation_generate_sub_topics_live_result_info_instance = ContentGenerationGenerateSubTopicsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print ContentGenerationGenerateSubTopicsLiveResultInfo.to_json()

# convert the object into a dict
content_generation_generate_sub_topics_live_result_info_dict = content_generation_generate_sub_topics_live_result_info_instance.to_dict()
# create an instance of ContentGenerationGenerateSubTopicsLiveResultInfo from a dict
content_generation_generate_sub_topics_live_result_info_form_dict = content_generation_generate_sub_topics_live_result_info.from_dict(content_generation_generate_sub_topics_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
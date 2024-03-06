[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ContentGenerationGenerateTextLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | main topic of the content to generate required field main topic for generating content; can contain from 1 to 50 tokens | [optional]
**word_count** | **int** | number of words in content required field the number of tokens in the generated text; can take values from 1 to 1000 | [optional]
**sub_topics** | **List[str]** | secondary topics of the content to generate optional field secondary topics for generating content; can contain up to 10 terms; example: \&quot;sub_topics\&quot;: [\&quot;Apple\&quot;,\&quot;Pixar\&quot;,\&quot;Amazing Products\&quot;] | [optional]
**description** | **str** | meta description of the content to generate optional field can contain from 1 to 1000 tokens learn more about this parameter on our help center | [optional]
**meta_keywords** | **List[str]** | keywords for the content to generate optional field can contain up to 10 terms; learn more about this parameter on our help center example: \&quot;meta_keywords\&quot;: [\&quot;iPhone\&quot;,\&quot;sell\&quot;,\&quot;CEO\&quot;] | [optional]
**creativity_index** | **float** | creativity of content generation optional field the randomness of the selection of equally probable subsequent tokens; can take values from 0 to 1 default value: 0.8 learn more about this parameter on our help center | [optional]
**include_conclusion** | **bool** | include conclusion in generated text optional field if set to true, generated content will include a logical conclusion | [optional]
**supplement_token** | **str** | token for generating subsequent results optional field provided in the identical filed of the response to each request; you can use this parameter to continue the generation of text from the initial response supplement_token values are unique for each subsequent task | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.content_generation_generate_text_live_request_info import ContentGenerationGenerateTextLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationGenerateTextLiveRequestInfo from a JSON string
content_generation_generate_text_live_request_info_instance = ContentGenerationGenerateTextLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print ContentGenerationGenerateTextLiveRequestInfo.to_json()

# convert the object into a dict
content_generation_generate_text_live_request_info_dict = content_generation_generate_text_live_request_info_instance.to_dict()
# create an instance of ContentGenerationGenerateTextLiveRequestInfo from a dict
content_generation_generate_text_live_request_info_form_dict = content_generation_generate_text_live_request_info.from_dict(content_generation_generate_text_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
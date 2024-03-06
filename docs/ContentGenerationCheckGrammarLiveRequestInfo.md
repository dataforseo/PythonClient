[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ContentGenerationCheckGrammarLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | target text required field can contain from 1 to 10000 tokens learn more about tokens on our help center | [optional]
**language_code** | **str** | code of the text language required field if you do not specify language_name see the List of Languages for Content Generation Check Grammar API | [optional]
**language_name** | **str** | name of the text language required field if you do not specify language_code see the List of Languages for Content Generation Check Grammar API | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.content_generation_check_grammar_live_request_info import ContentGenerationCheckGrammarLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationCheckGrammarLiveRequestInfo from a JSON string
content_generation_check_grammar_live_request_info_instance = ContentGenerationCheckGrammarLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print ContentGenerationCheckGrammarLiveRequestInfo.to_json()

# convert the object into a dict
content_generation_check_grammar_live_request_info_dict = content_generation_check_grammar_live_request_info_instance.to_dict()
# create an instance of ContentGenerationCheckGrammarLiveRequestInfo from a dict
content_generation_check_grammar_live_request_info_form_dict = content_generation_check_grammar_live_request_info.from_dict(content_generation_check_grammar_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
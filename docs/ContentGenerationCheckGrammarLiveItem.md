[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ContentGenerationCheckGrammarLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | message of the grammar or spelling error | [optional]
**description** | **str** | description of the grammar or spelling error | [optional]
**suggestions** | **List[Optional[str]]** | suggested corrections | [optional]
**offset** | **int** | offset token for subsequent requests | [optional]
**length** | **int** | offset token for subsequent requests | [optional]
**type** | **str** | type of element | [optional]
**rule_id** | **str** | id of the grammar or spelling rule see the List of Grammar Rules for Content Generation API | [optional]
**rule_description** | **str** | description of the grammar or spelling rule | [optional]
**rule_issue_type** | **str** | type of the issue found by the relevant rule | [optional]
**rule_category_id** | **str** | id of the rule category | [optional]
**rule_category_name** | **str** | name of the rule category | [optional]

## Example

```python
from dataforseo_client.models.content_generation_check_grammar_live_item import ContentGenerationCheckGrammarLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationCheckGrammarLiveItem from a JSON string
content_generation_check_grammar_live_item_instance = ContentGenerationCheckGrammarLiveItem.from_json(json)
# print the JSON string representation of the object
print ContentGenerationCheckGrammarLiveItem.to_json()

# convert the object into a dict
content_generation_check_grammar_live_item_dict = content_generation_check_grammar_live_item_instance.to_dict()
# create an instance of ContentGenerationCheckGrammarLiveItem from a dict
content_generation_check_grammar_live_item_form_dict = content_generation_check_grammar_live_item.from_dict(content_generation_check_grammar_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
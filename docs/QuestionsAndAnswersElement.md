[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# QuestionsAndAnswersElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**url** | **str** | URL | [optional]
**question_text** | **str** | question included in the item | [optional]
**answer_text** | **str** | answer included in the item | [optional]
**source** | **str** | web source of the hotel booking element indicates the source of information included in the element | [optional]
**domain** | **str** | domain where a link points | [optional]
**votes** | **int** | answer upvotes from the source | [optional]

## Example

```python
from dataforseo_client.models.questions_and_answers_element import QuestionsAndAnswersElement

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionsAndAnswersElement from a JSON string
questions_and_answers_element_instance = QuestionsAndAnswersElement.from_json(json)
# print the JSON string representation of the object
print QuestionsAndAnswersElement.to_json()

# convert the object into a dict
questions_and_answers_element_dict = questions_and_answers_element_instance.to_dict()
# create an instance of QuestionsAndAnswersElement from a dict
questions_and_answers_element_form_dict = questions_and_answers_element.from_dict(questions_and_answers_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
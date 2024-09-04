# QuestionsAndAnswersSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[QuestionsAndAnswersElement]**](QuestionsAndAnswersElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.questions_and_answers_serp_element_item import QuestionsAndAnswersSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionsAndAnswersSerpElementItem from a JSON string
questions_and_answers_serp_element_item_instance = QuestionsAndAnswersSerpElementItem.from_json(json)
# print the JSON string representation of the object
print QuestionsAndAnswersSerpElementItem.to_json()

# convert the object into a dict
questions_and_answers_serp_element_item_dict = questions_and_answers_serp_element_item_instance.to_dict()
# create an instance of QuestionsAndAnswersSerpElementItem from a dict
questions_and_answers_serp_element_item_form_dict = questions_and_answers_serp_element_item.from_dict(questions_and_answers_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



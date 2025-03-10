# QuestionsAndAnswersSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**items** | [**List[QuestionsAndAnswersElement]**](QuestionsAndAnswersElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.questions_and_answers_serp_element_item import QuestionsAndAnswersSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionsAndAnswersSerpElementItem from a JSON string
questions_and_answers_serp_element_item_instance = QuestionsAndAnswersSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(QuestionsAndAnswersSerpElementItem.to_json())

# convert the object into a dict
questions_and_answers_serp_element_item_dict = questions_and_answers_serp_element_item_instance.to_dict()
# create an instance of QuestionsAndAnswersSerpElementItem from a dict
questions_and_answers_serp_element_item_from_dict = QuestionsAndAnswersSerpElementItem.from_dict(questions_and_answers_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



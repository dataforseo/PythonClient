# QuestionsAndAnswersSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**items** | [**List[QuestionsAndAnswersElement]**](QuestionsAndAnswersElement.md) | contains results featured in the ‘hotels_pack’ element of SERP | [optional] 
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



# ItemsWithoutAnswers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank among all the elements | [optional] 
**question_id** | **str** | ID of the question | [optional] 
**url** | **str** | URL of the question | [optional] 
**profile_image_url** | **str** | URL of the user’s profile image | [optional] 
**profile_url** | **str** | URL of the user’s profile | [optional] 
**profile_name** | **str** | displayed name of the user | [optional] 
**question_text** | **str** | current text of the question | [optional] 
**original_question_text** | **str** | original text of the question | [optional] 
**time_ago** | **str** | estimated time when the question was posted | [optional] 
**timestamp** | **str** | exact time when the question was posted | [optional] 
**items** | **object** | array of items items within google_business_question_item | [optional] 

## Example

```python
from dataforseo_client.models.items_without_answers import ItemsWithoutAnswers

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsWithoutAnswers from a JSON string
items_without_answers_instance = ItemsWithoutAnswers.from_json(json)
# print the JSON string representation of the object
print ItemsWithoutAnswers.to_json()

# convert the object into a dict
items_without_answers_dict = items_without_answers_instance.to_dict()
# create an instance of ItemsWithoutAnswers from a dict
items_without_answers_form_dict = items_without_answers.from_dict(items_without_answers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



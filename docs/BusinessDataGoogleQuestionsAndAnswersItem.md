# BusinessDataGoogleQuestionsAndAnswersItem


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
**items** | [**List[GoogleBusinessAnswerElement]**](GoogleBusinessAnswerElement.md) | array of google business question items with answers possible item types: google_business_question_item | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_questions_and_answers_item import BusinessDataGoogleQuestionsAndAnswersItem

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleQuestionsAndAnswersItem from a JSON string
business_data_google_questions_and_answers_item_instance = BusinessDataGoogleQuestionsAndAnswersItem.from_json(json)
# print the JSON string representation of the object
print BusinessDataGoogleQuestionsAndAnswersItem.to_json()

# convert the object into a dict
business_data_google_questions_and_answers_item_dict = business_data_google_questions_and_answers_item_instance.to_dict()
# create an instance of BusinessDataGoogleQuestionsAndAnswersItem from a dict
business_data_google_questions_and_answers_item_form_dict = business_data_google_questions_and_answers_item.from_dict(business_data_google_questions_and_answers_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



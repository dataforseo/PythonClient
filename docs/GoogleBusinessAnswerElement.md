# GoogleBusinessAnswerElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**answer_id** | **str** | ID of the answer | [optional] 
**profile_image_url** | **str** | URL of the user’s profile image | [optional] 
**profile_url** | **str** | URL of the user’s profile | [optional] 
**profile_name** | **str** | displayed name of the user | [optional] 
**answer_text** | **str** | current text of the answer | [optional] 
**original_answer_text** | **str** | original text of the answer | [optional] 
**time_ago** | **str** | estimated time when the answer was posted | [optional] 
**timestamp** | **str** | exact time when the answer was posted | [optional] 

## Example

```python
from dataforseo_client.models.google_business_answer_element import GoogleBusinessAnswerElement

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleBusinessAnswerElement from a JSON string
google_business_answer_element_instance = GoogleBusinessAnswerElement.from_json(json)
# print the JSON string representation of the object
print GoogleBusinessAnswerElement.to_json()

# convert the object into a dict
google_business_answer_element_dict = google_business_answer_element_instance.to_dict()
# create an instance of GoogleBusinessAnswerElement from a dict
google_business_answer_element_form_dict = google_business_answer_element.from_dict(google_business_answer_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



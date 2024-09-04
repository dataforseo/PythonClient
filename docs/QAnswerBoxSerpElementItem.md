# QAnswerBoxSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **List[Optional[str]]** | text if there is none, equals null | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | link of the element | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.q_answer_box_serp_element_item import QAnswerBoxSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of QAnswerBoxSerpElementItem from a JSON string
q_answer_box_serp_element_item_instance = QAnswerBoxSerpElementItem.from_json(json)
# print the JSON string representation of the object
print QAnswerBoxSerpElementItem.to_json()

# convert the object into a dict
q_answer_box_serp_element_item_dict = q_answer_box_serp_element_item_instance.to_dict()
# create an instance of QAnswerBoxSerpElementItem from a dict
q_answer_box_serp_element_item_form_dict = q_answer_box_serp_element_item.from_dict(q_answer_box_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



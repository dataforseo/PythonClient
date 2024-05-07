# QAnswerBoxSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values; positions of elements with different type values are omitted from rank_group; always equals 0 for desktop | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP always equals 0 for desktop | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
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



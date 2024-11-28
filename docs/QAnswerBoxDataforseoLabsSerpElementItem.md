# QAnswerBoxDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **List[Optional[str]]** | text if there is none, equals null | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.q_answer_box_dataforseo_labs_serp_element_item import QAnswerBoxDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of QAnswerBoxDataforseoLabsSerpElementItem from a JSON string
q_answer_box_dataforseo_labs_serp_element_item_instance = QAnswerBoxDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(QAnswerBoxDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
q_answer_box_dataforseo_labs_serp_element_item_dict = q_answer_box_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of QAnswerBoxDataforseoLabsSerpElementItem from a dict
q_answer_box_dataforseo_labs_serp_element_item_from_dict = QAnswerBoxDataforseoLabsSerpElementItem.from_dict(q_answer_box_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



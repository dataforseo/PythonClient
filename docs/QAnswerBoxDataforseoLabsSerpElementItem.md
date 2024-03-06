[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# QAnswerBoxDataforseoLabsSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
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
print QAnswerBoxDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
q_answer_box_dataforseo_labs_serp_element_item_dict = q_answer_box_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of QAnswerBoxDataforseoLabsSerpElementItem from a dict
q_answer_box_dataforseo_labs_serp_element_item_form_dict = q_answer_box_dataforseo_labs_serp_element_item.from_dict(q_answer_box_dataforseo_labs_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
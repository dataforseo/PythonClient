# FaqBoxElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**description** | **str** | description | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | link of the element | [optional] 

## Example

```python
from dataforseo_client.models.faq_box_element import FaqBoxElement

# TODO update the JSON string below
json = "{}"
# create an instance of FaqBoxElement from a JSON string
faq_box_element_instance = FaqBoxElement.from_json(json)
# print the JSON string representation of the object
print FaqBoxElement.to_json()

# convert the object into a dict
faq_box_element_dict = faq_box_element_instance.to_dict()
# create an instance of FaqBoxElement from a dict
faq_box_element_form_dict = faq_box_element.from_dict(faq_box_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



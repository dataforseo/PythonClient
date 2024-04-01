# PeopleAlsoAskElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**seed_question** | **str** | question that triggered additional expanded elements | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**expanded_element** | [**List[PeopleAlsoAskExpandedElement]**](PeopleAlsoAskExpandedElement.md) | expanded element | [optional] 

## Example

```python
from dataforseo_client.models.people_also_ask_element import PeopleAlsoAskElement

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleAlsoAskElement from a JSON string
people_also_ask_element_instance = PeopleAlsoAskElement.from_json(json)
# print the JSON string representation of the object
print(PeopleAlsoAskElement.to_json())

# convert the object into a dict
people_also_ask_element_dict = people_also_ask_element_instance.to_dict()
# create an instance of PeopleAlsoAskElement from a dict
people_also_ask_element_form_dict = people_also_ask_element.from_dict(people_also_ask_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



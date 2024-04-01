# PeopleAlsoAskExpandedElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**featured_title** | **str** | the title of the featured snippets source page | [optional] 
**url** | **str** | URL of element | [optional] 
**domain** | **str** | domain where a link points | [optional] 
**title** | **str** | title of the carousel item | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**images** | [**List[ImagesElement]**](ImagesElement.md) | images of the element | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**table** | [**Table**](Table.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.people_also_ask_expanded_element import PeopleAlsoAskExpandedElement

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleAlsoAskExpandedElement from a JSON string
people_also_ask_expanded_element_instance = PeopleAlsoAskExpandedElement.from_json(json)
# print the JSON string representation of the object
print(PeopleAlsoAskExpandedElement.to_json())

# convert the object into a dict
people_also_ask_expanded_element_dict = people_also_ask_expanded_element_instance.to_dict()
# create an instance of PeopleAlsoAskExpandedElement from a dict
people_also_ask_expanded_element_form_dict = people_also_ask_expanded_element.from_dict(people_also_ask_expanded_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



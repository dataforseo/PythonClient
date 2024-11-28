# InformationAndTicketsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the element | [optional] 
**description** | **str** | description of the element | [optional] 
**url** | **str** | relevant URL | [optional] 
**domain** | **str** | domain in SERP | [optional] 

## Example

```python
from dataforseo_client.models.information_and_tickets_element import InformationAndTicketsElement

# TODO update the JSON string below
json = "{}"
# create an instance of InformationAndTicketsElement from a JSON string
information_and_tickets_element_instance = InformationAndTicketsElement.from_json(json)
# print the JSON string representation of the object
print(InformationAndTicketsElement.to_json())

# convert the object into a dict
information_and_tickets_element_dict = information_and_tickets_element_instance.to_dict()
# create an instance of InformationAndTicketsElement from a dict
information_and_tickets_element_from_dict = InformationAndTicketsElement.from_dict(information_and_tickets_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



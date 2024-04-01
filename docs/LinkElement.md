# LinkElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**snippet** | **str** | text alongside the link title | [optional] 
**description** | **str** | description of the results element | [optional] 
**url** | **str** | URL | [optional] 
**domain** | **str** | domain where a link points | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 

## Example

```python
from dataforseo_client.models.link_element import LinkElement

# TODO update the JSON string below
json = "{}"
# create an instance of LinkElement from a JSON string
link_element_instance = LinkElement.from_json(json)
# print the JSON string representation of the object
print(LinkElement.to_json())

# convert the object into a dict
link_element_dict = link_element_instance.to_dict()
# create an instance of LinkElement from a dict
link_element_form_dict = link_element.from_dict(link_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



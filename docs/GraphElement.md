# GraphElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**var_date** | **str** | the posting date | [optional] 
**value** | **int** | the value of the rating | [optional] 

## Example

```python
from dataforseo_client.models.graph_element import GraphElement

# TODO update the JSON string below
json = "{}"
# create an instance of GraphElement from a JSON string
graph_element_instance = GraphElement.from_json(json)
# print the JSON string representation of the object
print GraphElement.to_json()

# convert the object into a dict
graph_element_dict = graph_element_instance.to_dict()
# create an instance of GraphElement from a dict
graph_element_form_dict = graph_element.from_dict(graph_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



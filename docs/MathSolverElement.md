# MathSolverElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the row | [optional] 
**expanded_element** | [**List[MathSolverExpandedElement]**](MathSolverExpandedElement.md) | expanded element | [optional] 

## Example

```python
from dataforseo_client.models.math_solver_element import MathSolverElement

# TODO update the JSON string below
json = "{}"
# create an instance of MathSolverElement from a JSON string
math_solver_element_instance = MathSolverElement.from_json(json)
# print the JSON string representation of the object
print MathSolverElement.to_json()

# convert the object into a dict
math_solver_element_dict = math_solver_element_instance.to_dict()
# create an instance of MathSolverElement from a dict
math_solver_element_form_dict = math_solver_element.from_dict(math_solver_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



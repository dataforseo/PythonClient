[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# MathSolverExpandedElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of a given link element | [optional]
**solution** | **List[Optional[str]]** | solution of the element displays steps to solve the mathematical equation as specified in the element | [optional]

## Example

```python
from dataforseo_client.models.math_solver_expanded_element import MathSolverExpandedElement

# TODO update the JSON string below
json = "{}"
# create an instance of MathSolverExpandedElement from a JSON string
math_solver_expanded_element_instance = MathSolverExpandedElement.from_json(json)
# print the JSON string representation of the object
print MathSolverExpandedElement.to_json()

# convert the object into a dict
math_solver_expanded_element_dict = math_solver_expanded_element_instance.to_dict()
# create an instance of MathSolverExpandedElement from a dict
math_solver_expanded_element_form_dict = math_solver_expanded_element.from_dict(math_solver_expanded_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
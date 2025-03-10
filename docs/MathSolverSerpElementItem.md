# MathSolverSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**result** | **str** | solution to the equation solution to the mathematical equation specified in the keyword field when setting a task | [optional] 
**items** | [**List[MathSolverElement]**](MathSolverElement.md) | contains arrays of specific images | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | link of the element | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.math_solver_serp_element_item import MathSolverSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MathSolverSerpElementItem from a JSON string
math_solver_serp_element_item_instance = MathSolverSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(MathSolverSerpElementItem.to_json())

# convert the object into a dict
math_solver_serp_element_item_dict = math_solver_serp_element_item_instance.to_dict()
# create an instance of MathSolverSerpElementItem from a dict
math_solver_serp_element_item_from_dict = MathSolverSerpElementItem.from_dict(math_solver_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



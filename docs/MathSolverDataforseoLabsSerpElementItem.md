# MathSolverDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**result** | **str** | solution to the equation solution to the mathematical equation specified in the keyword field when setting a task | [optional] 
**items** | [**List[MathSolverElement]**](MathSolverElement.md) | additional items present in the element if there are none, equals null | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.math_solver_dataforseo_labs_serp_element_item import MathSolverDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MathSolverDataforseoLabsSerpElementItem from a JSON string
math_solver_dataforseo_labs_serp_element_item_instance = MathSolverDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(MathSolverDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
math_solver_dataforseo_labs_serp_element_item_dict = math_solver_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of MathSolverDataforseoLabsSerpElementItem from a dict
math_solver_dataforseo_labs_serp_element_item_from_dict = MathSolverDataforseoLabsSerpElementItem.from_dict(math_solver_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RefinementChipsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the element | [optional] 
**url** | **str** | search URL with refinement parameters | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**options** | [**List[LicensesElement]**](LicensesElement.md) | further search refinement options | [optional] 

## Example

```python
from dataforseo_client.models.refinement_chips_element import RefinementChipsElement

# TODO update the JSON string below
json = "{}"
# create an instance of RefinementChipsElement from a JSON string
refinement_chips_element_instance = RefinementChipsElement.from_json(json)
# print the JSON string representation of the object
print(RefinementChipsElement.to_json())

# convert the object into a dict
refinement_chips_element_dict = refinement_chips_element_instance.to_dict()
# create an instance of RefinementChipsElement from a dict
refinement_chips_element_from_dict = RefinementChipsElement.from_dict(refinement_chips_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



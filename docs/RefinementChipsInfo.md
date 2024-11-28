# RefinementChipsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**items** | [**List[RefinementChipsElement]**](RefinementChipsElement.md) | items of the element | [optional] 

## Example

```python
from dataforseo_client.models.refinement_chips_info import RefinementChipsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RefinementChipsInfo from a JSON string
refinement_chips_info_instance = RefinementChipsInfo.from_json(json)
# print the JSON string representation of the object
print(RefinementChipsInfo.to_json())

# convert the object into a dict
refinement_chips_info_dict = refinement_chips_info_instance.to_dict()
# create an instance of RefinementChipsInfo from a dict
refinement_chips_info_from_dict = RefinementChipsInfo.from_dict(refinement_chips_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



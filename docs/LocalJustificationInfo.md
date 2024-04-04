# LocalJustificationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**text** | **str** | text snippet of local justification | [optional] 

## Example

```python
from dataforseo_client.models.local_justification_info import LocalJustificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LocalJustificationInfo from a JSON string
local_justification_info_instance = LocalJustificationInfo.from_json(json)
# print the JSON string representation of the object
print LocalJustificationInfo.to_json()

# convert the object into a dict
local_justification_info_dict = local_justification_info_instance.to_dict()
# create an instance of LocalJustificationInfo from a dict
local_justification_info_form_dict = local_justification_info.from_dict(local_justification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



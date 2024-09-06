# AiOverviewReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**source** | **str** | reference source name or title | [optional] 
**domain** | **str** | website domain | [optional] 
**url** | **str** | URL | [optional] 
**title** | **str** | title of a given link element | [optional] 
**text** | **str** | row content | [optional] 

## Example

```python
from dataforseo_client.models.ai_overview_reference import AiOverviewReference

# TODO update the JSON string below
json = "{}"
# create an instance of AiOverviewReference from a JSON string
ai_overview_reference_instance = AiOverviewReference.from_json(json)
# print the JSON string representation of the object
print AiOverviewReference.to_json()

# convert the object into a dict
ai_overview_reference_dict = ai_overview_reference_instance.to_dict()
# create an instance of AiOverviewReference from a dict
ai_overview_reference_form_dict = ai_overview_reference.from_dict(ai_overview_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



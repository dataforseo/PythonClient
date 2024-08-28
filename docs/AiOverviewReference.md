# AiOverviewReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**source** | **str** | source of the element indicates the source of information included in the questions_and_answers_element | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**url** | **str** | URL | [optional] 
**title** | **str** | title of a given shopping element | [optional] 
**text** | **str** | reference text text snippet from the page that was used to generate the ai_overview_element | [optional] 

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



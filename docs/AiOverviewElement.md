# AiOverviewElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the element | [optional] 
**text** | **str** | description content | [optional] 
**images** | [**List[ImagesElement]**](ImagesElement.md) | images of the element | [optional] 
**references** | [**List[AiOverviewReference]**](AiOverviewReference.md) | references relevant to the element | [optional] 

## Example

```python
from dataforseo_client.models.ai_overview_element import AiOverviewElement

# TODO update the JSON string below
json = "{}"
# create an instance of AiOverviewElement from a JSON string
ai_overview_element_instance = AiOverviewElement.from_json(json)
# print the JSON string representation of the object
print(AiOverviewElement.to_json())

# convert the object into a dict
ai_overview_element_dict = ai_overview_element_instance.to_dict()
# create an instance of AiOverviewElement from a dict
ai_overview_element_from_dict = AiOverviewElement.from_dict(ai_overview_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



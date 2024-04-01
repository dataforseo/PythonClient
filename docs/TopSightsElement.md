# TopSightsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**url** | **str** | URL | [optional] 
**description** | **str** | description | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.top_sights_element import TopSightsElement

# TODO update the JSON string below
json = "{}"
# create an instance of TopSightsElement from a JSON string
top_sights_element_instance = TopSightsElement.from_json(json)
# print the JSON string representation of the object
print(TopSightsElement.to_json())

# convert the object into a dict
top_sights_element_dict = top_sights_element_instance.to_dict()
# create an instance of TopSightsElement from a dict
top_sights_element_form_dict = top_sights_element.from_dict(top_sights_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



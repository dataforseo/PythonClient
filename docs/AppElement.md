# AppElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**description** | **str** | description | [optional] 
**url** | **str** | URL | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.app_element import AppElement

# TODO update the JSON string below
json = "{}"
# create an instance of AppElement from a JSON string
app_element_instance = AppElement.from_json(json)
# print the JSON string representation of the object
print(AppElement.to_json())

# convert the object into a dict
app_element_dict = app_element_instance.to_dict()
# create an instance of AppElement from a dict
app_element_from_dict = AppElement.from_dict(app_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



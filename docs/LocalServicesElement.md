# LocalServicesElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**url** | **str** | URL | [optional] 
**domain** | **str** | website domain | [optional] 
**description** | **str** | description | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**profile_image_url** | **str** | URL of the image featured in the element | [optional] 

## Example

```python
from dataforseo_client.models.local_services_element import LocalServicesElement

# TODO update the JSON string below
json = "{}"
# create an instance of LocalServicesElement from a JSON string
local_services_element_instance = LocalServicesElement.from_json(json)
# print the JSON string representation of the object
print(LocalServicesElement.to_json())

# convert the object into a dict
local_services_element_dict = local_services_element_instance.to_dict()
# create an instance of LocalServicesElement from a dict
local_services_element_form_dict = local_services_element.from_dict(local_services_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



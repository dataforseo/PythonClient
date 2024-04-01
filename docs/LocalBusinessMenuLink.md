# LocalBusinessMenuLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the element domain of the online menu system | [optional] 
**url** | **str** | URL to view the menu | [optional] 

## Example

```python
from dataforseo_client.models.local_business_menu_link import LocalBusinessMenuLink

# TODO update the JSON string below
json = "{}"
# create an instance of LocalBusinessMenuLink from a JSON string
local_business_menu_link_instance = LocalBusinessMenuLink.from_json(json)
# print the JSON string representation of the object
print(LocalBusinessMenuLink.to_json())

# convert the object into a dict
local_business_menu_link_dict = local_business_menu_link_instance.to_dict()
# create an instance of LocalBusinessMenuLink from a dict
local_business_menu_link_form_dict = local_business_menu_link.from_dict(local_business_menu_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



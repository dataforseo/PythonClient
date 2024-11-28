# LicensesElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the element | [optional] 
**url** | **str** | search URL with refinement parameters | [optional] 
**domain** | **str** | domain in SERP | [optional] 

## Example

```python
from dataforseo_client.models.licenses_element import LicensesElement

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesElement from a JSON string
licenses_element_instance = LicensesElement.from_json(json)
# print the JSON string representation of the object
print(LicensesElement.to_json())

# convert the object into a dict
licenses_element_dict = licenses_element_instance.to_dict()
# create an instance of LicensesElement from a dict
licenses_element_from_dict = LicensesElement.from_dict(licenses_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



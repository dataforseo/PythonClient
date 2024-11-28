# FormatsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**format** | **str** | type of file format of the dataset for example: zip, html, csv | [optional] 
**size** | **str** | file size in bytes | [optional] 

## Example

```python
from dataforseo_client.models.formats_element import FormatsElement

# TODO update the JSON string below
json = "{}"
# create an instance of FormatsElement from a JSON string
formats_element_instance = FormatsElement.from_json(json)
# print the JSON string representation of the object
print(FormatsElement.to_json())

# convert the object into a dict
formats_element_dict = formats_element_instance.to_dict()
# create an instance of FormatsElement from a dict
formats_element_from_dict = FormatsElement.from_dict(formats_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



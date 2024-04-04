# AuthorsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**name** | **str** | name of the dataset author | [optional] 
**url** | **str** | author’s link URL | [optional] 
**domain** | **str** | author’s link domain | [optional] 

## Example

```python
from dataforseo_client.models.authors_element import AuthorsElement

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorsElement from a JSON string
authors_element_instance = AuthorsElement.from_json(json)
# print the JSON string representation of the object
print AuthorsElement.to_json()

# convert the object into a dict
authors_element_dict = authors_element_instance.to_dict()
# create an instance of AuthorsElement from a dict
authors_element_form_dict = authors_element.from_dict(authors_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



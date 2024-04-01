# Table


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_element** | **str** | name assigned to the table element possible values: table_element | [optional] 
**table_header** | **List[Optional[str]]** | column names | [optional] 
**table_content** | **List[Optional[List[Optional[str]]]]** | the content of the table one line of the table in this element of the array | [optional] 

## Example

```python
from dataforseo_client.models.table import Table

# TODO update the JSON string below
json = "{}"
# create an instance of Table from a JSON string
table_instance = Table.from_json(json)
# print the JSON string representation of the object
print(Table.to_json())

# convert the object into a dict
table_dict = table_instance.to_dict()
# create an instance of Table from a dict
table_form_dict = table.from_dict(table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TableContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**List[TableContentItemInfo]**](TableContentItemInfo.md) | parsed content of the header | [optional] 
**body** | [**List[TableContentItemInfo]**](TableContentItemInfo.md) | content of the body of the table | [optional] 
**footer** | [**List[TableContentItemInfo]**](TableContentItemInfo.md) | content of the footer of the table | [optional] 

## Example

```python
from dataforseo_client.models.table_content import TableContent

# TODO update the JSON string below
json = "{}"
# create an instance of TableContent from a JSON string
table_content_instance = TableContent.from_json(json)
# print the JSON string representation of the object
print(TableContent.to_json())

# convert the object into a dict
table_content_dict = table_content_instance.to_dict()
# create an instance of TableContent from a dict
table_content_from_dict = TableContent.from_dict(table_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



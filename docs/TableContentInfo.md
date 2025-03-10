# TableContentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**List[TableContentItemInfo]**](TableContentItemInfo.md) | parsed content of the header | [optional] 
**body** | [**List[TableContentItemInfo]**](TableContentItemInfo.md) | content of the body of the table | [optional] 
**footer** | [**List[TableContentItemInfo]**](TableContentItemInfo.md) | content of the footer of the table | [optional] 

## Example

```python
from dataforseo_client.models.table_content_info import TableContentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TableContentInfo from a JSON string
table_content_info_instance = TableContentInfo.from_json(json)
# print the JSON string representation of the object
print(TableContentInfo.to_json())

# convert the object into a dict
table_content_info_dict = table_content_info_instance.to_dict()
# create an instance of TableContentInfo from a dict
table_content_info_from_dict = TableContentInfo.from_dict(table_content_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



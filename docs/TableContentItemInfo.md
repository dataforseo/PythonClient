# TableContentItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_cells** | [**List[RowCellInfo]**](RowCellInfo.md) | content of the row cells of the header | [optional] 

## Example

```python
from dataforseo_client.models.table_content_item_info import TableContentItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TableContentItemInfo from a JSON string
table_content_item_info_instance = TableContentItemInfo.from_json(json)
# print the JSON string representation of the object
print TableContentItemInfo.to_json()

# convert the object into a dict
table_content_item_info_dict = table_content_item_info_instance.to_dict()
# create an instance of TableContentItemInfo from a dict
table_content_item_info_form_dict = table_content_item_info.from_dict(table_content_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RowCellInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | content text | [optional] 
**urls** | [**List[ContentUrlInfo]**](ContentUrlInfo.md) | contains other URLs and anchors found in the content element | [optional] 
**is_header** | **bool** | indicates if the text belongs to the header | [optional] 

## Example

```python
from dataforseo_client.models.row_cell_info import RowCellInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RowCellInfo from a JSON string
row_cell_info_instance = RowCellInfo.from_json(json)
# print the JSON string representation of the object
print(RowCellInfo.to_json())

# convert the object into a dict
row_cell_info_dict = row_cell_info_instance.to_dict()
# create an instance of RowCellInfo from a dict
row_cell_info_from_dict = RowCellInfo.from_dict(row_cell_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



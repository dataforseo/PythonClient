# RowCells


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | content text | [optional] 
**urls** | **object** | contains other URLs and anchors found in the content element | [optional] 
**is_header** | **bool** | indicates if the text belongs to the header | [optional] 

## Example

```python
from dataforseo_client.models.row_cells import RowCells

# TODO update the JSON string below
json = "{}"
# create an instance of RowCells from a JSON string
row_cells_instance = RowCells.from_json(json)
# print the JSON string representation of the object
print RowCells.to_json()

# convert the object into a dict
row_cells_dict = row_cells_instance.to_dict()
# create an instance of RowCells from a dict
row_cells_form_dict = row_cells.from_dict(row_cells_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



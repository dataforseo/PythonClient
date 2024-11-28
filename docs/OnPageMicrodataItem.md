# OnPageMicrodataItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**inspection_info** | [**MicrodataInspectionInfo**](MicrodataInspectionInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.on_page_microdata_item import OnPageMicrodataItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageMicrodataItem from a JSON string
on_page_microdata_item_instance = OnPageMicrodataItem.from_json(json)
# print the JSON string representation of the object
print(OnPageMicrodataItem.to_json())

# convert the object into a dict
on_page_microdata_item_dict = on_page_microdata_item_instance.to_dict()
# create an instance of OnPageMicrodataItem from a dict
on_page_microdata_item_from_dict = OnPageMicrodataItem.from_dict(on_page_microdata_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



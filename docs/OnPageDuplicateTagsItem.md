# OnPageDuplicateTagsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accumulator** | **str** | contains the value of duplicated tag | [optional] 
**total_count** | **int** | total count of duplicate pages | [optional] 
**pages** | [**List[BaseOnPageResourceItemInfo]**](BaseOnPageResourceItemInfo.md) | pages with duplicate tags | [optional] 

## Example

```python
from dataforseo_client.models.on_page_duplicate_tags_item import OnPageDuplicateTagsItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageDuplicateTagsItem from a JSON string
on_page_duplicate_tags_item_instance = OnPageDuplicateTagsItem.from_json(json)
# print the JSON string representation of the object
print(OnPageDuplicateTagsItem.to_json())

# convert the object into a dict
on_page_duplicate_tags_item_dict = on_page_duplicate_tags_item_instance.to_dict()
# create an instance of OnPageDuplicateTagsItem from a dict
on_page_duplicate_tags_item_from_dict = OnPageDuplicateTagsItem.from_dict(on_page_duplicate_tags_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



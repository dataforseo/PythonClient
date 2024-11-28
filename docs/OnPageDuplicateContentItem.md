# OnPageDuplicateContentItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the specified page | [optional] 
**total_count** | **int** | total count of duplicate pages | [optional] 
**pages** | [**List[Pages]**](Pages.md) | pages with duplicate content | [optional] 

## Example

```python
from dataforseo_client.models.on_page_duplicate_content_item import OnPageDuplicateContentItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageDuplicateContentItem from a JSON string
on_page_duplicate_content_item_instance = OnPageDuplicateContentItem.from_json(json)
# print the JSON string representation of the object
print(OnPageDuplicateContentItem.to_json())

# convert the object into a dict
on_page_duplicate_content_item_dict = on_page_duplicate_content_item_instance.to_dict()
# create an instance of OnPageDuplicateContentItem from a dict
on_page_duplicate_content_item_from_dict = OnPageDuplicateContentItem.from_dict(on_page_duplicate_content_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



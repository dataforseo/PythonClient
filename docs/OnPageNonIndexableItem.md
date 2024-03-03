# OnPageNonIndexableItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | the reason why the page is non-indexable can take the following values: robots_txt, meta_tag, http_header, attribute, too_many_redirects | [optional] 
**url** | **str** | url of the non-indexable page | [optional] 

## Example

```python
from dataforseo_client.models.on_page_non_indexable_item import OnPageNonIndexableItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageNonIndexableItem from a JSON string
on_page_non_indexable_item_instance = OnPageNonIndexableItem.from_json(json)
# print the JSON string representation of the object
print OnPageNonIndexableItem.to_json()

# convert the object into a dict
on_page_non_indexable_item_dict = on_page_non_indexable_item_instance.to_dict()
# create an instance of OnPageNonIndexableItem from a dict
on_page_non_indexable_item_form_dict = on_page_non_indexable_item.from_dict(on_page_non_indexable_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



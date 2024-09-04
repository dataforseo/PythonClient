# OnPageAlternateLinkElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_to_status_code** | **int** | status code of the referenced page status code of the page to which the link is pointing | [optional] 

## Example

```python
from dataforseo_client.models.on_page_alternate_link_element_item import OnPageAlternateLinkElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageAlternateLinkElementItem from a JSON string
on_page_alternate_link_element_item_instance = OnPageAlternateLinkElementItem.from_json(json)
# print the JSON string representation of the object
print OnPageAlternateLinkElementItem.to_json()

# convert the object into a dict
on_page_alternate_link_element_item_dict = on_page_alternate_link_element_item_instance.to_dict()
# create an instance of OnPageAlternateLinkElementItem from a dict
on_page_alternate_link_element_item_form_dict = on_page_alternate_link_element_item.from_dict(on_page_alternate_link_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



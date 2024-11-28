# OnPageImageResourceElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResourceMetaInfo**](ResourceMetaInfo.md) |  | [optional] 
**fetch_timing** | [**FetchTiming**](FetchTiming.md) |  | [optional] 
**accept_type** | **str** | indicates the expected type of resource for example, if \&quot;resource_type\&quot;: \&quot;broken\&quot;, accept_type will indicate the type of the broken resource possible values: any, none, image, sitemap, robots, script, stylesheet, redirect, html, text, other, font | [optional] 

## Example

```python
from dataforseo_client.models.on_page_image_resource_element_item import OnPageImageResourceElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageImageResourceElementItem from a JSON string
on_page_image_resource_element_item_instance = OnPageImageResourceElementItem.from_json(json)
# print the JSON string representation of the object
print(OnPageImageResourceElementItem.to_json())

# convert the object into a dict
on_page_image_resource_element_item_dict = on_page_image_resource_element_item_instance.to_dict()
# create an instance of OnPageImageResourceElementItem from a dict
on_page_image_resource_element_item_from_dict = OnPageImageResourceElementItem.from_dict(on_page_image_resource_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



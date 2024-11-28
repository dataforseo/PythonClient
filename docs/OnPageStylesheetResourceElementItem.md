# OnPageStylesheetResourceElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResourceMetaInfo**](ResourceMetaInfo.md) |  | [optional] 
**fetch_timing** | [**FetchTiming**](FetchTiming.md) |  | [optional] 
**accept_type** | **str** | indicates the expected type of resource for example, if \&quot;resource_type\&quot;: \&quot;broken\&quot;, accept_type will indicate the type of the broken resource possible values: any, none, image, sitemap, robots, script, stylesheet, redirect, html, text, other, font | [optional] 
**initiator** | **str** | resource initiator | [optional] 
**duration_time** | **int** | total time it takes until a browser receives a complete response from a server (in milliseconds) | [optional] 
**fetch_start** | **int** | time to start downloading the resource the amount of time the browser needs to start downloading a resource | [optional] 
**fetch_end** | **int** | time to complete downloading the resource the amount of time the browser needs to complete downloading a resource | [optional] 
**is_render_blocking** | **bool** | indicates whether the resource blocks rendering | [optional] 

## Example

```python
from dataforseo_client.models.on_page_stylesheet_resource_element_item import OnPageStylesheetResourceElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageStylesheetResourceElementItem from a JSON string
on_page_stylesheet_resource_element_item_instance = OnPageStylesheetResourceElementItem.from_json(json)
# print the JSON string representation of the object
print(OnPageStylesheetResourceElementItem.to_json())

# convert the object into a dict
on_page_stylesheet_resource_element_item_dict = on_page_stylesheet_resource_element_item_instance.to_dict()
# create an instance of OnPageStylesheetResourceElementItem from a dict
on_page_stylesheet_resource_element_item_from_dict = OnPageStylesheetResourceElementItem.from_dict(on_page_stylesheet_resource_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



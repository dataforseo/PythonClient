# OnPageBrokenResourceElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PageMetaInfo**](PageMetaInfo.md) |  | [optional] 
**status_code** | **int** | status code of the page where a given resource is located | [optional] 
**location** | **str** | location header indicates the URL to redirect a page to | [optional] 
**url** | **str** | resource URL | [optional] 
**size** | **int** | resource size indicates the size of a given resource measured in bytes | [optional] 
**encoded_size** | **int** | resource size after encoding indicates the size of the encoded resource measured in bytes | [optional] 
**total_transfer_size** | **int** | compressed resource size indicates the compressed size of a given resource in bytes | [optional] 
**fetch_time** | **str** | date and time when a resource was fetched in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2021-02-17 13:54:15 +00:00 | [optional] 
**fetch_timing** | [**FetchTiming**](FetchTiming.md) |  | [optional] 
**cache_control** | [**CacheControl**](CacheControl.md) |  | [optional] 
**checks** | **Dict[str, Optional[bool]]** | resource check-ups contents of the array depend on the resource_type | [optional] 
**content_encoding** | **str** | type of encoding | [optional] 
**media_type** | **str** | types of media used to display a resource | [optional] 
**accept_type** | **str** | indicates the expected type of resource for example, if \&quot;resource_type\&quot;: \&quot;broken\&quot;, accept_type will indicate the type of the broken resource possible values: any, none, image, sitemap, robots, script, stylesheet, redirect, html, text, other, font | [optional] 
**server** | **str** | server version | [optional] 
**last_modified** | [**LastModified**](LastModified.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.on_page_broken_resource_element_item import OnPageBrokenResourceElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageBrokenResourceElementItem from a JSON string
on_page_broken_resource_element_item_instance = OnPageBrokenResourceElementItem.from_json(json)
# print the JSON string representation of the object
print(OnPageBrokenResourceElementItem.to_json())

# convert the object into a dict
on_page_broken_resource_element_item_dict = on_page_broken_resource_element_item_instance.to_dict()
# create an instance of OnPageBrokenResourceElementItem from a dict
on_page_broken_resource_element_item_form_dict = on_page_broken_resource_element_item.from_dict(on_page_broken_resource_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



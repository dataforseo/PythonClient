# OnPageHtmlResourceElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | status code of the page | [optional] 
**location** | **str** | location header indicates the URL to redirect a page to | [optional] 
**url** | **str** | page URL | [optional] 
**meta** | [**PageMetaInfo**](PageMetaInfo.md) |  | [optional] 
**page_timing** | [**PageTiming**](PageTiming.md) |  | [optional] 
**onpage_score** | **float** | shows how page is optimized on a 100-point scale this field shows how page is optimized considering critical on-page issues and warnings detected; 100 is the highest possible score that means the page does not have any critical on-page issues and important warnings; learn more about how the metric is calculated in this help center article | [optional] 
**total_dom_size** | **int** | total DOM size of a page | [optional] 
**custom_js_response** | **object** | the result of executing a specified JS script note that you should specify a custom_js field when setting a task to receive this data and the field type and its value will totally depend on the script you specified;you can also filter the results by this value specifying filters in the following way: [\&quot;custom_js_response.url\&quot;, \&quot;like\&quot;, \&quot;pixel\&quot;] | [optional] 
**resource_errors** | [**OnPageResourceIssueInfo**](OnPageResourceIssueInfo.md) |  | [optional] 
**broken_resources** | **bool** | indicates whether a page contains broken resources | [optional] 
**broken_links** | **bool** | indicates whether a page contains broken links | [optional] 
**duplicate_title** | **bool** | indicates whether a page has duplicate title tags | [optional] 
**duplicate_description** | **bool** | indicates whether a page has a duplicate description | [optional] 
**duplicate_content** | **bool** | indicates whether a page has duplicate content | [optional] 
**click_depth** | **int** | number of clicks it takes to get to the page indicates the number of clicks from the homepage needed before landing at the target page | [optional] 
**size** | **int** | resource size indicates the size of a given page measured in bytes | [optional] 
**encoded_size** | **int** | page size after encoding indicates the size of the encoded page measured in bytes | [optional] 
**total_transfer_size** | **int** | compressed page size indicates the compressed size of a given page | [optional] 
**fetch_time** | **str** | date and time when a resource was fetched in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**cache_control** | [**CacheControl**](CacheControl.md) |  | [optional] 
**checks** | **Dict[str, Optional[bool]]** | website checks on-page check-ups related to the page | [optional] 
**content_encoding** | **str** | type of encoding | [optional] 
**media_type** | **str** | types of media used to display a page | [optional] 
**server** | **str** | server version | [optional] 
**is_resource** | **bool** | indicates whether a page is a single resource | [optional] 
**url_length** | **int** | page URL length in characters | [optional] 
**relative_url_length** | **int** | relative URL length in characters | [optional] 
**last_modified** | [**LastModified**](LastModified.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.on_page_html_resource_element_item import OnPageHtmlResourceElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageHtmlResourceElementItem from a JSON string
on_page_html_resource_element_item_instance = OnPageHtmlResourceElementItem.from_json(json)
# print the JSON string representation of the object
print(OnPageHtmlResourceElementItem.to_json())

# convert the object into a dict
on_page_html_resource_element_item_dict = on_page_html_resource_element_item_instance.to_dict()
# create an instance of OnPageHtmlResourceElementItem from a dict
on_page_html_resource_element_item_form_dict = on_page_html_resource_element_item.from_dict(on_page_html_resource_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



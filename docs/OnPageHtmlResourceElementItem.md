# OnPageHtmlResourceElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PageMetaInfo**](PageMetaInfo.md) |  | [optional] 
**page_timing** | [**PageTiming**](PageTiming.md) |  | [optional] 
**onpage_score** | **float** | shows how page is optimized on a 100-point scale this field shows how page is optimized considering critical on-page issues and warnings detected; 100 is the highest possible score that means the page does not have any critical on-page issues and important warnings; learn more about how the metric is calculated in this help center article | [optional] 
**total_dom_size** | **int** | total DOM size of a page | [optional] 
**custom_js_response** | **object** | the result of executing a specified JS script note that you should specify a custom_js field when setting a task to receive this data and the field type and its value will totally depend on the script you specified;you can also filter the results by this value specifying filters in the following way: [\&quot;custom_js_response.url\&quot;, \&quot;like\&quot;, \&quot;pixel\&quot;] | [optional] 
**broken_resources** | **bool** | indicates whether a page contains broken resources | [optional] 
**broken_links** | **bool** | indicates whether a page contains broken links | [optional] 
**duplicate_title** | **bool** | indicates whether a page has duplicate title tags | [optional] 
**duplicate_description** | **bool** | indicates whether a page has a duplicate description | [optional] 
**duplicate_content** | **bool** | indicates whether a page has duplicate content | [optional] 
**click_depth** | **int** | number of clicks it takes to get to the page indicates the number of clicks from the homepage needed before landing at the target page | [optional] 
**is_resource** | **bool** | indicates whether a page is a single resource | [optional] 
**url_length** | **int** | page URL length in characters | [optional] 
**relative_url_length** | **int** | relative URL length in characters | [optional] 

## Example

```python
from dataforseo_client.models.on_page_html_resource_element_item import OnPageHtmlResourceElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageHtmlResourceElementItem from a JSON string
on_page_html_resource_element_item_instance = OnPageHtmlResourceElementItem.from_json(json)
# print the JSON string representation of the object
print OnPageHtmlResourceElementItem.to_json()

# convert the object into a dict
on_page_html_resource_element_item_dict = on_page_html_resource_element_item_instance.to_dict()
# create an instance of OnPageHtmlResourceElementItem from a dict
on_page_html_resource_element_item_form_dict = on_page_html_resource_element_item.from_dict(on_page_html_resource_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



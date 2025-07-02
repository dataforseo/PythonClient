# HtmlResourceElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**meta** | **PageMetaInfo** | page properties<br>the value depends on the resource_type |[optional]|
**page_timing** | **PageTiming** | object of page load metrics |[optional]|
**onpage_score** | **StrictFloat** | shows how page is optimized on a 100-point scale<br>this field shows how page is optimized considering critical on-page issues and warnings detected;<br>100 is the highest possible score that means the page does not have any critical on-page issues and important warnings;<br>learn more about how the metric is calculated in this help center article |[optional]|
**total_dom_size** | **StrictInt** | total DOM size of a page |[optional]|
**custom_js_response** | **Any** | the result of executing a specified JS script<br>note that you should specify a custom_js field when setting a task to receive this data and the field type and its value will totally depend on the script you specified;you can also filter the results by this value specifying filters in the following way:<br>['custom_js_response.url', 'like', 'pixel'] |[optional]|
**custom_js_client_exception** | **StrictStr** | error when executing a custom js<br>if the error occurred when executing the script you specified in the custom_js field, the error message would be displayed here |[optional]|
**broken_resources** | **StrictBool** | indicates whether a page contains broken resources |[optional]|
**broken_links** | **StrictBool** | indicates whether a page contains broken links |[optional]|
**duplicate_title** | **StrictBool** | indicates whether a page has duplicate title tags |[optional]|
**duplicate_description** | **StrictBool** | indicates whether a page has a duplicate description |[optional]|
**duplicate_content** | **StrictBool** | indicates whether a page has duplicate content |[optional]|
**click_depth** | **StrictInt** | number of clicks it takes to get to the page<br>indicates the number of clicks from the homepage needed before landing at the target page |[optional]|
**is_resource** | **StrictBool** | indicates whether a page is a single resource |[optional]|
**url_length** | **StrictInt** | page URL length in characters |[optional]|
**relative_url_length** | **StrictInt** | relative URL length in characters |[optional]|
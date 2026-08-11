# OnPageHtmlResourceItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**meta** | **PageMetaInfo** | <em>page properties</em><br>the value depends on the <code>resource_type</code> |[optional]|
**page_timing** | **PageTiming** | <em>object of page load metrics</em> |[optional]|
**onpage_score** | **StrictFloat** | <em>shows how page is optimized on a 100-point scale</em><br>this field shows how page is optimized considering critical on-page issues and warnings detected;<br><code>100</code> is the highest possible score that means the page does not have any critical on-page issues and important warnings;<br>learn more about how the metric is calculated in <a href='https://dataforseo.com/help-center/how-on-page-seo-score-is-calculated' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**total_dom_size** | **StrictInt** | <em>total <a href='https://developers.google.com/web/tools/chrome-devtools/dom' target='_blank' rel='noopener noreferrer'>DOM</a> size of a page</em> |[optional]|
**custom_js_response** | **Any** | <em>the result of executing a specified JS script</em><br><strong>note</strong> that you should specify a <code>custom_js</code> field when <a href='/v3/on_page/task_post/' target='_blank' rel='noopener noreferrer'>setting a task</a> to receive this data and the field type and its value will totally depend on the script you specified;<br>you can also filter the results by this value specifying <code>filters</code> in the following way:<br><code>['custom_js_response.url', 'like', 'pixel']</code> |[optional]|
**custom_js_client_exception** | **StrictStr** | <em>error when executing a custom js</em><br>if the error occurred when executing the script you specified in the <code>custom_js</code> field, the error message would be displayed here |[optional]|
**broken_resources** | **StrictBool** | <em>indicates whether a page contains broken resources</em> |[optional]|
**broken_links** | **StrictBool** | <em>indicates whether a page contains broken links</em> |[optional]|
**duplicate_title** | **StrictBool** | <em>indicates whether a page has duplicate <code>title</code> tags</em> |[optional]|
**duplicate_description** | **StrictBool** | <em>indicates whether a page has a duplicate description</em> |[optional]|
**duplicate_content** | **StrictBool** | <em>indicates whether a page has duplicate content</em> |[optional]|
**click_depth** | **StrictInt** | <em>number of clicks it takes to get to the page</em><br>indicates the number of clicks from the homepage needed before landing at the target page |[optional]|
**is_resource** | **StrictBool** | <em>indicates whether a page is a single resource</em> |[optional]|
**url_length** | **StrictInt** | <em>page URL length in characters</em> |[optional]|
**relative_url_length** | **StrictInt** | <em>relative URL length in characters</em> |[optional]|
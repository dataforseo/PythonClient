# RelatedResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**page** | **StrictInt** | <em>search results page number</em><br>indicates the number of the SERP page on which the element is located |[optional]|
**xpath** | **StrictStr** | <em>the <a href='https://en.wikipedia.org/wiki/XPath'>XPath</a> of the element</em> |[optional]|
**domain** | **StrictStr** | <em>website domain</em> |[optional]|
**title** | **StrictStr** | <em>title of a given link element</em> |[optional]|
**url** | **StrictStr** | <em>URL</em> |[optional]|
**cache_url** | **StrictStr** | <em>cached version of the page</em> |[optional]|
**related_search_url** | **StrictStr** | <em>URL to a similar search</em><br>URL to a new search for the same keyword(s) <a href='https://support.google.com/websearch/answer/2466433?hl=en#:~:text=Search%20for%20related%20sites'>on related sites</a> |[optional]|
**breadcrumb** | **StrictStr** | <em>breadcrumb in SERP</em> |[optional]|
**website_name** | **StrictStr** | <em>name of the website in the ad element</em> |[optional]|
**is_image** | **StrictBool** | <em>indicates whether the element contains an_<code class='prettyprint'>image</code></em><br><strong>Note:</strong> this check no longer appears in SERPn |[optional]|
**is_video** | **StrictBool** | <em>indicates whether the element contains a <code class='prettyprint'>video</code></em><br><strong>Note:</strong> this check no longer appears in SERP |[optional]|
**checks** | **List[Optional[StrictStr]]** | <em>array of properties detected for the SERP element</em><br>lists the properties that are true for this element<br>each value in the array represents a detected property <br>example:<br>if <code>is_image</code> is present in the array, the element contains an image<br>possible values in the array:<br><code>is_image</code>, <code>is_video</code>, <code>is_featured_snippet</code>, <code>amp_version</code>, <code>is_malicious</code>, <code>is_web_story</code>, <code>is_highly_cited</code><br>equals <code>null</code> if none of the properties are detected for the element<br>learn more about the <code>checks</code> array in <a href='https://dataforseo.com/help-center/whats-a-checks-array-in-the-google-organic-serp-api' target='_blank'>this Help Center article</a> |[optional]|
**description** | **StrictStr** | <em>description of the results element in SERP</em> |[optional]|
**pre_snippet** | **StrictStr** | <em>includes additional information appended before the result description in SERP</em> |[optional]|
**extended_snippet** | **StrictStr** | <em>includes additional information appended after the result description in SERP</em> |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | <em>images of the component</em><br>if there are none, equals <code>null</code> |[optional]|
**amp_version** | **StrictBool** | <em>Accelerated Mobile Pages</em><br>indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**rating** | **RatingInfo** | <em>the item's rating </em><br>the popularity rate based on reviews and displayed in SERP;<br>if there is none, equals <code>null</code> |[optional]|
**price** | **PriceInfo** | <em>price of booking a place for the specified dates of stay</em> |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | <em>words highlighted in bold within the results <code>description</code></em> |[optional]|
**about_this_result** | **AboutThisResultElement** | <em>contains information from the 'About this result' panel</em><br><strong>Note:</strong> this object is deprecated and always returns <code>null</code> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the result was published</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
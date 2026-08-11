# OrganicSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank in SERP</em><br>absolute position among all the elements found in SERP<strong>note</strong> values are returned in the ascending order, with values corresponding to advanced SERP features omitted from the results;<br>to get all items (including SERP features and rich snippets) with their positions, please refer to the <a href='https://docs.dataforseo.com/v3/serp/google/organic/live/advanced/?php'>Google Organiс Advanced SERP</a> endpoint |[optional]|
**domain** | **StrictStr** | <em>domain in SERP</em> |[optional]|
**title** | **StrictStr** | <em>title of the results element in SERP</em> |[optional]|
**description** | **StrictStr** | <em>description of the results element in SERP</em> |[optional]|
**url** | **StrictStr** | <em> relevant URL in SERP</em> |[optional]|
**breadcrumb** | **StrictStr** | <em>breadcrumb in SERP</em> |[optional]|
**cache_url** | **StrictStr** | <em>cached version of the page</em> |[optional]|
**related_search_url** | **StrictStr** | <em>URL to a similar search</em><br>URL to a new search for the same keyword(s) <a href='https://support.google.com/websearch/answer/2466433?hl=en#:~:text=Search%20for%20related%20sites'>on related sites</a> |[optional]|
**website_name** | **StrictStr** | <em>name of the website in SERP</em> |[optional]|
**is_image** | **StrictBool** | <em>indicates whether the element contains an_<code class='prettyprint'>image</code></em><br><strong>Note:</strong> this check no longer appears in SERPn |[optional]|
**is_video** | **StrictBool** | <em>indicates whether the element contains a <code class='prettyprint'>video</code></em><br><strong>Note:</strong> this check no longer appears in SERP |[optional]|
**is_featured_snippet** | **StrictBool** | <em>indicates whether the element is a <code class='prettyprint'>featured_snippet</code></em><br><strong>Note:</strong> this check no longer appears in SERP |[optional]|
**is_malicious** | **StrictBool** | <em>indicates whether the element is marked as malicious</em><br><strong>Note:</strong> this check no longer appears in SERP |[optional]|
**is_web_story** | **StrictBool** | <em>indicates whether the element is marked as Google web story</em><br><strong>Note:</strong> this check no longer appears in SERP |[optional]|
**checks** | **List[Optional[StrictStr]]** | <em>array of properties detected for the SERP element</em><br>lists the properties that are true for this element<br>each value in the array represents a detected property <br>example:<br>if <code>is_image</code> is present in the array, the element contains an image<br>possible values in the array:<br><code>is_image</code>, <code>is_video</code>, <code>is_featured_snippet</code>, <code>amp_version</code>, <code>is_malicious</code>, <code>is_web_story</code>, <code>is_highly_cited</code><br>equals <code>null</code> if none of the properties are detected for the element<br>learn more about the <code>checks</code> array in <a href='https://dataforseo.com/help-center/whats-a-checks-array-in-the-google-organic-serp-api' target='_blank'>this Help Center article</a> |[optional]|
**pre_snippet** | **StrictStr** | <em>includes additional information appended before the result description in SERP</em> |[optional]|
**extended_snippet** | **StrictStr** | <em>includes additional information appended after the result description in SERP</em> |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | <em>images of the element</em><br>if there are none, equals <code>null</code> |[optional]|
**amp_version** | **StrictBool** | <em>Accelerated Mobile Pages</em><br>indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**rating** | **RatingInfo** | <em>the item's rating </em><br>the popularity rate based on reviews and displayed in SERP<br>if there is none, equals <code>null</code> |[optional]|
**price** | **PriceInfo** | <em>pricing details</em><br>contains the pricing details of the product or service featured in the result;<br>if there is none, equals <code>null</code> |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | <em>words highlighted in bold within the results <code>description</code></em> |[optional]|
**links** | **List[Optional[LinkElement]]** | <em>link of the element</em> |[optional]|
**faq** | **FaqBox** | <em>frequently asked questions</em><br>questions and answers extension shown below some of Google's search results<br><strong>Note:</strong> this object is deprecated and always returns <code>null</code> |[optional]|
**extended_people_also_search** | **List[Optional[StrictStr]]** | <em>extension of the organic element</em><br>extension of the organic result containing related search queries<br><strong>Note:</strong> extension appears in SERP upon clicking on the result and then bouncing back to search results |[optional]|
**about_this_result** | **AboutThisResultElement** | <em>contains information from the 'About this result' panel</em><br><strong>Note:</strong> this object is deprecated and always returns <code>null</code> |[optional]|
**related_result** | **List[Optional[RelatedResult]]** | <em>related result from the same domain</em><br>related result from the same domain appears as a part of the main result snippet;<br>you can derive the <code>related_result</code> snippets as <code>'type': 'organic'</code> results by setting the <code>group_organic_results</code> parameter to <code>false</code> in the POST request |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the result was published</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
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
**cache_url** | **StrictStr** | cached version of the page |[optional]|
**related_search_url** | **StrictStr** | URL to a similar search<br>URL to a new search for the same keyword(s) on related sites |[optional]|
**website_name** | **StrictStr** | name of the website in SERP |[optional]|
**is_image** | **StrictBool** | indicates whether the element contains an image<br>Note: this check no longer appears in SERP |[optional]|
**is_video** | **StrictBool** | indicates whether the element contains a video<br>Note: this check no longer appears in SERP |[optional]|
**is_featured_snippet** | **StrictBool** | indicates whether the element is a featured_snippet<br>Note: this check no longer appears in SERP |[optional]|
**is_malicious** | **StrictBool** | indicates whether the element is marked as malicious<br>Note: this check no longer appears in SERP |[optional]|
**is_web_story** | **StrictBool** | indicates whether the element is marked as Google web story<br>Note: this check no longer appears in SERP |[optional]|
**checks** | **List[Optional[StrictStr]]** | array of properties detected for the SERP element<br>lists the properties that are true for this element<br>each value in the array represents a detected property<br>example:<br>if is_image is present in the array, the element contains an image<br>possible values in the array:<br>is_image, is_video, is_featured_snippet, amp_version, is_malicious, is_web_story, is_highly_cited<br>equals null if none of the properties are detected for the element<br>learn more about the checks array in this Help Center article |[optional]|
**pre_snippet** | **StrictStr** | includes additional information appended before the result description in SERP |[optional]|
**extended_snippet** | **StrictStr** | includes additional information appended after the result description in SERP |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the element<br>if there are none, equals null |[optional]|
**amp_version** | **StrictBool** | Accelerated Mobile Pages<br>indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP<br>if there is none, equals null |[optional]|
**price** | **PriceInfo** | pricing details<br>contains the pricing details of the product or service featured in the result;<br>if there is none, equals null |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**links** | **List[Optional[LinkElement]]** | link of the element |[optional]|
**faq** | **FaqBox** | frequently asked questions<br>questions and answers extension shown below some of Google’s search results<br>Note: this object is deprecated and always returns null |[optional]|
**extended_people_also_search** | **List[Optional[StrictStr]]** | extension of the organic element<br>extension of the organic result containing related search queries<br>Note: extension appears in SERP upon clicking on the result and then bouncing back to search results |[optional]|
**about_this_result** | **AboutThisResultElement** | contains information from the ‘About this result’ panel<br>Note: this object is deprecated and always returns null |[optional]|
**related_result** | **List[Optional[RelatedResult]]** | related result from the same domain<br>related result from the same domain appears as a part of the main result snippet;<br>you can derive the related_result snippets as 'type': 'organic' results by setting the group_organic_results parameter to false in the POST request |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
# OrganicSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements found in SERP<br>note values are returned in the ascending order, with values corresponding to advanced SERP features omitted from the results;<br>to get all items (including SERP features and rich snippets) with their positions, please refer to the Google Organiс Advanced SERP endpoint |[optional]|
**domain** | **StrictStr** | domain in SERP |[optional]|
**title** | **StrictStr** | title of the results element in SERP |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**url** | **StrictStr** | relevant URL in SERP |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb in SERP |[optional]|
**cache_url** | **StrictStr** | cached version of the page |[optional]|
**related_search_url** | **StrictStr** | URL to a similar search<br>URL to a new search for the same keyword(s) on related sites |[optional]|
**website_name** | **StrictStr** | name of the website in SERP |[optional]|
**is_image** | **StrictBool** | indicates whether the element contains an image |[optional]|
**is_video** | **StrictBool** | indicates whether the element contains a video |[optional]|
**is_featured_snippet** | **StrictBool** | indicates whether the element is a featured_snippet |[optional]|
**is_malicious** | **StrictBool** | indicates whether the element is marked as malicious |[optional]|
**is_web_story** | **StrictBool** | indicates whether the element is marked as Google web story |[optional]|
**pre_snippet** | **StrictStr** | includes additional information appended before the result description in SERP |[optional]|
**extended_snippet** | **StrictStr** | includes additional information appended after the result description in SERP |[optional]|
**images** | **List[Optional[AiModeImagesElement]]** | images of the element<br>if there are none, equals null |[optional]|
**amp_version** | **StrictBool** | Accelerated Mobile Pages<br>indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**price** | **PriceInfo** | pricing details<br>contains the pricing details of the product or service featured in the result |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**faq** | **FaqBox** | frequently asked questions<br>questions and answers extension shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**extended_people_also_search** | **List[Optional[StrictStr]]** | extension of the organic element<br>extension of the organic result containing related search queries<br>Note: extension appears in SERP upon clicking on the result and then bouncing back to search results |[optional]|
**about_this_result** | **AboutThisResultElement** | contains information from the ‘About this result’ panel<br>‘About this result’ panel provides additional context about why Google returned this result for the given query;<br>this feature appears after clicking on the three dots next to most results |[optional]|
**related_result** | **List[Optional[RelatedResult]]** | related result from the same domain<br>related result from the same domain appears as a part of the main result snippet;<br>you can derive the related_result snippets as 'type': 'organic' results by setting the group_organic_results parameter to false in the POST request |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
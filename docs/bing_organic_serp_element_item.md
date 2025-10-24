# BingOrganicSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | domain in SERP |[optional]|
**title** | **StrictStr** | title of the results element in SERP |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**url** | **StrictStr** | relevant URL in SERP |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb in SERP |[optional]|
**cache_url** | **StrictStr** | cached version of the page |[optional]|
**related_search_url** | **StrictStr** | URL to a similar search<br>URL to a new search for the same keyword(s) on related sites |[optional]|
**website_name** | **StrictStr** | name of the source website |[optional]|
**is_image** | **StrictBool** | indicates whether the element contains an image |[optional]|
**is_video** | **StrictBool** | indicates whether the element contains a video |[optional]|
**is_featured_snippet** | **StrictBool** | indicates whether the element is a featured_snippet |[optional]|
**is_malicious** | **StrictBool** | indicates whether the element is marked as malicious |[optional]|
**is_web_story** | **StrictBool** | indicates whether the element is marked as a web story |[optional]|
**pre_snippet** | **StrictStr** | includes additional information appended before the result description in SERP |[optional]|
**extended_snippet** | **StrictStr** | includes additional information appended after the result description in SERP |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the element |[optional]|
**amp_version** | **StrictBool** | Accelerated Mobile Pages<br>indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**price** | **PriceInfo** | pricing details<br>contains the pricing details of the product or service featured in the result |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some search results<br>if there are none, equals null |[optional]|
**faq** | **FaqBox** | frequently asked questions<br>questions and answers extension shown below some search results<br>if there are none, equals null |[optional]|
**extended_people_also_search** | **List[Optional[StrictStr]]** | extension of the organic element<br>extension of the organic result containing related search queries<br>Note: extension appears in SERP upon clicking on the result and then bouncing back to search results |[optional]|
**about_this_result** | **AboutThisResultElement** | contains information from the ‘About this result’ panel<br>note: about_this_result feature is not available in Bing search engine, that’s why it always equals null |[optional]|
**related_result** | **List[Optional[RelatedResult]]** | related result from the same domain<br>related result from the same domain appears as a part of the main result snippet;<br>note: related_result feature is not available in Bing search engine, that’s why it always equals null |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
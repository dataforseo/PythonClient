# RelatedResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**domain** | **StrictStr** | domain where a link points |[optional]|
**title** | **StrictStr** | title of a given link element |[optional]|
**url** | **StrictStr** | reference page URL |[optional]|
**cache_url** | **StrictStr** | cached version of the page |[optional]|
**related_search_url** | **StrictStr** | URL to a similar search<br>URL to a new search for the same keyword(s) on related sites |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb in SERP |[optional]|
**website_name** | **StrictStr** | name of the website in the ad element |[optional]|
**is_image** | **StrictBool** | indicates whether the element contains an image |[optional]|
**is_video** | **StrictBool** | indicates whether the element contains a video |[optional]|
**description** | **StrictStr** | description of the hotel booking element |[optional]|
**pre_snippet** | **StrictStr** | includes additional information appended before the result description in SERP |[optional]|
**extended_snippet** | **StrictStr** | includes additional information appended after the result description in SERP |[optional]|
**images** | **List[Optional[ImagesElement]]** | images of the element |[optional]|
**amp_version** | **StrictBool** | Accelerated Mobile Pages<br>indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**rating** | **BusinessDataRatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**price** | **PriceInfo** | price of booking a place for the specified dates of stay |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**about_this_result** | **AboutThisResultElement** | contains information from the ‘About this result’ panel<br>‘About this result’ panel provides additional context about why Google returned this result for the given query;<br>this feature appears after clicking on the three dots next to most results |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
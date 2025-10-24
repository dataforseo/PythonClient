# PaidSerpElementItem


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
**website_name** | **StrictStr** | name of the website in SERP |[optional]|
**is_image** | **StrictBool** | indicates whether the element contains an image |[optional]|
**is_video** | **StrictBool** | indicates whether the element contains a video |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the element<br>if there are none, equals null |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**extra** | **Dict[str, Optional[StrictStr]]** | additional information about the result |[optional]|
**description_rows** | **List[Optional[StrictStr]]** | extended description<br>if there is none, equals null |[optional]|
**links** | **List[Optional[AdLinkElement]]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**price** | **PriceInfo** | price of booking a place for the specified dates of stay |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
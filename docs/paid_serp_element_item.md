# PaidSerpElementItem


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
**website_name** | **StrictStr** | name of the website in SERP |[optional]|
**is_image** | **StrictBool** | indicates whether the element contains an image |[optional]|
**is_video** | **StrictBool** | indicates whether the element contains a video |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the element<br>if there are none, equals null |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**extra** | **Dict[str, Optional[StrictStr]]** | additional information about the result |[optional]|
**description_rows** | **List[Optional[StrictStr]]** | extended description<br>if there is none, equals null |[optional]|
**links** | **List[Optional[AdLinkElement]]** | link of the element |[optional]|
**price** | **PriceInfo** | pricing details<br>contains the pricing details of the product or service featured in the result;<br>if there is none, equals null |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP<br>if there is none, equals null |[optional]|
# PaidSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**domain** | **StrictStr** | domain name of the reference |[optional]|
**website_name** | **StrictStr** | name of the website in SERP |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb in SERP |[optional]|
**is_image** | **StrictBool** | indicates whether the element contains an image |[optional]|
**is_video** | **StrictBool** | indicates whether the element contains a video |[optional]|
**images** | **List[Optional[ImagesElement]]** | images of the element |[optional]|
**url** | **StrictStr** | relevant URL in SERP |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**extra** | **Dict[str, Optional[StrictStr]]** | additional information about the result |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**description_rows** | **List[Optional[StrictStr]]** | extended description<br>if there is none, equals null |[optional]|
**links** | **List[Optional[AdLinkElement]]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**price** | **PriceInfo** | pricing details<br>contains the pricing details of the product or service featured in the result |[optional]|
**rating** | **BusinessDataRatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|
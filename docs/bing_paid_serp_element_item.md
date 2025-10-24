# BingPaidSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | domain of the ad element in SERP |[optional]|
**title** | **StrictStr** | title of the ad element in SERP |[optional]|
**description** | **StrictStr** | description of the ad element in SERP |[optional]|
**url** | **StrictStr** | relevant URL of the ad element in SERP |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb of the ad element in SERP |[optional]|
**website_name** | **StrictStr** | website name in SERP |[optional]|
**is_image** | **StrictBool** | indicates whether the element contains an image |[optional]|
**is_video** | **StrictBool** | indicates whether the element contains a video |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the element |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**extra** | **Dict[str, Optional[StrictStr]]** | additional information about the result |[optional]|
**description_rows** | **List[Optional[StrictStr]]** | extended description<br>if there is none, equals null |[optional]|
**links** | **List[Optional[AdLinkElement]]** | links featured in the organic result |[optional]|
**price** | **PriceInfo** | price of the shopping element |[optional]|
**rating** | **RatingInfo** | the item’s rating<br>the popularity rate based on reviews and displayed in SERP |[optional]|
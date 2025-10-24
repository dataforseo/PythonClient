# BingPaidSerpElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **string** | domain of the ad element in SERP |[optional]|
**title** | **string** | title of the ad element in SERP |[optional]|
**description** | **string** | description of the ad element in SERP |[optional]|
**url** | **string** | relevant URL of the ad element in SERP |[optional]|
**breadcrumb** | **string** | breadcrumb of the ad element in SERP |[optional]|
**website_name** | **string** | website name in SERP |[optional]|
**is_image** | **boolean** | indicates whether the element contains an image |[optional]|
**is_video** | **boolean** | indicates whether the element contains a video |[optional]|
**images** | **AiModeImagesElementInfo[]** | images of the element |[optional]|
**highlighted** | **string[]** | words highlighted in bold within the results description |[optional]|
**extra** | **{ [key: string]: string; }** | additional information about the result |[optional]|
**description_rows** | **string[]** | extended description<br>if there is none, equals null |[optional]|
**links** | **AdLinkElement[]** | links featured in the organic result |[optional]|
**price** | **PriceInfo** | price of the shopping element |[optional]|
**rating** | **RatingInfo** | the item’s rating<br>the popularity rate based on reviews and displayed in SERP |[optional]|
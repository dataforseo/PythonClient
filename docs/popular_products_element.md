# PopularProductsElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | title of a given link element |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**more_sellers** | **StrictBool** | indicates whether the product is sold by multiple sellers |[optional]|
**seller** | **StrictStr** | seller of the product |[optional]|
**image_url** | **StrictStr** | URL of the image<br>the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
**price** | **PriceInfo** | price indicated in the element |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP;<br>if there is none, equals null |[optional]|
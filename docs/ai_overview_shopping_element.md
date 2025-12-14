# AiOverviewShoppingElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**product_id** | **StrictStr** |  |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**url** | **StrictStr** | reference page URL |[optional]|
**domain** | **StrictStr** | domain in link |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**price** | **Price** | pricing details<br>contains the pricing details of the product or service featured in the result |[optional]|
**seller** | **StrictStr** | seller of the product |[optional]|
**snippet** | **StrictStr** | text alongside the link title |[optional]|
**marketplace** | **StrictStr** | merchant account provider<br>commerce site that hosts products or websites of individual sellers under the same merchant account<br>example:<br>by Google |[optional]|
**marketplace_url** | **StrictStr** | relevant marketplace URL<br>URL of the page on the marketplace website where the product is hosted |[optional]|
**image_url** | **StrictStr** | URL of the image<br>the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
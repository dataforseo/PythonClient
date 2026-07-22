# ShoppingElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | title of a given link element |[optional]|
**price** | **PriceInfo** | price indicated in the element |[optional]|
**source** | **StrictStr** | reference source name or title |[optional]|
**description** | **StrictStr** | link description |[optional]|
**marketplace** | **StrictStr** | merchant account provider<br>commerce site that hosts products or websites of individual sellers under the same merchant account<br>example:<br>by Google |[optional]|
**marketplace_url** | **StrictStr** | relevant marketplace URL<br>URL of the page on the marketplace website where the product is hosted |[optional]|
**url** | **StrictStr** | source URL |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP;<br>if there is none, equals null |[optional]|
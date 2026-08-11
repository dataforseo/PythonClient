# ShoppingElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | <em>title of a given link element</em> |[optional]|
**price** | **PriceInfo** | <em>price indicated in the element</em> |[optional]|
**source** | **StrictStr** | <em>reference source name or title</em> |[optional]|
**description** | **StrictStr** | <em>link description</em> |[optional]|
**marketplace** | **StrictStr** | <em>merchant account provider</em><br>commerce site that hosts products or websites of individual sellers under the same merchant account<br>example:<br><code>by Google</code> |[optional]|
**marketplace_url** | **StrictStr** | <em>relevant marketplace URL</em><br>URL of the page on the marketplace website where the product is hosted |[optional]|
**url** | **StrictStr** | <em>source URL</em> |[optional]|
**rating** | **RatingInfo** | <em>the item's rating </em><br>the popularity rate based on reviews and displayed in SERP;<br>if there is none, equals <code>null</code> |[optional]|
# KnowledgeGraphShoppingElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | <em>title of the element</em> |[optional]|
**url** | **StrictStr** | <em>URL</em> |[optional]|
**domain** | **StrictStr** | <em>domain where a link points</em> |[optional]|
**price** | **PriceInfo** | <em>pricing details</em><br>contains the pricing details of the product or service featured in the result;<br>if there is none, equals <code>null</code> |[optional]|
**source** | **StrictStr** | <em>reference source name or title</em> |[optional]|
**snippet** | **StrictStr** | <em>text alongside the link title</em> |[optional]|
**marketplace** | **StrictStr** | <em>merchant account provider</em><br>ecommerce site that hosts products or websites of individual sellers under the same merchant account<br>example:<br><code>by Google</code> |[optional]|
**marketplace_url** | **StrictStr** | <em>URL to the merchant account provider</em><br>ecommerce site that hosts products or websites of individual sellers under the same merchant account |[optional]|
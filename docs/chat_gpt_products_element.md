# ChatGptProductsElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**product_id** | **StrictStr** | product id |[optional]|
**merchants** | **StrictStr** | merchant(s) offering the product |[optional]|
**id_to_token_map** | **StrictStr** | product identifier tokenBase64-encoded token containing Google Shopping product IDs associated with the product |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**rating** | **RatingInfo** | rating of the corresponding local businesspopularity rate based on reviews as displayed in the results |[optional]|
**price** | **StrictFloat** | product price |[optional]|
**currency** | **StrictStr** | currency of the listed priceISO code of the currency applied to the price |[optional]|
**tag** | **StrictStr** | tag text |[optional]|
**url** | **StrictStr** | URL |[optional]|
**domain** | **StrictStr** | domain |[optional]|
**images** | **List[Optional[StrictStr]]** | image URLs of the elementcontains URLs leading to the images on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
**product_ids** | **List[Optional[ChatGptGoogleShoppingProduct]]** | Google Shopping product identifiersarray of Google Shopping product IDs associated with the product |[optional]|
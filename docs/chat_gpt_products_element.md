# ChatGptProductsElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**product_id** | **StrictStr** | <em>product id</em> |[optional]|
**merchants** | **StrictStr** | <em>merchant(s) offering the product</em> |[optional]|
**id_to_token_map** | **StrictStr** | <em>product identifier token</em><br>Base64-encoded token containing Google Shopping product IDs associated with the product |[optional]|
**title** | **StrictStr** | <em>title of the element</em> |[optional]|
**rating** | **RatingInfo** | <em>rating of the corresponding local business</em><br>popularity rate based on reviews as displayed in the results |[optional]|
**price** | **StrictFloat** | <em>product price</em> |[optional]|
**currency** | **StrictStr** | <em>currency of the listed price</em><br>ISO code of the currency applied to the price |[optional]|
**tag** | **StrictStr** | <em>tag text</em> |[optional]|
**url** | **StrictStr** | <em>URL</em> |[optional]|
**domain** | **StrictStr** | <em>domain</em> |[optional]|
**images** | **List[Optional[StrictStr]]** | <em>image URLs of the element</em><br>contains URLs leading to the images on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
**product_ids** | **List[Optional[ChatGptGoogleShoppingProduct]]** | <em>Google Shopping product identifiers</em><br>array of Google Shopping product IDs associated with the product |[optional]|
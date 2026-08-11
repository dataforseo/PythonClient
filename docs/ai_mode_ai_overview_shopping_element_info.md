# AiModeAiOverviewShoppingElementInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**product_id** | **StrictStr** | <em>unique product identifier on Google Shopping</em><br>learn more about the parameter in <a href='https://dataforseo.com/help-center/product-id-google-shopping' rel='noopener noreferrer' target='_blank'>this help center guide</a> |[optional]|
**data_docid** | **StrictStr** | <em>unique identifier of the SERP data element</em> |[optional]|
**gid** | **StrictStr** | <em>global product identifier on Google Shopping</em><br>learn more about the parameter in <a href='https://dataforseo.com/help-center/whats-a-gid-in-google-shopping-api' rel='noopener noreferrer' target='_blank'>this help center guide</a> |[optional]|
**title** | **StrictStr** | <em>reference page title</em> |[optional]|
**url** | **StrictStr** | <em>URL in link</em> |[optional]|
**domain** | **StrictStr** | <em>domain in link</em> |[optional]|
**rating** | **RatingInfo** | <em>product rating </em><br>the popularity rate based on reviews<br> if there is none, the value will be <code>null</code> |[optional]|
**price** | **PriceInfo** | <em>product price</em><br>product price details on the seller's website;<br> if there is none, the value will be <code>null</code> |[optional]|
**seller** | **StrictStr** | <em>product seller</em><br>name of the product's seller as displayed in search results |[optional]|
**snippet** | **StrictStr** | <em>additional information about the result</em> |[optional]|
**marketplace** | **StrictStr** | <em>merchant account provider</em><br>e-commerce site that hosts products or websites of individual sellers under the same merchant account<br>example:<br><code>by Google</code> |[optional]|
**marketplace_url** | **StrictStr** | <em>URL to the merchant account provider</em><br>e-commerce site that hosts products or websites of individual sellers under the same merchant account |[optional]|
**image_url** | **StrictStr** | <em>URL of the image</em><br>the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
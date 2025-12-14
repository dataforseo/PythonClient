# ChatGptProductsElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**product_id** | **StrictStr** | product id |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**rating** | **RatingInfo** | rating of the corresponding local businesses<br>popularity rate based on reviews as displayed in the results |[optional]|
**price** | **StrictFloat** | product price |[optional]|
**currency** | **StrictStr** | currency of the listed price<br>ISO code of the currency applied to the price |[optional]|
**tag** | **StrictStr** | tag text |[optional]|
**url** | **StrictStr** | URL |[optional]|
**domain** | **StrictStr** | domain |[optional]|
**images** | **List[Optional[StrictStr]]** | image URLs of the element<br>contains URLs leading to the images on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
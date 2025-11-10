# ProductSeller


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | product title |[optional]|
**url** | **StrictStr** | seller url<br>url of the page where the product is sold |[optional]|
**seller_rating** | **RatingElement** | rating of the seller |[optional]|
**seller_review_count** | **StrictInt** | number of seller reviews<br>number of reviews on the product seller’s account |[optional]|
**price** | **PriceInfo** | product price<br>product price details on the seller’s website |[optional]|
**delivery_info** | **DeliveryInfo** | delivery information<br>product delivery information |[optional]|
**product_availability** | **StrictStr** | product availability information<br>can take the following values: in_stock, limited_stock, out_of_stock, backordered, pre_order_available, on_display_to_order |[optional]|
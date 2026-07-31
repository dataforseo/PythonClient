# ProductSeller


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | <em>product title</em> |[optional]|
**url** | **StrictStr** | <em>seller url</em><br>url of the page where the product is sold |[optional]|
**seller_rating** | **RatingElement** | <em>rating of the seller</em> |[optional]|
**seller_review_count** | **StrictInt** | number of seller reviews<br>number of reviews on the product seller’s account |[optional]|
**price** | **PriceInfo** | <em>product price</em><br>product price details on the seller's website |[optional]|
**delivery_info** | **DeliveryInfo** | <em>delivery information</em><br>product delivery information |[optional]|
**product_availability** | **StrictStr** | <em>product availability information</em><br>can take the following values: <code>in_stock</code>, <code>limited_stock</code>, <code>out_of_stock</code>, <code>backordered</code>, <code>pre_order_available</code>, <code>on_display_to_order</code> |[optional]|
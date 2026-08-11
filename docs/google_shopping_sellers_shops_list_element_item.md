# GoogleShoppingSellersShopsListElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**price_multiplier** | **StrictInt** | <em>monthly price multiplier</em><br>indicates the number of months covered by the monthly payment for the product |[optional]|
**displayed_payment_breakdown** | **StrictStr** | <em>installment details as displayed in the results</em><br>shows how the product price can be broken down into monthly payments, if applicable |[optional]|
**rating** | **RatingElement** | <em>shop rating</em><br>the shop popularity rate based on product reviews |[optional]|
**product_condition** | **StrictStr** | <em>indicated condition of the product</em><br>possible values: <code>Used</code>, <code>Refurbished</code>, <code>New</code>, <code>Pre-owned</code>, <code>null</code> |[optional]|
**product_annotation** | **StrictStr** | <em>data from annotations and badges with special offers</em><br>if there is no annotation for this product, the value will be <code>null</code><br>examples: <code>LOW PRICE</code>, <code>SPECIAL OFFER</code>, <code>SALE</code>, <code>PRICE DROP</code> |[optional]|
**product_availability** | **StrictStr** | <em>product availability information</em><br>product availability information<br>can take the following values: <code>in_stock</code>, <code>limited_stock</code>, <code>out_of_stock</code>, <code>backordered</code>, <code>pre_order_available</code>, <code>on_display_to_order</code> |[optional]|
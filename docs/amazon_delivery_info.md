# AmazonDeliveryInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**delivery_message** | **StrictStr** | message accompanying the delivery information as posted by the seller |[optional]|
**delivery_date_from** | **StrictStr** | the earliest date when the product can be shipped |[optional]|
**delivery_date_to** | **StrictStr** | the latest date when the product can be delivered |[optional]|
**fastest_delivery_date_from** | **StrictStr** | the earliest date when the product can be delivered with a fast delivery option |[optional]|
**fastest_delivery_date_to** | **StrictStr** | the latest date when the product can be delivered with a fast delivery option |[optional]|
**delivery_price** | **PriceInfo** | price for the delivery<br>price of the delivery based on the location you specified in the POST request;<br>if free delivery is available, the value is null |[optional]|
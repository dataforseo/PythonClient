# DeliveryInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**delivery_date_from** | **StrictStr** | earliest delivery datethe earliest date when the product can be shipped |[optional]|
**delivery_date_to** | **StrictStr** | latest delivery datethe latest date when the product can be delivered |[optional]|
**fastest_delivery_date_from** | **StrictStr** | earliest free delivery datethe earliest date when the product can be delivered with a fast delivery option |[optional]|
**fastest_delivery_date_to** | **StrictStr** | latest free delivery datethe latest date when the product can be delivered with a fast delivery option |[optional]|
**delivery_message** | **StrictStr** | delivery informationmessage accompanying the delivery information as posted by the seller |[optional]|
**delivery_price** | **PriceInfo** | price for the deliveryprice of the delivery based on the location you specified in the POST request;if free delivery is available, the value is null |[optional]|
# AmazonAmazonSellerMainItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**seller_name** | **StrictStr** | business name of the seller |[optional]|
**seller_url** | **StrictStr** | url forwarding to the seller’s page on Amazon |[optional]|
**ships_from** | **StrictStr** | sender company name |[optional]|
**price** | **PriceInfo** | product pricing details<br>if there are no details, the value will be null |[optional]|
**rating** | **RatingElement** | seller rating details<br>seller popularity rate based on customer reviews |[optional]|
**condition** | **StrictStr** | product condition<br>condition of the product offered by the seller |[optional]|
**condition_description** | **StrictStr** | product condition details<br>expanded details on the condition of the product offered by the seller |[optional]|
**delivery_info** | **AmazonDeliveryInfo** | delivery information<br>delivery information including free and fast delivery date ranges |[optional]|
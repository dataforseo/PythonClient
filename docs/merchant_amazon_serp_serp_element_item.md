# MerchantAmazonSerpSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | Amazon domain |[optional]|
**title** | **StrictStr** | product title |[optional]|
**url** | **StrictStr** | the URL of the product page |[optional]|
**image_url** | **StrictStr** | URL of the product image featured in the results |[optional]|
**bought_past_month** | **StrictInt** | number of product purchases in the past month |[optional]|
**price_from** | **StrictFloat** | the regular price of a product<br>example:<br>49.98 |[optional]|
**price_to** | **StrictFloat** | the upper limit of the product price range<br>example:<br>384.99 |[optional]|
**currency** | **StrictStr** | currency in the ISO format<br>example:<br>USD |[optional]|
**special_offers** | **List[Optional[StrictStr]]** | special offer details<br>contains special offer details, including coupon and Subscribe & Save discounts |[optional]|
**data_asin** | **StrictStr** | unique product identifier on Amazon<br>note that there is no full list of possible values as the data_asin is a dynamic value assigned by Amazon<br>example:<br>B07G82D89J |[optional]|
**rating** | **RatingElement** | product rating info |[optional]|
**is_amazon_choice** | **StrictBool** | “Amazon’s choice” label<br>if the value is true, the product is marked with the “Amazon’s choice” label |[optional]|
**is_best_seller** | **StrictBool** | “Best Seller” label<br>if the value is true, the product is marked with the “Best Seller” label |[optional]|
**delivery_info** | **AmazonDeliveryInfo** | delivery information<br>delivery information including free and fast delivery date ranges |[optional]|
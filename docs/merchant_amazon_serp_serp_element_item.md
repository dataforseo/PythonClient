# MerchantAmazonSerpSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | <em>Amazon domain</em> |[optional]|
**title** | **StrictStr** | <em>product title</em> |[optional]|
**url** | **StrictStr** | <em>the URL of the product page</em> |[optional]|
**image_url** | **StrictStr** | <em>URL of the product image featured in the results</em> |[optional]|
**bought_past_month** | **StrictInt** | <em>number of product purchases in the past month</em> |[optional]|
**price_from** | **StrictFloat** | <em>the regular price of a product</em><br>example:<br><code>49.98</code> |[optional]|
**price_to** | **StrictFloat** | <em>the upper limit of the product price range</em><br>example:<br><code>384.99</code> |[optional]|
**currency** | **StrictStr** | <em>currency in the <a href='https://en.wikipedia.org/wiki/ISO_4217'>ISO</a> format</em><br>example:<br><code>USD</code> |[optional]|
**special_offers** | **List[Optional[StrictStr]]** | <em>special offer details</em><br>contains special offer details, including coupon and Subscribe & Save discounts |[optional]|
**data_asin** | **StrictStr** | <em>unique product identifier on Amazon</em><br>note that there is no full list of possible values as the <code>data_asin</code> is a dynamic value assigned by Amazon<br>example:<br><code>B07G82D89J</code> |[optional]|
**rating** | **RatingElement** | <em>product rating info</em> |[optional]|
**is_amazon_choice** | **StrictBool** | <em>'Amazon's choice' label</em><br>if the value is <code>true</code>, the product is marked with the 'Amazon's choice' label |[optional]|
**is_best_seller** | **StrictBool** | <em>'Best Seller' label</em><br>if the value is <code>true</code>, the product is marked with the 'Best Seller' label |[optional]|
**delivery_info** | **AmazonDeliveryInfo** | <em>delivery information</em><br>delivery information including free and fast delivery date ranges |[optional]|
**labels** | **List[Optional[AmazonLabelElement]]** | <em>product labels</em><br>array containing an object with main Amazon labels’ information<br>if the product contains no labels, the value will be <code>null</code> |[optional]|
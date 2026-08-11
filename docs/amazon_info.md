# AmazonInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in Amazon SERP</em><br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | <em>the alignment of the element in Amazon SERP</em><br>can take the following values:<br><code>left</code>, <code>right</code> |[optional]|
**xpath** | **StrictStr** | <em>the <a href='https://en.wikipedia.org/wiki/XPath'>XPath</a> of the element</em> |[optional]|
**domain** | **StrictStr** | <em>Amazon domain</em> |[optional]|
**title** | **StrictStr** | <em>product title</em> |[optional]|
**url** | **StrictStr** | <em>URL of the product page</em> |[optional]|
**asin** | **StrictStr** | <em>ASIN in a POST array</em> |[optional]|
**image_url** | **StrictStr** | <em>URL of the product image featured in the results</em> |[optional]|
**price_from** | **StrictFloat** | <em>the regular price of a product</em><br>example:<br><code>49.98</code> |[optional]|
**price_to** | **StrictFloat** | <em>the upper limit of the product price range</em><br>example:<br><code>384.99</code> |[optional]|
**currency** | **StrictStr** | <em>currency in the <a href='https://en.wikipedia.org/wiki/ISO_4217'>ISO</a> format</em><br>example:<br><code>USD</code> |[optional]|
**special_offers** | **List[Optional[StrictStr]]** | <em>special offer details</em><br>contains special offer details, including coupon and Subscribe & Save discounts |[optional]|
**is_best_seller** | **StrictBool** | <em>'Best Seller' label</em><br>if the value is <code>true</code>, the product is marked with the 'Best Seller' label |[optional]|
**is_amazon_choice** | **StrictBool** | <em>'Amazon's choice' label</em><br>if the value is <code>true</code>, the product is marked with the 'Amazon's choice' label |[optional]|
**rating** | **RatingInfo** | <em>the item's rating </em><br>the popularity rate based on reviews and displayed in SERP |[optional]|
**delivery_info** | **AmazonDeliveryInfo** | <em>delivery information</em><br>delivery information including free and fast delivery date ranges |[optional]|
**bought_past_month** | **StrictInt** |  |[optional]|
# AmazonInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in Amazon SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | the alignment of the element in Amazon SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**domain** | **StrictStr** | Amazon domain |[optional]|
**title** | **StrictStr** | product title |[optional]|
**url** | **StrictStr** | URL of the product page |[optional]|
**asin** | **StrictStr** | ASIN of the product<br>learn more about ASIN in this help center guide |[optional]|
**image_url** | **StrictStr** | URL of the product image featured in the results |[optional]|
**price_from** | **StrictFloat** | the regular price of a product<br>example:<br>49.98 |[optional]|
**price_to** | **StrictFloat** | the upper limit of the product price range<br>example:<br>384.99 |[optional]|
**currency** | **StrictStr** | currency in the ISO format<br>example:<br>USD |[optional]|
**special_offers** | **List[Optional[StrictStr]]** | special offer details<br>contains special offer details, including coupon and Subscribe & Save discounts |[optional]|
**is_best_seller** | **StrictBool** | “Best Seller” label<br>if the value is true, the product is marked with the “Best Seller” label |[optional]|
**is_amazon_choice** | **StrictBool** | “Amazon’s choice” label<br>if the value is true, the product is marked with the “Amazon’s choice” label |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**delivery_info** | **AmazonDeliveryInfo** | delivery information<br>delivery information including free and fast delivery date ranges |[optional]|
**bought_past_month** | **StrictInt** |  |[optional]|
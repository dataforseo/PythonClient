# GoogleShoppingSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | <em>domain of the URL</em><br>domain of the URL where a special offer is posted<br><strong>Note:</strong> this field is deprecated and will return <code>null</code> |[optional]|
**title** | **StrictStr** | <em>title of the element</em> |[optional]|
**description** | **StrictStr** | <em>description of the product in Google Shopping SERP</em> |[optional]|
**url** | **StrictStr** | <em>URL pointing at special offer page</em><br>URL where a special offer is posted<br><strong>Note:</strong> this field is deprecated and will return <code>null</code> |[optional]|
**shopping_url** | **StrictStr** | <em>URL to the product page on Google Shopping</em> |[optional]|
**tags** | **List[Optional[StrictStr]]** | <em>tags assigned to the product</em> |[optional]|
**price** | **StrictFloat** | <em>product price</em><br>example:<br><code>384.99</code> |[optional]|
**price_multiplier** | **StrictInt** | <em>price multiplier for instalment plan</em><br>indicates the number of months covered by the monthly payment for the product |[optional]|
**old_price** | **StrictFloat** | <em>product old price</em><br>displayed if the product price has been changed<br>example:<br><code>499</code> |[optional]|
**currency** | **StrictStr** | <em>currency in the <a href='https://en.wikipedia.org/wiki/ISO_4217'>ISO</a> format</em><br>example:<br><code>USD</code> |[optional]|
**product_id** | **StrictStr** | <em>unique product identifier on Google Shopping</em><br>note that there is no full list of possible values as the <code>product_id</code> is a dynamic value assigned by Google<br>if there are no values, you will get <code>null</code><br>example:<br><code>4485466949985702538</code><br>learn more about the parameter in <a href='https://dataforseo.com/help-center/product-id-google-shopping' rel='noopener noreferrer' target='_blank'>this help center guide</a> |[optional]|
**data_docid** | **StrictStr** | <em>unique identifier of the SERP data element</em><br>note that there is no full list of possible values as the <code>data_docid</code> is a dynamic value assigned by Google<br>example:<br><code>17363035694596624076</code> |[optional]|
**seller** | **StrictStr** | <em>name of the seller</em><br>the name of the company that placed a corresponding product on Google Shopping |[optional]|
**additional_specifications** | **Dict[str, Optional[StrictStr]]** | <em>object containing additional url parameters</em><br>you can get more details about the product by using this object in the POST request to the <a href='/v3/merchant/google/products/task_post/?php' rel='noopener noreferrer' target='_blank'>Google Shopping Product Specification</a> and <a href='/v3/merchant/google/sellers/task_post/?php' rel='noopener noreferrer' target='_blank'>Google Shopping Sellers</a> endpoint |[optional]|
**reviews_count** | **StrictInt** | <em>number of product reviews</em><br>indicates the number of reviews left by users on Google Shopping<br>if there are no values, you will get <code>null</code> |[optional]|
**is_best_match** | **StrictBool** | <em>'best match' label</em><br>if the value is <code>true</code>, the product is marked with the 'best match' label<br>if there are no values, you will get <code>null</code> |[optional]|
**product_rating** | **RatingElement** | <em>product rating</em><br>the product popularity rate based on product reviews |[optional]|
**shop_rating** | **RatingElement** | <em>shop rating</em><br>the popularity rate of the seller based on user reviews |[optional]|
**product_images** | **List[Optional[StrictStr]]** | <em>URLs to the images of the product</em><br>the first URL in the array is the featured image of the product |[optional]|
**shop_ad_aclk** | **StrictStr** | <em>unique ad click referral parameter</em><br>using this parameter you can get a URL of the advertisement in <a href='/v3/merchant/google/sellers/ad_url/'>Google Shopping Sellers Ad URL</a> |[optional]|
**gid** | **StrictStr** | <em>global product identifier on Google Shopping</em><br>note that there is no full list of possible values as the <code>gid</code> is a dynamic value assigned by Google<br>if there are no values, you will get <code>null</code><br>example:<br><code>4702526954592161872</code><br>learn more about <code>gid</code> parameter in <a href='https://dataforseo.com/help-center/whats-a-gid-in-google-shopping-api' target='_blank'>this help center guide</a> |[optional]|
**delivery_info** | **DeliveryInfo** | <em>delivery information</em><br>delivery information including free and fast delivery date ranges |[optional]|
**stores_count_info** | **StoresCountInfo** | <em>stores count information</em><br>contains information about the number of stores that offer the same product |[optional]|
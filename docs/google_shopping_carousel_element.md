# GoogleShoppingCarouselElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**xpath** | **StrictStr** | <em><a href='https://en.wikipedia.org/wiki/XPath'>XPath</a> of the element</em> |[optional]|
**title** | **StrictStr** | <em>product title</em> |[optional]|
**tags** | **List[Optional[StrictStr]]** | <em>tags assigned to the product</em> |[optional]|
**seller** | **StrictStr** | <em>name of the seller</em><br>the name of the company that placed a corresponding product on Google Shopping |[optional]|
**price** | **StrictFloat** | <em>product price</em><br>example:<br><code>384.99</code> |[optional]|
**currency** | **StrictStr** | <em>currency in the <a href='https://en.wikipedia.org/wiki/ISO_4217'>ISO</a> format</em><br>example:<br><code>USD</code> |[optional]|
**product_rating** | **RatingElement** | <em>product rating</em><br>the product popularity rate based on product reviews |[optional]|
**product_images** | **List[Optional[StrictStr]]** | <em>URLs to the images of the product</em><br>the first URL in the array is the featured image of the product |[optional]|
**shopping_url** | **StrictStr** | <em>URL to the product page on Google Shopping</em> |[optional]|
**product_id** | **StrictStr** | <em>unique product identifier on Google Shopping</em><br>note that there is no full list of possible values as the <code>product_id</code> is a dynamic value assigned by Google<br>if there are no values, you will get <code>null</code><br>example:<br><code>4485466949985702538</code><br>learn more about the parameter in <a href='https://dataforseo.com/help-center/product-id-google-shopping' rel='noopener noreferrer' target='_blank'>this help center guide</a> |[optional]|
**data_docid** | **StrictStr** | <em>unique identifier of the SERP data element</em><br>note that there is no full list of possible values as the <code>data_docid</code> is a dynamic value assigned by Google<br>example:<br><code>17363035694596624076</code> |[optional]|
**gid** | **StrictStr** | <em>global product identifier on Google Shopping</em><br>note that there is no full list of possible values as the <code>gid</code> is a dynamic value assigned by Google<br>if there are no values, you will get <code>null</code><br>example:<br><code>4702526954592161872</code><br>learn more about <code>gid</code> parameter in <a href='https://dataforseo.com/help-center/whats-a-gid-in-google-shopping-api' target='_blank'>this help center guide</a> |[optional]|
**delivery_info** | **DeliveryInfo** | <em>delivery information</em><br>delivery information including free and fast delivery date ranges |[optional]|
**special_offer_info** | **SpecialOfferInfo** | <em>special offer from the seller</em><br>information on the special offer from the seller, including discount and coupon info |[optional]|
# GoogleShoppingSponsoredCarouselElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**xpath** | **StrictStr** | <em><a href='https://en.wikipedia.org/wiki/XPath'>XPath</a> of the element</em> |[optional]|
**title** | **StrictStr** | <em>title of the element</em> |[optional]|
**tags** | **List[Optional[StrictStr]]** | <em>tags assigned to the product</em> |[optional]|
**seller** | **StrictStr** | <em>name of the seller</em><br>the name of the company that placed a corresponding product on Google Shopping |[optional]|
**price** | **StrictFloat** | <em>product price</em><br>example:<br><code>384.99</code> |[optional]|
**currency** | **StrictStr** | <em>currency in the <a href='https://en.wikipedia.org/wiki/ISO_4217'>ISO</a> format</em><br>example:<br><code>USD</code> |[optional]|
**product_rating** | **RatingElement** | <em>product rating</em><br>the product popularity rate based on product reviews |[optional]|
**product_images** | **List[Optional[StrictStr]]** | <em>URLs to the images of the product</em><br>the first URL in the array is the featured image of the product |[optional]|
**shop_ad_aclk** | **StrictStr** | <em>unique ad click referral parameter</em><br>using this parameter you can get a URL of the advertisement in <a href='/v3/merchant/google/sellers/ad_url/'>Google Shopping Sellers Ad URL</a> |[optional]|
**delivery_info** | **DeliveryInfo** | <em>delivery information</em><br>delivery information including free and fast delivery date ranges |[optional]|
**special_offer_info** | **SpecialOfferInfo** | <em>special offer from the seller</em><br>information on the special offer from the seller, including discount and coupon info |[optional]|
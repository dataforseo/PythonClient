# GoogleShoppingSponsoredCarouselElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**xpath** | **StrictStr** | XPath of the element |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**tags** | **List[Optional[StrictStr]]** | tags assigned to the product |[optional]|
**seller** | **StrictStr** | name of the sellerthe name of the company that placed a corresponding product on Google Shopping |[optional]|
**price** | **StrictFloat** | product priceexample:384.99 |[optional]|
**currency** | **StrictStr** | currency in the ISO formatexample:USD |[optional]|
**product_rating** | **RatingElement** | product ratingthe product popularity rate based on product reviews |[optional]|
**product_images** | **List[Optional[StrictStr]]** | URLs to the images of the productthe first URL in the array is the featured image of the product |[optional]|
**shop_ad_aclk** | **StrictStr** | unique ad click referral parameterusing this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL |[optional]|
**delivery_info** | **DeliveryInfo** | delivery informationdelivery information including free and fast delivery date ranges |[optional]|
**special_offer_info** | **SpecialOfferInfo** | special offer from the sellerinformation on the special offer from the seller, including discount and coupon info |[optional]|
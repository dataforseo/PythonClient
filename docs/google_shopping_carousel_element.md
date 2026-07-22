# GoogleShoppingCarouselElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**xpath** | **StrictStr** | XPath of the element |[optional]|
**title** | **StrictStr** | product title |[optional]|
**tags** | **List[Optional[StrictStr]]** | tags assigned to the product |[optional]|
**seller** | **StrictStr** | name of the sellerthe name of the company that placed a corresponding product on Google Shopping |[optional]|
**price** | **StrictFloat** | product priceexample:384.99 |[optional]|
**currency** | **StrictStr** | currency in the ISO formatexample:USD |[optional]|
**product_rating** | **RatingElement** | product ratingthe product popularity rate based on product reviews |[optional]|
**product_images** | **List[Optional[StrictStr]]** | URLs to the images of the productthe first URL in the array is the featured image of the product |[optional]|
**shopping_url** | **StrictStr** | URL to the product page on Google Shopping |[optional]|
**product_id** | **StrictStr** | unique product identifier on Google Shoppingnote that there is no full list of possible values as the product_id is a dynamic value assigned by Googleif there are no values, you will get nullexample:4485466949985702538learn more about the parameter in this help center guide |[optional]|
**data_docid** | **StrictStr** | unique identifier of the SERP data elementnote that there is no full list of possible values as the data_docid is a dynamic value assigned by Googleexample:17363035694596624076 |[optional]|
**gid** | **StrictStr** | global product identifier on Google Shoppingnote that there is no full list of possible values as the gid is a dynamic value assigned by Googleif there are no values, you will get nullexample:4702526954592161872learn more about gid parameter in this help center guide |[optional]|
**delivery_info** | **DeliveryInfo** | delivery informationdelivery information including free and fast delivery date ranges |[optional]|
**special_offer_info** | **SpecialOfferInfo** | special offer from the sellerinformation on the special offer from the seller, including discount and coupon info |[optional]|
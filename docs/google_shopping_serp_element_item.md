# GoogleShoppingSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | domain of the URLdomain of the URL where a special offer is postedNote: this field is deprecated and will return null |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**description** | **StrictStr** | description of the product in Google Shopping SERP |[optional]|
**url** | **StrictStr** | URL pointing at special offer pageURL where a special offer is postedNote: this field is deprecated and will return null |[optional]|
**shopping_url** | **StrictStr** | URL to the product page on Google Shopping |[optional]|
**tags** | **List[Optional[StrictStr]]** | tags assigned to the product |[optional]|
**price** | **StrictFloat** | product priceexample:384.99 |[optional]|
**price_multiplier** | **StrictInt** | price multiplier for instalment planindicates the number of months covered by the monthly payment for the product |[optional]|
**old_price** | **StrictFloat** | product old pricedisplayed if the product price has been changedexample:499 |[optional]|
**currency** | **StrictStr** | currency in the ISO formatexample:USD |[optional]|
**product_id** | **StrictStr** | unique product identifier on Google Shoppingnote that there is no full list of possible values as the product_id is a dynamic value assigned by Googleif there are no values, you will get nullexample:4485466949985702538learn more about the parameter in this help center guide |[optional]|
**data_docid** | **StrictStr** | unique identifier of the SERP data elementnote that there is no full list of possible values as the data_docid is a dynamic value assigned by Googleexample:17363035694596624076 |[optional]|
**seller** | **StrictStr** | name of the sellerthe name of the company that placed a corresponding product on Google Shopping |[optional]|
**additional_specifications** | **Dict[str, Optional[StrictStr]]** | object containing additional url parametersyou can get more details about the product by using this object in the POST request to the Google Shopping Product Specification and Google Shopping Sellers endpoint |[optional]|
**reviews_count** | **StrictInt** | number of product reviewsindicates the number of reviews left by users on Google Shoppingif there are no values, you will get null |[optional]|
**is_best_match** | **StrictBool** | 'best match' labelif the value is true, the product is marked with the 'best match' labelif there are no values, you will get null |[optional]|
**product_rating** | **RatingElement** | product ratingthe product popularity rate based on product reviews |[optional]|
**shop_rating** | **RatingElement** | shop ratingthe popularity rate of the seller based on user reviews |[optional]|
**product_images** | **List[Optional[StrictStr]]** | URLs to the images of the productthe first URL in the array is the featured image of the product |[optional]|
**shop_ad_aclk** | **StrictStr** | unique ad click referral parameterusing this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL |[optional]|
**gid** | **StrictStr** | global product identifier on Google Shoppingnote that there is no full list of possible values as the gid is a dynamic value assigned by Googleif there are no values, you will get nullexample:4702526954592161872learn more about gid parameter in this help center guide |[optional]|
**delivery_info** | **DeliveryInfo** | delivery informationdelivery information including free and fast delivery date ranges |[optional]|
**stores_count_info** | **StoresCountInfo** | stores count informationcontains information about the number of stores that offer the same product |[optional]|
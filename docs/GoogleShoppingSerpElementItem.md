# GoogleShoppingSerpElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **string** | domain of the URL<br>domain of the URL where a special offer is posted |[optional]|
**title** | **string** | title of the element |[optional]|
**description** | **string** | description of the product in Google Shopping SERP |[optional]|
**url** | **string** | URL pointing at special offer page<br>URL where a special offer is posted |[optional]|
**shopping_url** | **string** | URL to the product page on Google Shopping |[optional]|
**tags** | **string[]** | tags assigned to the product |[optional]|
**price** | **number** | product price<br>example:<br>384.99 |[optional]|
**price_multiplier** | **number** | price multiplier for instalment plan<br>indicates the number of months covered by the monthly payment for the product |[optional]|
**old_price** | **number** | product old price<br>displayed if the product price has been changed<br>example:<br>499 |[optional]|
**currency** | **string** | currency in the ISO format<br>example:<br>USD |[optional]|
**product_id** | **string** | unique product identifier on Google Shopping<br>note that there is no full list of possible values as the product_id is a dynamic value assigned by Google<br>if there are no values, you will get null<br>example:<br>4485466949985702538<br>learn more about the parameter in this help center guide |[optional]|
**data_docid** | **string** | unique identifier of the SERP data element<br>note that there is no full list of possible values as the data_docid is a dynamic value assigned by Google<br>example:<br>17363035694596624076 |[optional]|
**seller** | **string** | name of the seller<br>the name of the company that placed a corresponding product on Google Shopping |[optional]|
**additional_specifications** | **{ [key: string]: string; }** | object containing additional url parameters<br>you can get more details about the product by using this object in the POST request to the Google Shopping Product Specification and Google Shopping Sellers endpoint |[optional]|
**reviews_count** | **number** | number of product reviews<br>indicates the number of reviews left by users on Google Shopping<br>if there are no values, you will get null |[optional]|
**is_best_match** | **boolean** | “best match” label<br>if the value is true, the product is marked with the “best match” label<br>if there are no values, you will get null |[optional]|
**product_rating** | **RatingElement** | product rating<br>the product popularity rate based on product reviews |[optional]|
**shop_rating** | **RatingElement** | shop rating<br>the popularity rate of the seller based on user reviews |[optional]|
**product_images** | **string[]** | URLs to the images of the product<br>the first URL in the array is the featured image of the product |[optional]|
**shop_ad_aclk** | **string** | unique ad click referral parameter<br>using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL |[optional]|
**gid** | **string** | global product identifier on Google Shopping<br>note that there is no full list of possible values as the gid is a dynamic value assigned by Google<br>if there are no values, you will get null<br>example:<br>4702526954592161872<br>learn more about gid parameter in this help center guide |[optional]|
**delivery_info** | **DeliveryInfo** | delivery information<br>delivery information including free and fast delivery date ranges |[optional]|
**stores_count_info** | **StoresCountInfo** | stores count information<br>contains information about the number of stores that offer the same product |[optional]|
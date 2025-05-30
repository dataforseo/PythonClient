# MerchantAmazonSellersTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**asin** | **StrictStr** | asin received in a POST array<br>learn more about ASINs in this help center guide |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain received in a POST array |[optional]|
**location_code** | **StrictFloat** | location code received in a POST array |[optional]|
**language_code** | **StrictStr** | language code received in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to Amazon results<br>you can use it to make sure the provided results are accurate |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**title** | **StrictStr** | product title<br>title of the product relevant to the asin received in a POST array |[optional]|
**image** | **StrictStr** | product image url<br>image URL of the product relevant to the asin received in a POST array |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results found in Amazon Sellers SERP<br>contains types of all search results (items) found in the returned SERP<br>possible item types:<br>amazon_seller_main_item, amazon_seller_item |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseAmazonSerpElementItem]]** | items in SERP |[optional]|
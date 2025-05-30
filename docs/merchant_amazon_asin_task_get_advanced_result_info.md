# MerchantAmazonAsinTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**asin** | **StrictStr** | ASIN received in a POST array<br>the unique product identifier in Amazon (ASIN) received in a POST array<br>learn more about the identified in this help center guide |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | Amazon domain in a POST array |[optional]|
**location_code** | **StrictFloat** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to Amazon results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results found on Amazon<br>contains types of all search results (items) found in the returned SERP<br>possible item types:<br>amazon_product_info |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseAmazonSerpElementItem]]** | Amazon product info items |[optional]|
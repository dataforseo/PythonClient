# MerchantGoogleSellersTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**product_id** | **StrictStr** | product_id received in a POST array<br>learn more about the parameter in this help center guide |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to Google Shopping results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**title** | **StrictStr** | title of the product |[optional]|
**url** | **StrictStr** | URL to the product page |[optional]|
**image_url** | **StrictStr** | URL to the product image |[optional]|
**rating** | **RatingInfo** | product rating<br>the product popularity rate based on product reviews |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results found in Google Shopping SERP<br>contains types of all search results (items) found in the returned SERP<br>possible item types:<br>shops_list, buy_on_google |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseMerchantGoogleShoppingSellersElementItem]]** | items in SERP |[optional]|
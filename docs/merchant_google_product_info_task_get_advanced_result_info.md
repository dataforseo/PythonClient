# MerchantGoogleProductInfoTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**product_id** | **StrictStr** | product ID in a POST array<br>learn more about the parameter in this help center guide |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictFloat** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the format: “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of items found on the product specification page<br>possible item types:<br>product_info_element |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseMerchantSerpElementItem]]** | items on the product page<br>contains all product attributes and related data listed on the product page |[optional]|
# MerchantGoogleProductSpecTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**product_id** | **StrictStr** | product ID in a POST array<br>learn more about the parameter in this help center guide |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**title** | **StrictStr** | title of the product |[optional]|
**description** | **StrictStr** | description of the product |[optional]|
**image_url** | **StrictStr** | URL of the product image |[optional]|
**tags** | **List[Optional[StrictStr]]** | tags of the product |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the format: “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of items found on the product specification page<br>possible item types:<br>shopping_specification |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[ShoppingSpecification]]** | items on the product specification page<br>contains all product attributes and related data listed on the product specification page |[optional]|
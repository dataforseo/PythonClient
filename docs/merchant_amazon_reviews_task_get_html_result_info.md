# MerchantAmazonReviewsTaskGetHtmlResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**product_id** | **StrictStr** | ASIN received in a POST array |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[SerpHtmlItemInfo]]** | HTML pages and related data |[optional]|
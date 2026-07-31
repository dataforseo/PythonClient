# AppDataAppleAppInfoTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**app_id** | **StrictStr** | <em>application id received in a POST request</em> |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**se_results_count** | **StrictInt** | <em>the total number of results</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of items in the results array</em> |[optional]|
**items** | **List[Optional[AppStoreInfoOrganic]]** | <em>found app info</em> |[optional]|
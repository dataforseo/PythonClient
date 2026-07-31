# BusinessDataTripadvisorSearchTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array</em><br>this field will contain the <code>alias</code> parameter if it was specified in a POST array |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to Tripadvisor results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>item types encountered in the result</em><br>possible item types: <code>tripadvisor_search_organic</code> |[optional]|
**se_results_count** | **StrictInt** | <em>the total number of results</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of items in the results array</em><br>you can get more results by using the <code>depth</code> parameter when setting a task |[optional]|
**items** | **List[Optional[TripadvisorSearchOrganic]]** | <em>Tripadvisor search listing results</em><br>you can get more results by using the <code>depth</code> parameter when setting a task |[optional]|
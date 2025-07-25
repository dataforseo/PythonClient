# BusinessDataTripadvisorSearchTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword received in a POST array<br>this field will contain the alias parameter if it was specified in a POST array |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to Tripadvisor results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**item_types** | **List[Optional[StrictStr]]** | item types encountered in the result<br>possible item types: tripadvisor_search_organic |[optional]|
**se_results_count** | **StrictInt** | the total number of results |[optional]|
**items_count** | **StrictInt** | the number of items in the results array<br>you can get more results by using the depth parameter when setting a task |[optional]|
**items** | **List[Optional[TripadvisorSearchOrganic]]** | Tripadvisor search listing results<br>you can get more results by using the depth parameter when setting a task |[optional]|
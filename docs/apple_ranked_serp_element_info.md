# AppleRankedSerpElementInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**serp_item** | **AppStoreSearchOrganic** | contains data on the SERP element<br>the list of supported SERP elements can be found below |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**se_results_count** | **StrictInt** | number of search results for the returned keyword |[optional]|
**last_updated_time** | **StrictStr** | date and time when SERP data was updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**previous_updated_time** | **StrictStr** | previous to the most recent date and time when SERP data was updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-10-15 12:57:46 +00:00;<br>in this case, will equal null |[optional]|
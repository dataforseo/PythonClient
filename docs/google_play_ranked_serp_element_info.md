# GooglePlayRankedSerpElementInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**serp_item** | **GooglePlaySearchOrganic** | <em>contains data on the SERP element</em><br>the list of supported SERP elements can be found below |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**se_results_count** | **StrictInt** | <em>number of search results for the returned keyword</em> |[optional]|
**last_updated_time** | **StrictStr** | <em>date and time when keyword data was updated</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**previous_updated_time** | **StrictStr** | <em>previous to the most recent date and time when SERP data was updated</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-10-15 12:57:46 +00:00</code>;<br>in this case, will equal null |[optional]|
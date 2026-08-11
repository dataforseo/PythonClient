# AmazonRankedSerpElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**serp_item** | **AmazonInfo** | <em>contains data on the SERP element</em><br>the list of supported SERP elements can be found below |[optional]|
**check_url** | **StrictStr** | <em>direct URL to Amazon results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**serp_item_types** | **List[Optional[StrictStr]]** | <em>direct URL to Amazon results</em><br>contains types of all search results (<code>items</code>) found in the returned SERP;<br>possible item types:<br><code>amazon_serp</code>, <code>amazon_paid</code>, <code>editorial_recommendations</code>, <code>top_rated_from_our_brands</code>, <code>related_searches</code> |[optional]|
**se_results_count** | **StrictInt** | <em>total number of results in Amazon SERP</em> |[optional]|
**last_updated_time** | **StrictStr** | <em>date and time when keyword data was updated</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**previous_updated_time** | **StrictStr** | <em>previous to the most recent update of SERP data</em><br>in the <a href='https://en.wikipedia.org/wiki/ISO_8601'>ISO 860</a>1 format: “YYYY-MM-DDThh:mm:ss.sssssssZ”<br>example:<br><code class='long-string'>2020-09-12T00:07:43.0733218Z</code> |[optional]|
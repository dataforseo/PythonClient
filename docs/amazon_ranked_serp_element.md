# AmazonRankedSerpElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**serp_item** | **BaseAmazonSerpElementItem** | contains data on the SERP element<br>the list of supported SERP elements can be found below |[optional]|
**check_url** | **StrictStr** | direct URL to Amazon results<br>you can use it to make sure that we provided accurate results |[optional]|
**serp_item_types** | **List[Optional[StrictStr]]** | direct URL to Amazon results<br>contains types of all search results (items) found in the returned SERP;<br>possible item types:<br>amazon_serp, amazon_paid, editorial_recommendations, top_rated_from_our_brands, related_searches |[optional]|
**se_results_count** | **StrictFloat** | total number of results in Amazon SERP |[optional]|
**last_updated_time** | **StrictStr** | date and time when SERP data was last updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**previous_updated_time** | **StrictStr** | previous to the most recent update of SERP data<br>in the ISO 8601 format: “YYYY-MM-DDThh:mm:ss.sssssssZ”<br>example:<br>2020-09-12T00:07:43.0733218Z |[optional]|
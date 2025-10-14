# RankedSerpElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**serp_item** | **BaseDataforseoLabsApiElementItem** | contains data on the SERP element<br>the list of supported SERP elements can be found below |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**serp_item_types** | **List[Optional[StrictStr]]** | types of search results in SERP<br>contains types of search results (items) found in SERP<br>all possible item types can be found here, they include:<br>answer_box, app, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, images, jobs, knowledge_graph, local_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, mention_carousel, recipes, top_sights, scholarly_articles, popular_products, podcasts, questions_and_answers, find_results_on, stocks_box;<br>note that the actual results will be returned only for organic, paid, featured_snippet, local_pack, and ai_overview_reference elements |[optional]|
**se_results_count** | **StrictInt** | number of search results for the returned keyword |[optional]|
**keyword_difficulty** | **StrictInt** | difficulty of ranking in the first top-10 organic results for a keyword<br>indicates the chance of getting in top-10 organic results for a keyword on a logarithmic scale from 0 to 100;<br>calculated by analysing, among other parameters, link profiles of the first 10 pages in SERP;<br>learn more about the metric in this help center guide |[optional]|
**is_lost** | **StrictBool** | lost ranked elements<br>indicates how many ranked elements of this target were previously presented in SERPs, but weren’t found during the last check |[optional]|
**last_updated_time** | **StrictStr** | date and time when SERP data was updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**previous_updated_time** | **StrictStr** | previous to the most recent date and time when SERP data was updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-10-15 12:57:46 +00:00 |[optional]|
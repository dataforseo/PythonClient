# SerpInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**serp_item_types** | **List[Optional[StrictStr]]** | types of search results in SERP<br>contains types of search results (items) found in SERP<br>possible item types:<br>answer_box, app, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, images, jobs, knowledge_graph, local_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, mention_carousel, recipes, top_sights, scholarly_articles, popular_products, podcasts, questions_and_answers, find_results_on, stocks_box;<br>note that the actual results will be returned only for organic, paid, featured_snippet, and local_pack elements |[optional]|
**se_results_count** | **StrictInt** | number of search results for the returned keyword |[optional]|
**last_updated_time** | **StrictStr** | date and time when search intent data was last updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**previous_updated_time** | **StrictStr** | previous to the most recent date and time when SERP data was updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-10-15 12:57:46 +00:00 |[optional]|
# DataforseoLabsGoogleHistoricalSerpsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**keyword** | **StrictStr** | keyword obtained as a result of search engine autocorrection<br>the results will be provided for the corrected keyword |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engine<br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results in SERP<br>contains types of search results (items) found in SERP.<br>possible item types:<br>answer_box, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, google_posts, images, jobs, knowledge_graph, local_pack, hotels_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, mention_carousel, recipes, top_sights, scholarly_articles, popular_products, podcasts, questions_and_answers, find_results_on, stocks_box, visual_stories, commercial_units,  local_services, google_hotels, math_solver |[optional]|
**se_results_count** | **StrictInt** | total number of results in SERP |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseDataforseoLabsApiElementItem]]** | additional items present in the element<br>if there are none, equals null |[optional]|
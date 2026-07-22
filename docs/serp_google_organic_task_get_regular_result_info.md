# SerpGoogleOrganicTaskGetRegularResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword received in a POST arraykeyword is returned with decoded %## (plus symbol '+' will be decoded to a space character) |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine resultsyou can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was receivedin the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”example:2019-11-15 12:57:46 +00:00 |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engineif the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection;if there is none, the value is null |[optional]|
**refinement_chips** | **RefinementChipsInfo** | search refinement chipsif there are none, the value is null |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results found in SERPcontains types of all search results (items) found in the returned SERPpossible item types:answer_box, app, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, third_party_reviews,  images, jobs, knowledge_graph, local_pack, hotels_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, recipes, top_sights, scholarly_articles, popular_products, questions_and_answers, find_results_on, stocks_box, commercial_units, local_services, google_hotels, math_solver, currency_box, product_considerations, short_videos, refine_products, perspectives, discussions_and_forums, compare_sites, ai_overviewnote that this array contains all types of search results found in the returned SERP;however, this endpoint provides data for featured_snippet, organic and paid types only;to get all items (including SERP features and rich snippets) found in the returned SERP, please refer to the Google Organiс Advanced SERP endpoint |[optional]|
**se_results_count** | **StrictInt** | total number of results in SERP |[optional]|
**pages_count** | **StrictInt** | total search results pages retrievedtotal number of retrieved SERPs in the result |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseSerpApiElementItem]]** | items in SERP |[optional]|
# SerpBingOrganicTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword received in a POST array<br>the keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engine<br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**refinement_chips** | **RefinementChipsInfo** | search refinement chips<br>equals null |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results in SERP<br>contains types of search results (items) found in SERP.<br>possible item types:<br>answer_box, carousel, events, featured_snippet, hotels_pack, images, jobs, local_pack, map, organic, paid, people_also_ask, people_also_search, questions_and_answers,recipes, related_searches, shopping, top_stories, video, ai_overview |[optional]|
**se_results_count** | **StrictInt** | total number of results in SERP |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseSerpApiElementItem]]** | contains results featured in the ‘hotels_pack’ element of SERP |[optional]|
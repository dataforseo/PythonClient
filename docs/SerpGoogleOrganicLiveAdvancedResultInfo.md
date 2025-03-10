# SerpGoogleOrganicLiveAdvancedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array the keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**spell** | [**SpellInfo**](SpellInfo.md) |  | [optional] 
**refinement_chips** | [**RefinementChipsInfo**](RefinementChipsInfo.md) |  | [optional] 
**item_types** | **List[Optional[str]]** | types of search results in SERP contains types of search results (items) found in SERP. possible item types: answer_box, app, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, third_party_reviews, google_posts, images, jobs, knowledge_graph, local_pack, hotels_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, mention_carousel, recipes, top_sights, scholarly_articles, popular_products, podcasts, questions_and_answers, find_results_on, stocks_box, visual_stories, commercial_units, local_services, google_hotels, math_solver, currency_box, product_considerations, found_on_web, short_videos, refine_products, explore_brands, perspectives, discussions_and_forums, compare_sites, courses, ai_overview | [optional] 
**se_results_count** | **int** | total number of results in SERP | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BaseSerpElementItem]**](BaseSerpElementItem.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_organic_live_advanced_result_info import SerpGoogleOrganicLiveAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleOrganicLiveAdvancedResultInfo from a JSON string
serp_google_organic_live_advanced_result_info_instance = SerpGoogleOrganicLiveAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleOrganicLiveAdvancedResultInfo.to_json())

# convert the object into a dict
serp_google_organic_live_advanced_result_info_dict = serp_google_organic_live_advanced_result_info_instance.to_dict()
# create an instance of SerpGoogleOrganicLiveAdvancedResultInfo from a dict
serp_google_organic_live_advanced_result_info_from_dict = SerpGoogleOrganicLiveAdvancedResultInfo.from_dict(serp_google_organic_live_advanced_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



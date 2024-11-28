# RankedSerpElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**serp_item** | [**BaseDataforseoLabsSerpElementItem**](BaseDataforseoLabsSerpElementItem.md) |  | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**serp_item_types** | **List[Optional[str]]** | types of search results in SERP contains types of search results (items) found in SERP possible item types: answer_box, app, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, images, jobs, knowledge_graph, local_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, mention_carousel, recipes, top_sights, scholarly_articles, popular_products, podcasts, questions_and_answers, find_results_on, stocks_box; note that the actual results will be returned only for organic, paid, featured_snippet, and local_pack elements | [optional] 
**se_results_count** | **str** | number of search results for the returned keyword | [optional] 
**keyword_difficulty** | **int** | difficulty of ranking in the first top-10 organic results for a keyword indicates the chance of getting in top-10 organic results for a keyword on a logarithmic scale from 0 to 100; calculated by analysing, among other parameters, link profiles of the first 10 pages in SERP; learn more about the metric in this help center guide | [optional] 
**is_lost** | **bool** | lost ranked elements indicates how many ranked elements of this domain were previously presented in SERPs, but weren’t found during the last check | [optional] 
**last_updated_time** | **str** | date and time when search intent data was last updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**previous_updated_time** | **str** | previous to the most recent date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-10-15 12:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.ranked_serp_element import RankedSerpElement

# TODO update the JSON string below
json = "{}"
# create an instance of RankedSerpElement from a JSON string
ranked_serp_element_instance = RankedSerpElement.from_json(json)
# print the JSON string representation of the object
print(RankedSerpElement.to_json())

# convert the object into a dict
ranked_serp_element_dict = ranked_serp_element_instance.to_dict()
# create an instance of RankedSerpElement from a dict
ranked_serp_element_from_dict = RankedSerpElement.from_dict(ranked_serp_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



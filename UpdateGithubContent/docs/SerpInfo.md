# SerpInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**serp_item_types** | **List[Optional[str]]** | types of search results in SERP contains types of search results (items) found in SERP possible item types: answer_box, app, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, images, jobs, knowledge_graph, local_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, mention_carousel, recipes, top_sights, scholarly_articles, popular_products, podcasts, questions_and_answers, find_results_on, stocks_box; note that the actual results will be returned only for organic, paid, featured_snippet, and local_pack elements | [optional] 
**se_results_count** | **str** | number of search results for the returned keyword | [optional] 
**last_updated_time** | **str** | date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**previous_updated_time** | **str** | previous to the most recent date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-10-15 12:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.serp_info import SerpInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpInfo from a JSON string
serp_info_instance = SerpInfo.from_json(json)
# print the JSON string representation of the object
print SerpInfo.to_json()

# convert the object into a dict
serp_info_dict = serp_info_instance.to_dict()
# create an instance of SerpInfo from a dict
serp_info_form_dict = serp_info.from_dict(serp_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



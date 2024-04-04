# DataforseoLabsGoogleHistoricalSerpsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword** | **str** | keyword obtained as a result of search engine autocorrection the results will be provided for the corrected keyword | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**spell** | [**SpellInfo**](SpellInfo.md) |  | [optional] 
**item_types** | **List[Optional[str]]** | types of search results in SERP contains types of search results (items) found in SERP. possible item types: answer_box, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, google_posts, images, jobs, knowledge_graph, local_pack, hotels_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, mention_carousel, recipes, top_sights, scholarly_articles, popular_products, podcasts, questions_and_answers, find_results_on, stocks_box, visual_stories, commercial_units,  local_services, google_hotels, math_solver | [optional] 
**se_results_count** | **int** | total number of results in SERP | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BaseDataforseoLabsSerpElementItem]**](BaseDataforseoLabsSerpElementItem.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_historical_serps_live_item import DataforseoLabsGoogleHistoricalSerpsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleHistoricalSerpsLiveItem from a JSON string
dataforseo_labs_google_historical_serps_live_item_instance = DataforseoLabsGoogleHistoricalSerpsLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleHistoricalSerpsLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_google_historical_serps_live_item_dict = dataforseo_labs_google_historical_serps_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleHistoricalSerpsLiveItem from a dict
dataforseo_labs_google_historical_serps_live_item_form_dict = dataforseo_labs_google_historical_serps_live_item.from_dict(dataforseo_labs_google_historical_serps_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



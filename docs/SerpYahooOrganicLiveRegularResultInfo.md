# SerpYahooOrganicLiveRegularResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results You can use it to make sure that we provided exact results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**spell** | [**SpellInfo**](SpellInfo.md) |  | [optional] 
**refinement_chips** | [**RefinementChipsInfo**](RefinementChipsInfo.md) |  | [optional] 
**item_types** | **List[Optional[str]]** | types of search results found in SERP contains types of all search results (items) found in the returned SERP possible item types: featured_snippet, images, local_pack, hotels_pack, organic, paid, people_also_ask, related_searches, shopping, recipes, top_stories, video; note that this array contains all types of search results found in the returned SERP; however, this endpoint provides data for organic, paid, and featured_snippet types only; to get all items (including SERP features and rich snippets) found in the returned SERP, please refer to the Yahoo Organiс Advanced SERP endpoint | [optional] 
**se_results_count** | **int** | total number of results in SERP | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BaseSerpElementItem]**](BaseSerpElementItem.md) | items in SERP | [optional] 

## Example

```python
from dataforseo_client.models.serp_yahoo_organic_live_regular_result_info import SerpYahooOrganicLiveRegularResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpYahooOrganicLiveRegularResultInfo from a JSON string
serp_yahoo_organic_live_regular_result_info_instance = SerpYahooOrganicLiveRegularResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpYahooOrganicLiveRegularResultInfo.to_json())

# convert the object into a dict
serp_yahoo_organic_live_regular_result_info_dict = serp_yahoo_organic_live_regular_result_info_instance.to_dict()
# create an instance of SerpYahooOrganicLiveRegularResultInfo from a dict
serp_yahoo_organic_live_regular_result_info_from_dict = SerpYahooOrganicLiveRegularResultInfo.from_dict(serp_yahoo_organic_live_regular_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



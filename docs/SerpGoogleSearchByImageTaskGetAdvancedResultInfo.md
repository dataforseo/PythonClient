# SerpGoogleSearchByImageTaskGetAdvancedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | URL specified in a POST array | [optional] 
**keyword** | **str** | keyword Google associated with the specified image | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**spell** | [**SpellInfo**](SpellInfo.md) |  | [optional] 
**refinement_chips** | [**RefinementChipsInfo**](RefinementChipsInfo.md) |  | [optional] 
**item_types** | **List[Optional[str]]** | types of search results in SERP contains types of search results (items) found in SERP. possible item types: organic, images | [optional] 
**se_results_count** | **int** | total number of results in SERP | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BaseSerpElementItem]**](BaseSerpElementItem.md) | items featured in the faq_box | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_search_by_image_task_get_advanced_result_info import SerpGoogleSearchByImageTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleSearchByImageTaskGetAdvancedResultInfo from a JSON string
serp_google_search_by_image_task_get_advanced_result_info_instance = SerpGoogleSearchByImageTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleSearchByImageTaskGetAdvancedResultInfo.to_json())

# convert the object into a dict
serp_google_search_by_image_task_get_advanced_result_info_dict = serp_google_search_by_image_task_get_advanced_result_info_instance.to_dict()
# create an instance of SerpGoogleSearchByImageTaskGetAdvancedResultInfo from a dict
serp_google_search_by_image_task_get_advanced_result_info_from_dict = SerpGoogleSearchByImageTaskGetAdvancedResultInfo.from_dict(serp_google_search_by_image_task_get_advanced_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



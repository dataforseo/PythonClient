# SerpBaiduOrganicTaskGetAdvancedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array the keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**spell** | [**SpellInfo**](SpellInfo.md) |  | [optional] 
**refinement_chips** | [**RefinementChipsInfo**](RefinementChipsInfo.md) |  | [optional] 
**item_types** | **List[Optional[str]]** | types of search results in SERP contains types of search results (items) found in SERP. possible item types: images, local_pack, map, organic, paid, related_searches, video, stocks_box, dictionary, shopping | [optional] 
**se_results_count** | **int** | total number of results in SERP | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BaseSerpElementItem]**](BaseSerpElementItem.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.serp_baidu_organic_task_get_advanced_result_info import SerpBaiduOrganicTaskGetAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpBaiduOrganicTaskGetAdvancedResultInfo from a JSON string
serp_baidu_organic_task_get_advanced_result_info_instance = SerpBaiduOrganicTaskGetAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpBaiduOrganicTaskGetAdvancedResultInfo.to_json())

# convert the object into a dict
serp_baidu_organic_task_get_advanced_result_info_dict = serp_baidu_organic_task_get_advanced_result_info_instance.to_dict()
# create an instance of SerpBaiduOrganicTaskGetAdvancedResultInfo from a dict
serp_baidu_organic_task_get_advanced_result_info_from_dict = SerpBaiduOrganicTaskGetAdvancedResultInfo.from_dict(serp_baidu_organic_task_get_advanced_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SerpGoogleEventsLiveAdvancedResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in this case, the value will be null | [optional] 
**check_url** | **str** | direct URL to search engine results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**spell** | [**SpellInfo**](SpellInfo.md) |  | [optional] 
**item_types** | **List[Optional[str]]** | types of search results found in SERP possible item types: event_item | [optional] 
**se_results_count** | **int** | total number of results in SERP in this case, the value will be 0 this search engine does not indicate the total number of results | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BaseSerpElementItem]**](BaseSerpElementItem.md) | items in SERP | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_events_live_advanced_result_info import SerpGoogleEventsLiveAdvancedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleEventsLiveAdvancedResultInfo from a JSON string
serp_google_events_live_advanced_result_info_instance = SerpGoogleEventsLiveAdvancedResultInfo.from_json(json)
# print the JSON string representation of the object
print SerpGoogleEventsLiveAdvancedResultInfo.to_json()

# convert the object into a dict
serp_google_events_live_advanced_result_info_dict = serp_google_events_live_advanced_result_info_instance.to_dict()
# create an instance of SerpGoogleEventsLiveAdvancedResultInfo from a dict
serp_google_events_live_advanced_result_info_form_dict = serp_google_events_live_advanced_result_info.from_dict(serp_google_events_live_advanced_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



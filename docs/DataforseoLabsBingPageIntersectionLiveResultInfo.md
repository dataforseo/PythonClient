# DataforseoLabsBingPageIntersectionLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type search engine type specified in a POST request; for this endpoint, the field equals bing | [optional] 
**pages** | **Dict[str, Optional[str]]** | URLs you specified a POST array | [optional] 
**exclude_pages** | **List[Optional[str]]** | URLs you specified in a POST array that will be excluded from the results | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoLabsPageIntersectionLiveItem]**](DataforseoLabsPageIntersectionLiveItem.md) | contains keywords, relevant SERP elements and related data | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_page_intersection_live_result_info import DataforseoLabsBingPageIntersectionLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingPageIntersectionLiveResultInfo from a JSON string
dataforseo_labs_bing_page_intersection_live_result_info_instance = DataforseoLabsBingPageIntersectionLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBingPageIntersectionLiveResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_bing_page_intersection_live_result_info_dict = dataforseo_labs_bing_page_intersection_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsBingPageIntersectionLiveResultInfo from a dict
dataforseo_labs_bing_page_intersection_live_result_info_form_dict = dataforseo_labs_bing_page_intersection_live_result_info.from_dict(dataforseo_labs_bing_page_intersection_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



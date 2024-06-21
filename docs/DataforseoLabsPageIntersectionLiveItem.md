# DataforseoLabsPageIntersectionLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword_data** | [**KeywordDataKeywordDataInfo**](KeywordDataKeywordDataInfo.md) |  | [optional] 
**intersection_result** | [**Dict[str, BaseDataforseoLabsSerpElementItem]**](BaseDataforseoLabsSerpElementItem.md) | contains data on the SERP elements found for the returned keyword data will be provided in separate arrays for each URL you specified in the pages object when setting a task; depending on the number of specified URLs, it can contain from 1 to 20 arrays named respectively | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_page_intersection_live_item import DataforseoLabsPageIntersectionLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsPageIntersectionLiveItem from a JSON string
dataforseo_labs_page_intersection_live_item_instance = DataforseoLabsPageIntersectionLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsPageIntersectionLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_page_intersection_live_item_dict = dataforseo_labs_page_intersection_live_item_instance.to_dict()
# create an instance of DataforseoLabsPageIntersectionLiveItem from a dict
dataforseo_labs_page_intersection_live_item_form_dict = dataforseo_labs_page_intersection_live_item.from_dict(dataforseo_labs_page_intersection_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



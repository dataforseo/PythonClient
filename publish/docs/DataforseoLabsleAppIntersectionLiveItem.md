# DataforseoLabsleAppIntersectionLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword_data** | [**KeywordDataKeywordDataInfo**](KeywordDataKeywordDataInfo.md) |  | [optional] 
**intersection_result** | [**Dict[str, BaseAppDataSerpElementItem]**](BaseAppDataSerpElementItem.md) | contains SERP data for the returned keyword data will be provided in separate arrays for each app ID you specified in the app_ids object when setting a task; depending on the number of specified app IDs, it can contain from 1 to 20 arrays named respectively | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labsle_app_intersection_live_item import DataforseoLabsleAppIntersectionLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsleAppIntersectionLiveItem from a JSON string
dataforseo_labsle_app_intersection_live_item_instance = DataforseoLabsleAppIntersectionLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsleAppIntersectionLiveItem.to_json()

# convert the object into a dict
dataforseo_labsle_app_intersection_live_item_dict = dataforseo_labsle_app_intersection_live_item_instance.to_dict()
# create an instance of DataforseoLabsleAppIntersectionLiveItem from a dict
dataforseo_labsle_app_intersection_live_item_form_dict = dataforseo_labsle_app_intersection_live_item.from_dict(dataforseo_labsle_app_intersection_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



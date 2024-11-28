# DataforseoLabsAppleAppCompetitorsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**app_id** | **str** | id of the competitor app | [optional] 
**avg_position** | **float** | average position of the app in App Store SERP Note: average position is calculated for intersected keywords only; the value for a given application may differ when combined with different target applications | [optional] 
**sum_position** | **int** | sum of all app positions in App Store SERP Note: sum position is calculated for intersected keywords only; the value for a given application may differ when combined with different target applications | [optional] 
**intersections** | **int** | number of intersecting keywords | [optional] 
**competitor_metrics** | [**AppStoreMetricsBundleInfo**](AppStoreMetricsBundleInfo.md) |  | [optional] 
**full_metrics** | [**AppStoreMetricsBundleInfo**](AppStoreMetricsBundleInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_apple_app_competitors_live_item import DataforseoLabsAppleAppCompetitorsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAppleAppCompetitorsLiveItem from a JSON string
dataforseo_labs_apple_app_competitors_live_item_instance = DataforseoLabsAppleAppCompetitorsLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAppleAppCompetitorsLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_apple_app_competitors_live_item_dict = dataforseo_labs_apple_app_competitors_live_item_instance.to_dict()
# create an instance of DataforseoLabsAppleAppCompetitorsLiveItem from a dict
dataforseo_labs_apple_app_competitors_live_item_from_dict = DataforseoLabsAppleAppCompetitorsLiveItem.from_dict(dataforseo_labs_apple_app_competitors_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



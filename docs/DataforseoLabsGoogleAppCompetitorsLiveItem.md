# DataforseoLabsGoogleAppCompetitorsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**app_id** | **str** | id of the competitor app | [optional] 
**avg_position** | **float** | average position of the app in Google Play SERP Note: average position is calculated for intersected keywords only; the value for a given application may differ when combined with different target applications | [optional] 
**sum_position** | **int** | sum of all app positions in Google Play SERP Note: sum position is calculated for intersected keywords only; the value for a given application may differ when combined with different target applications | [optional] 
**intersections** | **int** | number of intersecting keywords | [optional] 
**competitor_metrics** | [**GooglePlayMetricsBundleInfo**](GooglePlayMetricsBundleInfo.md) |  | [optional] 
**full_metrics** | [**GooglePlayMetricsBundleInfo**](GooglePlayMetricsBundleInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_app_competitors_live_item import DataforseoLabsGoogleAppCompetitorsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleAppCompetitorsLiveItem from a JSON string
dataforseo_labs_google_app_competitors_live_item_instance = DataforseoLabsGoogleAppCompetitorsLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleAppCompetitorsLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_google_app_competitors_live_item_dict = dataforseo_labs_google_app_competitors_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleAppCompetitorsLiveItem from a dict
dataforseo_labs_google_app_competitors_live_item_from_dict = DataforseoLabsGoogleAppCompetitorsLiveItem.from_dict(dataforseo_labs_google_app_competitors_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



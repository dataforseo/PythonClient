# GooglePlayMetricsBundleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_play_search_organic** | [**AppMetricsInfo**](AppMetricsInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_play_metrics_bundle_info import GooglePlayMetricsBundleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePlayMetricsBundleInfo from a JSON string
google_play_metrics_bundle_info_instance = GooglePlayMetricsBundleInfo.from_json(json)
# print the JSON string representation of the object
print GooglePlayMetricsBundleInfo.to_json()

# convert the object into a dict
google_play_metrics_bundle_info_dict = google_play_metrics_bundle_info_instance.to_dict()
# create an instance of GooglePlayMetricsBundleInfo from a dict
google_play_metrics_bundle_info_form_dict = google_play_metrics_bundle_info.from_dict(google_play_metrics_bundle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



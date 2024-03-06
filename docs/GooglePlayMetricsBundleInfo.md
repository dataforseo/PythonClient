[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

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

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
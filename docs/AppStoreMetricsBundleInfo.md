[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppStoreMetricsBundleInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_store_search_organic** | [**AppMetricsInfo**](AppMetricsInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.app_store_metrics_bundle_info import AppStoreMetricsBundleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppStoreMetricsBundleInfo from a JSON string
app_store_metrics_bundle_info_instance = AppStoreMetricsBundleInfo.from_json(json)
# print the JSON string representation of the object
print AppStoreMetricsBundleInfo.to_json()

# convert the object into a dict
app_store_metrics_bundle_info_dict = app_store_metrics_bundle_info_instance.to_dict()
# create an instance of AppStoreMetricsBundleInfo from a dict
app_store_metrics_bundle_info_form_dict = app_store_metrics_bundle_info.from_dict(app_store_metrics_bundle_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
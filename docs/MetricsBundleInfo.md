[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# MetricsBundleInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organic** | [**MetricsInfo**](MetricsInfo.md) |  | [optional]
**paid** | [**MetricsInfo**](MetricsInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.metrics_bundle_info import MetricsBundleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsBundleInfo from a JSON string
metrics_bundle_info_instance = MetricsBundleInfo.from_json(json)
# print the JSON string representation of the object
print MetricsBundleInfo.to_json()

# convert the object into a dict
metrics_bundle_info_dict = metrics_bundle_info_instance.to_dict()
# create an instance of MetricsBundleInfo from a dict
metrics_bundle_info_form_dict = metrics_bundle_info.from_dict(metrics_bundle_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
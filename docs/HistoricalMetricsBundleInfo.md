[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# HistoricalMetricsBundleInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organic** | [**List[HistoricalMetricsInfo]**](HistoricalMetricsInfo.md) | traffic data from organic search | [optional]
**paid** | [**List[HistoricalMetricsInfo]**](HistoricalMetricsInfo.md) | traffic data from paid search | [optional]
**local_pack** | [**List[HistoricalMetricsInfo]**](HistoricalMetricsInfo.md) | traffic data from the featured snippet results in Google SERP | [optional]
**featured_snippet** | [**List[HistoricalMetricsInfo]**](HistoricalMetricsInfo.md) | traffic data from the local pack results in SERP | [optional]

## Example

```python
from dataforseo_client.models.historical_metrics_bundle_info import HistoricalMetricsBundleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalMetricsBundleInfo from a JSON string
historical_metrics_bundle_info_instance = HistoricalMetricsBundleInfo.from_json(json)
# print the JSON string representation of the object
print HistoricalMetricsBundleInfo.to_json()

# convert the object into a dict
historical_metrics_bundle_info_dict = historical_metrics_bundle_info_instance.to_dict()
# create an instance of HistoricalMetricsBundleInfo from a dict
historical_metrics_bundle_info_form_dict = historical_metrics_bundle_info.from_dict(historical_metrics_bundle_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")
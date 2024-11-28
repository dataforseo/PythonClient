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
print(MetricsBundleInfo.to_json())

# convert the object into a dict
metrics_bundle_info_dict = metrics_bundle_info_instance.to_dict()
# create an instance of MetricsBundleInfo from a dict
metrics_bundle_info_from_dict = MetricsBundleInfo.from_dict(metrics_bundle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AmazonMetricsBundleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_serp** | [**AppMetricsInfo**](AppMetricsInfo.md) |  | [optional] 
**amazon_paid** | [**AppMetricsInfo**](AppMetricsInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.amazon_metrics_bundle_info import AmazonMetricsBundleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonMetricsBundleInfo from a JSON string
amazon_metrics_bundle_info_instance = AmazonMetricsBundleInfo.from_json(json)
# print the JSON string representation of the object
print AmazonMetricsBundleInfo.to_json()

# convert the object into a dict
amazon_metrics_bundle_info_dict = amazon_metrics_bundle_info_instance.to_dict()
# create an instance of AmazonMetricsBundleInfo from a dict
amazon_metrics_bundle_info_form_dict = amazon_metrics_bundle_info.from_dict(amazon_metrics_bundle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



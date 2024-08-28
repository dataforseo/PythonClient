# BulkMetricsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etv** | **float** | estimated traffic volume estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and search volume values of all keywords the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**count** | **int** | total count of organic SERPs that contain the domain | [optional] 
**clickstream_etv** | **int** | estimated traffic volume based on clickstream data calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article https://dataforseo.com/help-center/whats-clickstream-estimated-traffic-volume-and-how-is-it-calculated | [optional] 

## Example

```python
from dataforseo_client.models.bulk_metrics_info import BulkMetricsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMetricsInfo from a JSON string
bulk_metrics_info_instance = BulkMetricsInfo.from_json(json)
# print the JSON string representation of the object
print BulkMetricsInfo.to_json()

# convert the object into a dict
bulk_metrics_info_dict = bulk_metrics_info_instance.to_dict()
# create an instance of BulkMetricsInfo from a dict
bulk_metrics_info_form_dict = bulk_metrics_info.from_dict(bulk_metrics_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



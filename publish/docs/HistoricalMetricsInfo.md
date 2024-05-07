# HistoricalMetricsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | year for which the data is provided | [optional] 
**month** | **int** | month for which the data is provided | [optional] 
**etv** | **float** | estimated traffic volume estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and search volume values of all keywords the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**count** | **int** | total count of organic SERPs that contain the domain | [optional] 

## Example

```python
from dataforseo_client.models.historical_metrics_info import HistoricalMetricsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalMetricsInfo from a JSON string
historical_metrics_info_instance = HistoricalMetricsInfo.from_json(json)
# print the JSON string representation of the object
print HistoricalMetricsInfo.to_json()

# convert the object into a dict
historical_metrics_info_dict = historical_metrics_info_instance.to_dict()
# create an instance of HistoricalMetricsInfo from a dict
historical_metrics_info_form_dict = historical_metrics_info.from_dict(historical_metrics_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



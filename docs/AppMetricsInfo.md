# AppMetricsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos_1** | **int** | number of organic SERPs where the product ranks #1 | [optional] 
**pos_2_3** | **int** | number of organic SERPs where the product ranks #2-3 | [optional] 
**pos_4_10** | **int** | number of organic SERPs where the product ranks #4-10 | [optional] 
**pos_11_100** | **int** | number of organic SERPs where the product ranks #11-100 | [optional] 
**count** | **int** | total count of Amazon organic SERPs that contain the product | [optional] 
**search_volume** | **int** | total search volume of the product’s ranking keywords in organic SERP | [optional] 

## Example

```python
from dataforseo_client.models.app_metrics_info import AppMetricsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppMetricsInfo from a JSON string
app_metrics_info_instance = AppMetricsInfo.from_json(json)
# print the JSON string representation of the object
print AppMetricsInfo.to_json()

# convert the object into a dict
app_metrics_info_dict = app_metrics_info_instance.to_dict()
# create an instance of AppMetricsInfo from a dict
app_metrics_info_form_dict = app_metrics_info.from_dict(app_metrics_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



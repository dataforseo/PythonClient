# MetricsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos_1** | **int** | number of organic SERPs where the domain ranks #1 | [optional] 
**pos_2_3** | **int** | number of organic SERPs where the domain ranks #2-3 | [optional] 
**pos_4_10** | **int** | number of organic SERPs where the domain ranks #4-10 | [optional] 
**pos_11_20** | **int** | number of organic SERPs where the domain ranks #11-20 | [optional] 
**pos_21_30** | **int** | number of organic SERPs where the domain ranks #21-30 | [optional] 
**pos_31_40** | **int** | number of organic SERPs where the domain ranks #31-40 | [optional] 
**pos_41_50** | **int** | number of organic SERPs where the domain ranks #41-50 | [optional] 
**pos_51_60** | **int** | number of organic SERPs where the domain ranks #51-60 | [optional] 
**pos_61_70** | **int** | number of organic SERPs where the domain ranks #61-70 | [optional] 
**pos_71_80** | **int** | number of organic SERPs where the domain ranks #71-80 | [optional] 
**pos_81_90** | **int** | number of organic SERPs where the domain ranks #81-90 | [optional] 
**pos_91_100** | **int** | number of organic SERPs where the domain ranks #91-100 | [optional] 
**etv** | **float** | estimated traffic volume estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and search volume values of all keywords the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**impressions_etv** | **float** | estimated traffic volume based on impressions estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and impressions values of all keywords the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**count** | **int** | total count of organic SERPs that contain the domain | [optional] 
**estimated_paid_traffic_cost** | **float** | estimated cost of converting organic search traffic into paid represents the estimated monthly cost of running ads (USD) for all keywords a domain ranks for the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search learn more about how the metric is calculated in this help center article | [optional] 
**is_new** | **int** | number of new ranked elements indicates how many new ranked elements were found for this domain | [optional] 
**is_up** | **int** | rank went up indicates how many ranked elements of this domain went up in Google Search | [optional] 
**is_down** | **int** | rank went down indicates how many ranked elements of this domain went down in Google Search | [optional] 
**is_lost** | **int** | lost ranked elements indicates how many ranked elements of this domain were previously presented in SERPs, but weren’t found during the last check | [optional] 

## Example

```python
from dataforseo_client.models.metrics_info import MetricsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsInfo from a JSON string
metrics_info_instance = MetricsInfo.from_json(json)
# print the JSON string representation of the object
print(MetricsInfo.to_json())

# convert the object into a dict
metrics_info_dict = metrics_info_instance.to_dict()
# create an instance of MetricsInfo from a dict
metrics_info_form_dict = metrics_info.from_dict(metrics_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



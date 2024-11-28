# DataforseoLabsMetricsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos_1** | **int** | number of organic SERPs where the domain or subdomain ranks #1 | [optional] 
**pos_2_3** | **int** | number of organic SERPs where the domain or subdomain ranks #2-3 | [optional] 
**pos_4_10** | **int** | number of organic SERPs where the domain or subdomain ranks #4-10 | [optional] 
**pos_11_20** | **int** | number of organic SERPs where the domain or subdomain ranks #11-20 | [optional] 
**pos_21_30** | **int** | number of organic SERPs where the domain or subdomain ranks #21-30 | [optional] 
**pos_31_40** | **int** | number of organic SERPs where the domain or subdomain ranks #31-40 | [optional] 
**pos_41_50** | **int** | number of organic SERPs where the domain or subdomain ranks #41-50 | [optional] 
**pos_51_60** | **int** | number of organic SERPs where the domain or subdomain ranks #51-60 | [optional] 
**pos_61_70** | **int** | number of organic SERPs where the domain or subdomain ranks #61-70 | [optional] 
**pos_71_80** | **int** | number of organic SERPs where the domain or subdomain ranks #71-80 | [optional] 
**pos_81_90** | **int** | number of organic SERPs where the domain or subdomain ranks #81-90 | [optional] 
**pos_91_100** | **int** | number of organic SERPs where the domain or subdomain ranks #91-100 | [optional] 
**etv** | **float** | estimated traffic volume estimated organic monthly traffic to the domain or subdomain calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the domain or subdomain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**impressions_etv** | **float** | estimated traffic volume based on impressions estimated organic monthly traffic to the domain or subdomain calculated as the product of CTR (click-through-rate) and impressions values of all keywords in the category that the domain or subdomain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**count** | **int** | total count of organic SERPs that contain the domain or subdomain | [optional] 
**estimated_paid_traffic_cost** | **float** | estimated cost of converting organic search traffic into paid represents the estimated monthly cost (USD) of running ads for all keywords in the category that the domain or subdomain ranks for the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search learn more about how the metric is calculated in this help center article | [optional] 
**is_new** | **int** | number of new ranked elements indicates how many new ranked elements were found for the indicated target | [optional] 
**is_up** | **int** | rank went up indicates how many ranked elements of the indicated target went up | [optional] 
**is_down** | **int** | rank went down indicates how many ranked elements of the indicated target went down | [optional] 
**is_lost** | **int** | lost ranked elements indicates how many ranked elements of the indicated target were previously presented in SERPs, but weren’t found during the last check | [optional] 
**clickstream_etv** | **int** | estimated traffic volume based on clickstream data calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article | [optional] 
**clickstream_gender_distribution** | **Dict[str, Optional[int]]** | distribution of estimated clickstream-based metrics by gender to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article | [optional] 
**clickstream_age_distribution** | **Dict[str, Optional[int]]** | distribution of clickstream-based metrics by age to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_metrics_info import DataforseoLabsMetricsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsMetricsInfo from a JSON string
dataforseo_labs_metrics_info_instance = DataforseoLabsMetricsInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsMetricsInfo.to_json())

# convert the object into a dict
dataforseo_labs_metrics_info_dict = dataforseo_labs_metrics_info_instance.to_dict()
# create an instance of DataforseoLabsMetricsInfo from a dict
dataforseo_labs_metrics_info_from_dict = DataforseoLabsMetricsInfo.from_dict(dataforseo_labs_metrics_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



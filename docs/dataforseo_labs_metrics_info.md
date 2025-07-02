# DataforseoLabsMetricsInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**pos_1** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #1 |[optional]|
**pos_2_3** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #2-3 |[optional]|
**pos_4_10** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #4-10 |[optional]|
**pos_11_20** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #11-20 |[optional]|
**pos_21_30** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #21-30 |[optional]|
**pos_31_40** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #31-40 |[optional]|
**pos_41_50** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #41-50 |[optional]|
**pos_51_60** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #51-60 |[optional]|
**pos_61_70** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #61-70 |[optional]|
**pos_71_80** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #71-80 |[optional]|
**pos_81_90** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #81-90 |[optional]|
**pos_91_100** | **StrictInt** | number of organic SERPs where the domain or subdomain ranks #91-100 |[optional]|
**etv** | **StrictFloat** | estimated traffic volume<br>estimated organic monthly traffic to the domain or subdomain<br>calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the domain or subdomain ranks for<br>learn more about how the metric is calculated in this help center article |[optional]|
**impressions_etv** | **StrictFloat** | estimated traffic volume based on impressions<br>estimated organic monthly traffic to the domain or subdomain<br>calculated as the product of CTR (click-through-rate) and impressions values of all keywords in the category that the domain or subdomain ranks for<br>learn more about how the metric is calculated in this help center article |[optional]|
**count** | **StrictInt** | total count of organic SERPs that contain the domain or subdomain |[optional]|
**estimated_paid_traffic_cost** | **StrictFloat** | estimated cost of converting organic search traffic into paid<br>represents the estimated monthly cost (USD) of running ads for all keywords in the category that the domain or subdomain ranks for<br>the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search<br>learn more about how the metric is calculated in this help center article |[optional]|
**is_new** | **StrictInt** | number of new ranked elements<br>indicates how many new ranked elements were found for the indicated target |[optional]|
**is_up** | **StrictInt** | rank went up<br>indicates how many ranked elements of the indicated target went up |[optional]|
**is_down** | **StrictInt** | rank went down<br>indicates how many ranked elements of the indicated target went down |[optional]|
**is_lost** | **StrictInt** | lost ranked elements<br>indicates how many ranked elements of the indicated target were previously presented in SERPs, but weren’t found during the last check |[optional]|
**clickstream_etv** | **StrictInt** | estimated traffic volume based on clickstream data<br>calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for<br>to retrieve results for this field, the parameter include_clickstream_data must be set to true<br>learn more about how the metric is calculated in this help center article |[optional]|
**clickstream_gender_distribution** | **Dict[str, Optional[StrictInt]]** | distribution of estimated clickstream-based metrics by gender<br>to retrieve results for this field, the parameter include_clickstream_data must be set to true<br>learn more about how the metric is calculated in this help center article |[optional]|
**clickstream_age_distribution** | **Dict[str, Optional[StrictInt]]** | distribution of clickstream-based metrics by age<br>to retrieve results for this field, the parameter include_clickstream_data must be set to true<br>learn more about how the metric is calculated in this help center article |[optional]|
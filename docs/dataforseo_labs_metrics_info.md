# DataforseoLabsMetricsInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**pos_1** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #1</em> |[optional]|
**pos_2_3** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #2-3</em> |[optional]|
**pos_4_10** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #4-10</em> |[optional]|
**pos_11_20** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #11-20</em> |[optional]|
**pos_21_30** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #21-30</em> |[optional]|
**pos_31_40** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #31-40</em> |[optional]|
**pos_41_50** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #41-50</em> |[optional]|
**pos_51_60** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #51-60</em> |[optional]|
**pos_61_70** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #61-70</em> |[optional]|
**pos_71_80** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #71-80</em> |[optional]|
**pos_81_90** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #81-90</em> |[optional]|
**pos_91_100** | **StrictInt** | <em>number of organic SERPs where the domain or subdomain ranks #91-100</em> |[optional]|
**etv** | **StrictFloat** | <em>estimated traffic volume</em><br>estimated organic monthly traffic to the domain or subdomain<br>calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the domain or subdomain ranks for<br>learn more about how the metric is calculated in <a href='https://dataforseo.com/help-center/how-is-etv-calculated' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**count** | **StrictInt** | <em>total count of organic SERPs that contain the domain or subdomain</em> |[optional]|
**estimated_paid_traffic_cost** | **StrictFloat** | <em>estimated cost of converting organic search traffic into paid</em><br>represents the estimated monthly cost (USD) of running ads for all keywords in the category that the domain or subdomain ranks for<br>the metric is calculated as the product of organic <code>etv</code> and paid <code>cpc</code> values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search<br>learn more about how the metric is calculated in <a href='https://dataforseo.com/help-center/how-is-traffic-cost-calculated' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**is_new** | **StrictInt** | <em>number of new ranked elements</em><br>indicates how many new ranked elements were found for the indicated target |[optional]|
**is_up** | **StrictInt** | <em>rank went up</em><br>indicates how many ranked elements of the indicated target went up |[optional]|
**is_down** | **StrictInt** | <em>rank went down</em><br>indicates how many ranked elements of the indicated target went down |[optional]|
**is_lost** | **StrictInt** | <em>lost ranked elements</em><br>indicates how many ranked elements of the indicated target were previously presented in SERPs, but weren't found during the last check |[optional]|
**clickstream_etv** | **StrictFloat** | <em>estimated traffic volume based on clickstream data</em><br>calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for<br>to retrieve results for this field, the parameter <code>include_clickstream_data</code> must be set to <code>true</code><br>learn more about how the metric is calculated in this <a href='https://dataforseo.com/help-center/whats-clickstream-estimated-traffic-volume-and-how-is-it-calculated' rel='noopener noreferrer' target='_blank'>help center article</a> |[optional]|
**clickstream_gender_distribution** | **Dict[str, Optional[StrictInt]]** | <em>distribution of estimated clickstream-based metrics by gender</em><br>to retrieve results for this field, the parameter <code>include_clickstream_data</code> must be set to <code>true</code><br>learn more about how the metric is calculated in this <a href='https://dataforseo.com/help-center/what-are-clickstream-based-metrics-and-how-do-we-calculate-them' rel='noopener noreferrer' target='_blank'>help center article</a> |[optional]|
**clickstream_age_distribution** | **Dict[str, Optional[StrictInt]]** | <em>distribution of clickstream-based metrics by age</em><br>to retrieve results for this field, the parameter <code>include_clickstream_data</code> must be set to <code>true</code><br>learn more about how the metric is calculated in this <a href='https://dataforseo.com/help-center/what-are-clickstream-based-metrics-and-how-do-we-calculate-them' rel='noopener noreferrer' target='_blank'>help center article</a> |[optional]|
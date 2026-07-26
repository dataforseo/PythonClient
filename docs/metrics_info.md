# MetricsInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**pos_1** | **StrictInt** | <em>number of organic SERPs where the domain ranks #1</em> |[optional]|
**pos_2_3** | **StrictInt** | <em>number of organic SERPs where the domain ranks #2-3</em> |[optional]|
**pos_4_10** | **StrictInt** | <em>number of organic SERPs where the domain ranks #4-10</em> |[optional]|
**pos_11_20** | **StrictInt** | <em>number of organic SERPs where the domain ranks #11-20</em> |[optional]|
**pos_21_30** | **StrictInt** | <em>number of organic SERPs where the domain ranks #21-30</em> |[optional]|
**pos_31_40** | **StrictInt** | <em>number of organic SERPs where the domain ranks #31-40</em> |[optional]|
**pos_41_50** | **StrictInt** | <em>number of organic SERPs where the domain ranks #41-50</em> |[optional]|
**pos_51_60** | **StrictInt** | <em>number of organic SERPs where the domain ranks #51-60</em> |[optional]|
**pos_61_70** | **StrictInt** | <em>number of organic SERPs where the domain ranks #61-70</em> |[optional]|
**pos_71_80** | **StrictInt** | <em>number of organic SERPs where the domain ranks #71-80</em> |[optional]|
**pos_81_90** | **StrictInt** | <em>number of organic SERPs where the domain ranks #81-90</em> |[optional]|
**pos_91_100** | **StrictInt** | <em>number of organic SERPs where the domain ranks #91-100</em> |[optional]|
**etv** | **StrictFloat** | <em>estimated traffic volume</em><br>estimated organic monthly traffic to the domain<br>calculated as the product of CTR (click-through-rate) and search volume values of all keywords the domain ranks for<br>learn more about how the metric is calculated in <a href='https://dataforseo.com/help-center/how-is-etv-calculated' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**count** | **StrictInt** | <em>total count of organic SERPs that contain the domain</em> |[optional]|
**estimated_paid_traffic_cost** | **StrictFloat** | <em>estimated cost of converting organic search traffic into paid</em><br>represents the estimated monthly cost of running ads (USD) for all keywords a domain ranks for<br>the metric is calculated as the product of organic <code>etv</code> and paid <code>cpc</code> values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search<br>learn more about how the metric is calculated in <a href='https://dataforseo.com/help-center/how-is-traffic-cost-calculated' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**is_new** | **StrictInt** | number of new ranked elements<br>indicates how many new ranked elements were found for this domain |[optional]|
**is_up** | **StrictInt** | rank went up<br>indicates how many ranked elements of this domain went up in Google Search |[optional]|
**is_down** | **StrictInt** | rank went down<br>indicates how many ranked elements of this domain went down in Google Search |[optional]|
**is_lost** | **StrictInt** | lost ranked elements<br>indicates how many ranked elements of this domain were previously presented in SERPs, but weren’t found during the last check |[optional]|
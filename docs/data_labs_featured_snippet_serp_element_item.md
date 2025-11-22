# DataLabsFeaturedSnippetSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | subdomain in SERP |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**featured_title** | **StrictStr** | the title of the featured snippets source page |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**url** | **StrictStr** | relevant URL in SERP |[optional]|
**table** | **Table** | results table<br>if there are none, equals null |[optional]|
**main_domain** | **StrictStr** | primary domain name in SERP |[optional]|
**relative_url** | **StrictStr** | URL in SERP that does not specify the HTTPs protocol and domain name |[optional]|
**etv** | **StrictFloat** | estimated traffic volume<br>estimated organic monthly traffic to the domain<br>calculated as the product of CTR (click-through-rate) and search volume values of the returned keyword<br>learn more about how the metric is calculated in this help center article |[optional]|
**estimated_paid_traffic_cost** | **StrictFloat** | estimated cost of converting organic search traffic into paid<br>represents the estimated monthly cost of running ads (USD) for the returned keyword<br>the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search<br>learn more about how the metric is calculated in this help center article |[optional]|
**clickstream_etv** | **StrictFloat** | estimated traffic volume based on clickstream data<br>calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for<br>to retrieve results for this field, the parameter include_clickstream_data must be set to true<br>learn more about how the metric is calculated in this help center article |[optional]|
**rank_changes** | **RankChanges** | changes in rankings<br>contains information about the ranking changes of the SERP element since the previous_updated_time |[optional]|
**backlinks_info** | **BacklinksInfo** | backlinks information for the ranked website |[optional]|
**rank_info** | **RankInfo** | page and domain rank information |[optional]|
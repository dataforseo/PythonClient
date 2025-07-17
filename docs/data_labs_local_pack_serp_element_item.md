# DataLabsLocalPackSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**domain** | **StrictStr** | domain in SERP |[optional]|
**phone** | **StrictStr** | phone number |[optional]|
**url** | **StrictStr** | sitelink URL |[optional]|
**is_paid** | **StrictBool** | indicates whether the element is an ad |[optional]|
**rating** | **RatingElement** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**main_domain** | **StrictStr** | primary domain name in SERP |[optional]|
**relative_url** | **StrictStr** | URL in SERP that does not specify the HTTPs protocol and domain name |[optional]|
**etv** | **StrictFloat** | estimated traffic volume<br>estimated organic monthly traffic a featured URL delivers to the domain<br>calculated as the product of CTR (click-through-rate) and search volume values of the returned keyword<br>learn more about how the metric is calculated in this help center article |[optional]|
**estimated_paid_traffic_cost** | **StrictFloat** | estimated cost of converting organic search traffic into paid<br>represents the estimated monthly cost of running ads for the returned keyword<br>the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search<br>learn more about how the metric is calculated in this help center article |[optional]|
**clickstream_etv** | **StrictFloat** |  |[optional]|
**rank_changes** | **RankChanges** | changes in rankings<br>ranking changes of the SERP element compared to the preceding month;<br>Note: the changes are calculated even if the preceding month is not included in a POST request |[optional]|
**backlinks_info** | **BacklinksInfo** | backlinks information for the ranked website |[optional]|
**rank_info** | **RankInfo** | page and domain rank information |[optional]|
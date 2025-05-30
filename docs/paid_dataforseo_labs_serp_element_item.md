# PaidDataforseoLabsSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**domain** | **StrictStr** | domain in SERP |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb in SERP |[optional]|
**url** | **StrictStr** | sitelink URL |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**extra** | **Dict[str, Optional[StrictStr]]** | additional information about the result |[optional]|
**description_rows** | **List[Optional[StrictStr]]** | extended description<br>if there is none, equals null |[optional]|
**links** | **List[Optional[AdLinkElement]]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**main_domain** | **StrictStr** | primary domain name in SERP |[optional]|
**relative_url** | **StrictStr** | URL in SERP that does not specify the HTTPs protocol and domain name |[optional]|
**etv** | **StrictFloat** | estimated traffic volume<br>estimated organic monthly traffic a featured URL delivers to the domain<br>calculated as the product of CTR (click-through-rate) and search volume values of the returned keyword<br>learn more about how the metric is calculated in this help center article |[optional]|
**estimated_paid_traffic_cost** | **StrictFloat** | estimated cost of paid monthly search traffic<br>represents the estimated cost of paid monthly traffic based on etv and cpc values<br>learn more about how the metric is calculated in this help center article |[optional]|
**clickstream_etv** | **StrictFloat** |  |[optional]|
**rank_changes** | **RankChanges** | changes in rankings<br>ranking changes of the SERP element compared to the preceding month;<br>Note: the changes are calculated even if the preceding month is not included in a POST request |[optional]|
**backlinks_info** | **BacklinksInfo** | backlinks information for the ranked website |[optional]|
**rank_info** | **RankInfo** | page and domain rank information |[optional]|
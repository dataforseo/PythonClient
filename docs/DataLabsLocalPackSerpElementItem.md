# DataLabsLocalPackSerpElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **string** | title of the result in SERP |[optional]|
**description** | **string** | description of the results element in SERP |[optional]|
**domain** | **string** | subdomain in SERP |[optional]|
**phone** | **string** | phone number |[optional]|
**url** | **string** | relevant URL in SERP |[optional]|
**is_paid** | **boolean** | indicates whether the element is an ad |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**main_domain** | **string** | primary domain name in SERP |[optional]|
**relative_url** | **string** | URL in SERP that does not specify the HTTPs protocol and domain name |[optional]|
**etv** | **number** | estimated traffic volume<br>estimated paid monthly traffic to the target<br>calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the target ranks for<br>learn more about how the metric is calculated in this help center article |[optional]|
**estimated_paid_traffic_cost** | **number** | estimated cost of monthly search traffic<br>represents the estimated cost of paid monthly traffic (USD) based on etv and cpc values of all keywords in the category that the target ranks for<br>learn more about how the metric is calculated in this help center article |[optional]|
**clickstream_etv** | **number** | estimated traffic volume based on clickstream data<br>calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for<br>to retrieve results for this field, the parameter include_clickstream_data must be set to true<br>learn more about how the metric is calculated in this help center article |[optional]|
**rank_changes** | **RankChanges** | changes in rankings<br>contains information about the ranking changes of the SERP element since the previous_updated_time |[optional]|
**backlinks_info** | **BacklinksInfo** | backlinks information for the target website |[optional]|
**rank_info** | **RankInfo** | page and domain rank information |[optional]|
# DataLabsOrganicSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | subdomain in SERP |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**url** | **StrictStr** | relevant URL in SERP |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb in SERP |[optional]|
**website_name** | **StrictStr** | relevant website name in SERP |[optional]|
**is_image** | **StrictBool** | indicates whether the element contains an image |[optional]|
**is_video** | **StrictBool** | indicates whether the element contains a video |[optional]|
**is_featured_snippet** | **StrictBool** | indicates whether the element is a featured_snippet |[optional]|
**is_malicious** | **StrictBool** | indicates whether the element is marked as malicious |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**pre_snippet** | **StrictStr** | includes additional information appended before the result description in SERP |[optional]|
**extended_snippet** | **StrictStr** | includes additional information appended after the result description in SERP |[optional]|
**amp_version** | **StrictBool** | Accelerated Mobile Pages<br>indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**rating** | **RatingInfo** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | words highlighted in bold within the results description |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**about_this_result** | **AboutThisResultElement** | contains information from the ‘About this result’ panel<br>‘About this result’ panel provides additional context about why Google returned this result for the given query;<br>this feature appears after clicking on the three dots next to most results |[optional]|
**main_domain** | **StrictStr** | primary domain name in SERP |[optional]|
**relative_url** | **StrictStr** | URL in SERP that does not specify the HTTPs protocol and domain name |[optional]|
**etv** | **StrictFloat** | estimated traffic volume<br>estimated paid monthly traffic to the target<br>calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the target ranks for<br>learn more about how the metric is calculated in this help center article |[optional]|
**estimated_paid_traffic_cost** | **StrictFloat** | estimated cost of monthly search traffic<br>represents the estimated cost of paid monthly traffic (USD) based on etv and cpc values of all keywords in the category that the target ranks for<br>learn more about how the metric is calculated in this help center article |[optional]|
**clickstream_etv** | **StrictFloat** | estimated traffic volume based on clickstream data<br>calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for<br>to retrieve results for this field, the parameter include_clickstream_data must be set to true<br>learn more about how the metric is calculated in this help center article |[optional]|
**rank_changes** | **RankChanges** | changes in rankings<br>contains information about the ranking changes of the SERP element since the previous_updated_time |[optional]|
**backlinks_info** | **BacklinksInfo** | backlinks information for the target website |[optional]|
**rank_info** | **RankInfo** | page and domain rank information |[optional]|
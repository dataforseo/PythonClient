# DataLabsOrganicSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | <em>subdomain in SERP</em> |[optional]|
**title** | **StrictStr** | <em>title of the result in SERP</em> |[optional]|
**url** | **StrictStr** | <em> relevant URL in SERP</em> |[optional]|
**breadcrumb** | **StrictStr** | <em>breadcrumb in SERP</em> |[optional]|
**website_name** | **StrictStr** | <em>relevant website name in SERP</em> |[optional]|
**is_image** | **StrictBool** | <em>indicates whether the element contains an <code class='prettyprint'>image</code></em> |[optional]|
**is_video** | **StrictBool** | <em>indicates whether the element contains a <code class='prettyprint'>video</code></em> |[optional]|
**is_featured_snippet** | **StrictBool** | <em>indicates whether the element is a <code class='prettyprint'>featured_snippet</code></em> |[optional]|
**is_malicious** | **StrictBool** | <em>indicates whether the element is marked as malicious</em> |[optional]|
**description** | **StrictStr** | <em>description of the results element in SERP</em> |[optional]|
**pre_snippet** | **StrictStr** | <em>includes additional information appended before the result description in SERP</em> |[optional]|
**extended_snippet** | **StrictStr** | <em>includes additional information appended after the result description in SERP</em> |[optional]|
**amp_version** | **StrictBool** | <em>Accelerated Mobile Pages</em><br>            indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**rating** | **RatingInfo** | <em>the item's rating </em><br>            the popularity rate based on reviews and displayed in SERP |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | <em>words highlighted in bold within the results <code>description</code></em> |[optional]|
**links** | **List[Optional[LinkElement]]** | <em>sitelinks</em><br>            the links shown below some of Google's search results<br>            if there are none, equals <code>null</code> |[optional]|
**about_this_result** | **AboutThisResultElement** | <em>contains information from the 'About this result' panel</em><br>            <a href='https://blog.google/products/search/learn-more-and-get-more-from-search/'>'About this result' panel</a> provides additional context about why Google returned this result for the given query;<br>            this feature appears after clicking on the three dots next to most results |[optional]|
**main_domain** | **StrictStr** | <em>primary domain name in SERP</em> |[optional]|
**relative_url** | **StrictStr** | <em>URL in SERP that does not specify the HTTPs protocol and domain name</em> |[optional]|
**etv** | **StrictFloat** | <em>estimated traffic volume</em><br>            estimated organic monthly traffic to the domain or webpage;<br>            calculated as the product of CTR (click-through-rate) and search volume values of all keywords the domain or webpage rank for;<br>            learn more about how the metric is calculated in <a href='https://dataforseo.com/help-center/how-is-etv-calculated' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**estimated_paid_traffic_cost** | **StrictFloat** | <em>estimated cost of converting organic search traffic into paid</em><br>            represents the estimated monthly cost of running ads for all keywords that a domain or webpage ranks for;<br>            the metric is calculated as the product of organic <code>etv</code> and paid <code>cpc</code> values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search;<br>            learn more about how the metric is calculated in <a href='https://dataforseo.com/help-center/how-is-traffic-cost-calculated' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**clickstream_etv** | **StrictFloat** | <em>estimated traffic volume based on clickstream data</em><br>            calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain or webpage ranks for;<br>            to retrieve results for this field, the parameter <code>include_clickstream_data</code> must be set to <code>true</code>;<br>            learn more about how the metric is calculated in this <a href='https://dataforseo.com/help-center/whats-clickstream-estimated-traffic-volume-and-how-is-it-calculated' rel='noopener noreferrer' target='_blank'>help center article</a> |[optional]|
**rank_changes** | **RankChanges** | <em>changes in rankings</em><br>            contains information about the ranking changes of the SERP element since the <code>previous_updated_time</code> |[optional]|
**backlinks_info** | **BacklinksInfo** | <em>backlinks information for the relevant page URL</em> |[optional]|
**rank_info** | **RankInfo** | <em>page and domain rank information</em> |[optional]|
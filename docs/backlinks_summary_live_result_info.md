# BacklinksSummaryLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | <em><code>target</code> in a POST array</em> |[optional]|
**first_seen** | **StrictStr** | <em>date and time when our crawler found the backlink for the <code>target</code> for the first time</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**lost_date** | **StrictStr** | <em>date and time when the backlink was lost</em><br>indicates the date and time when our crawler visited the target and it responded with a 4xx or 5xx status code or when its last backlink was removed<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**rank** | **StrictInt** | <code>target</code> rank<br>learn more about the metric and how it is calculated in <a href='https://dataforseo.com/help-center/what_is_rank_in_backlinks_api' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**backlinks** | **StrictInt** | <em>indicates the number of backlinks</em> |[optional]|
**backlinks_spam_score** | **StrictInt** | <em>spam score of the backlinks</em><br>displays the total spam score of all backlinks pointing to the <code>target</code> domain, subdomain, or webpage;<br>to learn more about how the metric is calculated, refer to <a href='https://dataforseo.com/help-center/what-is-spam-score-and-how-is-it-calculated' rel='noopener noreferrer' target='_blank'>this Help Center page</a> |[optional]|
**crawled_pages** | **StrictInt** | <em>number of crawled pages for the <code>target</code></em> |[optional]|
**info** | **TargetInfo** | <em>information about the <code>target</code></em> |[optional]|
**internal_links_count** | **StrictInt** | <em>number of internal links</em><br>calculated as the sum of internal links on the pages of the specified <code>target</code> |[optional]|
**external_links_count** | **StrictInt** | <em>number of external links on the page</em><br>calculated as the sum of external links on the pages of the specified <code>target</code> |[optional]|
**broken_backlinks** | **StrictInt** | <em>number of broken backlinks</em><br>number of broken backlinks pointing to the <code>target</code> |[optional]|
**broken_pages** | **StrictInt** | <em>number of broken pages</em><br>number of pages on the <code>target</code> that respond with 4xx or 5xx status codes<p>note that the number of broken pages includes pages on the <code>target</code> discovered by following external links, but it may also include pages discovered by following the target's sitemap |[optional]|
**referring_domains** | **StrictInt** | <em>indicates the number of referring domains</em><br>referring domains include subdomains that are counted as separate domains for this metric |[optional]|
**referring_domains_nofollow** | **StrictInt** | <em>number of domains pointing at least one nofollow link to the <code>target</code></em> |[optional]|
**referring_main_domains** | **StrictInt** | <em>indicates the number of referring main domains</em> |[optional]|
**referring_main_domains_nofollow** | **StrictInt** | <em>number of main domains pointing at least one nofollow link to the <code>target</code></em> |[optional]|
**referring_ips** | **StrictInt** | <em>number of referring IP addresses</em><br>number of IP addresses pointing to this page |[optional]|
**referring_subnets** | **StrictInt** | <em>number of referring subnetworks</em> |[optional]|
**referring_pages** | **StrictInt** | <em>indicates the number of pages pointing to the target</em> |[optional]|
**referring_pages_nofollow** | **StrictInt** | <em>number of referring pages pointing at least one nofollow link to the <code>target</code></em> |[optional]|
**referring_links_tld** | **Dict[str, Optional[StrictInt]]** | <em>top-level domains of the referring links</em><br>contains top level domains and referring link count per each |[optional]|
**referring_links_types** | **Dict[str, Optional[StrictInt]]** | <em>types of referring links</em><br>indicates the types of the referring links and link count per each type<br>possible values:<br><code>anchor</code>, <code>image</code>, <code>link</code>, <code>meta</code>, <code>canonical</code>, <code>alternate</code>, <code>redirect</code> |[optional]|
**referring_links_attributes** | **Dict[str, Optional[StrictInt]]** | <em>link attributes of the referring links</em><br>indicates link attributes of the referring links and link count per each attribute<br>example values:<br><code>nofollow</code>, <code>noopener</code>, <code>noreferrer</code>, <code>external</code>, <code>ugc</code>, <code>sponsored</code> |[optional]|
**referring_links_platform_types** | **Dict[str, Optional[StrictInt]]** | <em>types of referring platforms</em><br>indicates referring platform types and and link count per each platform<p>possible values: <code>cms</code>, <code>blogs</code>, <code>ecommerce</code>, <code>message-boards</code>, <code>wikis</code>, <code>news</code>, <code>organization</code> |[optional]|
**referring_links_semantic_locations** | **Dict[str, Optional[StrictInt]]** | <em>semantic locations of the referring links</em><br>indicates semantic elements in HTML where the referring links are located and link count per each semantic location<p>you can get the full list of semantic elements <a href='https://www.w3schools.com/html/html5_semantic_elements.asp' target='_blank' rel='noopener noreferrer'>here</a><br>example values:<br><code>article</code>, <code>section</code>, <code>summary</code>, <code>''</code> |[optional]|
**referring_links_countries** | **Dict[str, Optional[StrictInt]]** | <em>ISO country codes of the referring links</em><br>indicates ISO country codes of the domains where the referring links are located and the link count per each country |[optional]|
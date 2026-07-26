# BacklinksAnchorsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**anchor** | **StrictStr** | <em>anchor of the backlink</em> |[optional]|
**rank** | **StrictInt** | <em>rank of the anchor links</em><br>rank volume that referring websites pass to the <code>target</code> through links with a particular anchor<br><code>rank</code> is calculated based on the method for node ranking in a linked database - a principle used in the original Google PageRank algorithm<br>learn more about the metric and how it is calculated in <a href='https://dataforseo.com/help-center/what_is_rank_in_backlinks_api' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**backlinks** | **StrictInt** | <em>indicates the number of backlinks</em> |[optional]|
**first_seen** | **StrictStr** | <em>date and time when our crawler found the backlink with this anchor for the first time</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**lost_date** | **StrictStr** | <em>date and time when the last backlink with this anchor was lost</em><br>indicates the date and time when our crawler visited the page and it responded with 4xx or 5xx status code or the last backlink was removed<br>in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2017-01-24 13:20:59 +00:00</code> |[optional]|
**backlinks_spam_score** | **StrictInt** | <em>average spam score of all backlinks with this anchor</em><br>learn more about how the metric is calculated on <a href='https://dataforseo.com/help-center/what-is-spam-score-and-how-is-it-calculated' rel='noopener noreferrer' target='_blank'>this help center page</a> |[optional]|
**broken_backlinks** | **StrictInt** | <em>number of broken backlinks</em><br>number of broken backlinks pointing to the <code>target</code> |[optional]|
**broken_pages** | **StrictInt** | <em>number of broken pages</em><br>number of pages that respond with 4xx or 5xx status codes where backlinks are pointing to |[optional]|
**referring_domains** | **StrictInt** | <em>indicates the number of referring domains</em> |[optional]|
**referring_domains_nofollow** | **StrictInt** | <em>number of domains pointing at least one nofollow link to the <code>target</code></em> |[optional]|
**referring_main_domains** | **StrictInt** | <em>indicates the number of referring main domains</em> |[optional]|
**referring_main_domains_nofollow** | **StrictInt** | <em>number of main domains pointing at least one nofollow link to the <code>target</code></em> |[optional]|
**referring_ips** | **StrictInt** | <em>number of referring IP addresses</em><br>number of IP addresses pointing to this page |[optional]|
**referring_subnets** | **StrictInt** | <em>number of referring subnetworks</em> |[optional]|
**referring_pages** | **StrictInt** | <em>indicates the number of pages pointing to <code>target</code> with this anchor</em> |[optional]|
**referring_pages_nofollow** | **StrictInt** | <em>number of referring pages pointing at least one nofollow link to the <code>target</code> with this anchor</em> |[optional]|
**referring_links_tld** | **Dict[str, Optional[StrictInt]]** | <em>top-level domains of the referring links</em><br>contains top level domains and referring link count per each |[optional]|
**referring_links_types** | **Dict[str, Optional[StrictInt]]** | <em>types of referring links</em><br>indicates the types of the referring links and link count per each type<br>possible values:<br><code>anchor</code>, <code>image</code>, <code>link</code>, <code>meta</code>, <code>canonical</code>, <code>alternate</code>, <code>redirect</code> |[optional]|
**referring_links_attributes** | **Dict[str, Optional[StrictInt]]** | <em>link attributes of the referring links</em><br>indicates link attributes of the referring links and link count per each attribute |[optional]|
**referring_links_platform_types** | **Dict[str, Optional[StrictInt]]** | <em>types of referring platforms</em><br>indicates referring platform types and and link count per each platform<p>possible values: <code>cms</code>, <code>blogs</code>, <code>ecommerce</code>, <code>message-boards</code>, <code>wikis</code>, <code>news</code>, <code>organization</code> |[optional]|
**referring_links_semantic_locations** | **Dict[str, Optional[StrictInt]]** | <em>semantic locations of the referring links</em><br>indicates semantic elements in HTML where the referring links are located and link count per each semantic location<p>you can get the full list of semantic elements <a href='https://www.w3schools.com/html/html5_semantic_elements.asp' target='_blank' rel='noopener noreferrer'>here</a><br>examples:<br><code>article</code>, <code>section</code>, <code>summary</code> |[optional]|
**referring_links_countries** | **Dict[str, Optional[StrictInt]]** | <em>ISO country codes of the referring links</em><br>indicates ISO country codes of the domains where the referring links are located and the link count per each country |[optional]|
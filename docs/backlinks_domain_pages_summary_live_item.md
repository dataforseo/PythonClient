# BacklinksDomainPagesSummaryLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**url** | **StrictStr** | page URL |[optional]|
**rank** | **StrictFloat** | page rank<br>rank of the page<br>rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm<br>learn more about the metric and how it is calculated in this help center article |[optional]|
**backlinks** | **StrictFloat** | number of backlinks |[optional]|
**first_seen** | **StrictStr** | date and time when our crawler found a backlink to this page for the first time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**lost_date** | **StrictStr** | date and time when the last backlink to this page was lost<br>indicates the date and time when our crawler visited the page and it responded with 4xx or 5xx status code or the last backlink was removed<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2017-01-24 13:20:59 +00:00 |[optional]|
**backlinks_spam_score** | **StrictFloat** | average spam score of the backlinks pointing to the page<br>learn more about how the metric is calculated on this help center page |[optional]|
**broken_backlinks** | **StrictFloat** | number of broken backlinks<br>number of broken backlinks pointing to the page |[optional]|
**broken_pages** | **StrictFloat** | number of broken pages<br>number of pages that respond with 4xx or 5xx status codes where backlinks are pointing to |[optional]|
**referring_domains** | **StrictFloat** | indicates the number domains referring to the page |[optional]|
**referring_domains_nofollow** | **StrictFloat** | number of domains pointing at least one nofollow link to the page |[optional]|
**referring_main_domains** | **StrictFloat** | indicates the number of referring main domains |[optional]|
**referring_main_domains_nofollow** | **StrictInt** | number of main domains pointing at least one nofollow link to the page |[optional]|
**referring_ips** | **StrictFloat** | number of referring IP addresses<br>number of IP addresses pointing to this page |[optional]|
**referring_subnets** | **StrictFloat** | number of referring subnetworks |[optional]|
**referring_pages** | **StrictFloat** | indicates the number of pages pointing to the relevant url |[optional]|
**referring_pages_nofollow** | **StrictFloat** | number of referring pages pointing at least one nofollow link to the page |[optional]|
**referring_links_tld** | **Dict[str, Optional[StrictInt]]** | top-level domains of the referring links<br>contains top level domains and referring link count per each |[optional]|
**referring_links_types** | **Dict[str, Optional[StrictInt]]** | types of referring links<br>indicates the types of the referring links and link count per each type<br>possible values:<br>anchor, image, link, meta, canonical, alternate, redirect |[optional]|
**referring_links_attributes** | **Dict[str, Optional[StrictInt]]** | link attributes of the referring links<br>indicates link attributes of the referring links and link count per each attribute |[optional]|
**referring_links_platform_types** | **Dict[str, Optional[StrictInt]]** | types of referring platforms<br>indicates referring platform types and and link count per each platform<br>possible values: cms, blogs, ecommerce, message-boards, wikis, news, organization |[optional]|
**referring_links_semantic_locations** | **Dict[str, Optional[StrictInt]]** | semantic locations of the referring links<br>indicates semantic elements in HTML where the referring links are located and link count per each semantic location<br>you can get the full list of semantic elements here<br>examples:<br>article, section, footer |[optional]|
**referring_links_countries** | **Dict[str, Optional[StrictInt]]** | ISO country codes of the referring links<br>indicates ISO country codes of the domains where the referring links are located and the link count per each country |[optional]|
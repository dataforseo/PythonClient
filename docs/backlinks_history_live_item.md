# BacklinksHistoryLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**date** | **StrictStr** | date and time when the data for the target was stored<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**rank** | **StrictInt** | domain rank on the given date<br>learn more about the metric and how it is calculated in this help center article |[optional]|
**backlinks** | **StrictInt** | number of backlinks |[optional]|
**new_backlinks** | **StrictInt** | number of new backlinks for the target<br>data is provided based in a comparison with the previous period<br>Note: this data is available from May 2021;<br>if the date range specified in the POST request precedes May 2021, the field will equal 0 |[optional]|
**lost_backlinks** | **StrictInt** | number of lost backlinks for the target<br>data is provided based in a comparison with the previous period<br>Note: this data is available from May 2021;<br>if the date range specified in the POST request precedes May 2021, the field will equal 0 |[optional]|
**new_referring_domains** | **StrictInt** | number of new referring domains for the target<br>data is provided based in a comparison with the previous period<br>Note: this data is available from May 2021;<br>if the date range specified in the POST request precedes May 2021, the field will equal 0 |[optional]|
**lost_referring_domains** | **StrictInt** | number of lost referring domains for the target<br>data is provided based in a comparison with the previous period<br>Note: this data is available from May 2021;<br>if the date range specified in the POST request precedes May 2021, the field will equal 0 |[optional]|
**crawled_pages** | **StrictInt** | number of crawled pages for the target |[optional]|
**info** | **TargetInfo** | information about the target |[optional]|
**internal_links_count** | **StrictInt** | number of internal links<br>calculated as the sum of internal links on the pages of the specified target |[optional]|
**external_links_count** | **StrictInt** | number of external links on the page<br>calculated as the sum of external links on the pages of the specified target |[optional]|
**broken_backlinks** | **StrictInt** | number of broken backlinks<br>number of broken backlinks pointing to the target |[optional]|
**broken_pages** | **StrictInt** | number of broken pages<br>number of pages that receive backlinks but respond with 4xx or 5xx status codes |[optional]|
**referring_domains** | **StrictInt** | number of referring domains<br>referring domains include subdomains that are counted as separate domains for this metric |[optional]|
**referring_domains_nofollow** | **StrictInt** | number of domains pointing at least one nofollow link to the target |[optional]|
**referring_main_domains** | **StrictInt** | number of referring main domains |[optional]|
**referring_main_domains_nofollow** | **StrictInt** | number of main domains pointing at least one nofollow link to the target |[optional]|
**referring_ips** | **StrictInt** | number of referring IP addresses<br>number of IP addresses pointing to this page |[optional]|
**referring_subnets** | **StrictInt** | number of referring subnetworks |[optional]|
**referring_pages** | **StrictInt** | number of pages pointing to the target |[optional]|
**referring_pages_nofollow** | **StrictInt** | number of referring pages pointing at least one nofollow link to the target |[optional]|
**referring_links_tld** | **Dict[str, Optional[StrictInt]]** | top-level domains of the referring links<br>contains top-level domains and referring link count per each |[optional]|
**referring_links_types** | **Dict[str, Optional[StrictInt]]** | types of referring links<br>indicates the types of the referring links and link count per each type<br>possible values:<br>anchor, image, link, meta, canonical, alternate, redirect |[optional]|
**referring_links_attributes** | **Dict[str, Optional[StrictInt]]** | link attributes of the referring links<br>indicates link attributes of the referring links and link count per each attribute |[optional]|
**referring_links_platform_types** | **Dict[str, Optional[StrictInt]]** | types of referring platforms<br>indicates referring platform types and and link count per each platform<br>possible values: cms, blogs, ecommerce, message-boards, wikis, news, organization |[optional]|
**referring_links_semantic_locations** | **Dict[str, Optional[StrictInt]]** | semantic locations of the referring links<br>indicates semantic elements in HTML where the referring links are located and link count per each semantic location<br>you can get the full list of semantic elements here<br>examples:<br>article, section, summary |[optional]|
**referring_links_countries** | **Dict[str, Optional[StrictInt]]** | ISO country codes of the referring links<br>indicates ISO country codes of the domains where the referring links are located and the link count per each country |[optional]|
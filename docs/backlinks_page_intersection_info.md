# BacklinksPageIntersectionInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**domain_from** | **StrictStr** | domain referring to the target domain or webpage |[optional]|
**url_from** | **StrictStr** | URL of the page where the backlink is found |[optional]|
**url_from_https** | **StrictBool** | indicates whether the referring URL is secured with HTTPS<br>if true, the referring URL is secured with HTTPS |[optional]|
**domain_to** | **StrictStr** | domain the backlink is pointing to |[optional]|
**url_to** | **StrictStr** | URL the backlink is pointing to |[optional]|
**url_to_https** | **StrictBool** | indicates if the URL the backlink is pointing to is secured with HTTPS<br>if true, the URL is secured with HTTPS |[optional]|
**tld_from** | **StrictStr** | top-level domain of the referring URL |[optional]|
**is_new** | **StrictBool** | indicates whether the backlink is new<br>if true, the backlink was found on the page last time our crawler visited it |[optional]|
**is_lost** | **StrictBool** | indicates whether the backlink was removed<br>if true, the backlink or the entire page was removed |[optional]|
**backlink_spam_score** | **StrictInt** | spam score of the backlink<br>learn more about how the metric is calculated on this help center page |[optional]|
**rank** | **StrictInt** | backlink rank<br>rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm<br>learn more about the metric and how it is calculated in this help center article |[optional]|
**page_from_rank** | **StrictInt** | page rank of the referring page<br>page_from_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm<br>learn more about the metric and how it is calculated in this help center article |[optional]|
**domain_from_rank** | **StrictInt** | domain rank of the referring domain<br>indicates the rank of the domain at the time our crawler last saw the backlink;<br>domain_from_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm<br>learn more about the metric and how it is calculated in this help center article |[optional]|
**domain_from_platform_type** | **List[Optional[StrictStr]]** | platform types of the referring domain<br>possible values: cms, blogs, ecommerce, message-boards, wikis, news, organization |[optional]|
**domain_from_is_ip** | **StrictBool** | indicates if the domain is IP<br>if true, the domain functions as an IP address and does not have a domain name |[optional]|
**domain_from_ip** | **StrictStr** | IP address of the referring domain |[optional]|
**domain_from_country** | **StrictStr** | ISO country code of the referring domain |[optional]|
**page_from_external_links** | **StrictInt** | number of external links found on the referring page |[optional]|
**page_from_internal_links** | **StrictInt** | number of internal links found on the referring page |[optional]|
**page_from_size** | **StrictInt** | size of the referring page, in bytes<br>example:<br>63357 |[optional]|
**page_from_encoding** | **StrictStr** | character encoding of the referring page<br>example:<br>utf-8 |[optional]|
**page_from_language** | **StrictStr** | language of the referring page<br>in ISO 639-1 format<br>example:<br>en |[optional]|
**page_from_title** | **StrictStr** | title of the referring page |[optional]|
**page_from_status_code** | **StrictInt** | HTTP status code returned by the referring page<br>example:<br>200 |[optional]|
**first_seen** | **StrictStr** | date and time when our crawler found the backlink for the first time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**prev_seen** | **StrictStr** | previous to the most recent date when our crawler visited the backlink<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**last_seen** | **StrictStr** | most recent date when our crawler visited the backlink<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**item_type** | **StrictStr** | link type<br>possible values:<br>anchor, image, link, meta, canonical, alternate, redirect |[optional]|
**attributes** | **List[Optional[StrictStr]]** | link attributes of the referring links<br>example:<br>nofollow |[optional]|
**dofollow** | **StrictBool** | indicates whether the backlink is dofollow<br>if false, the backlink is nofollow |[optional]|
**original** | **StrictBool** | indicates whether the backlink was present on the referring page when our crawler first visited it |[optional]|
**alt** | **StrictStr** | alternative text of the image<br>this field will be null if backlink type is not image |[optional]|
**anchor** | **StrictStr** | anchor text of the backlink |[optional]|
**text_pre** | **StrictStr** | text snippet before the anchor text |[optional]|
**text_post** | **StrictStr** | snippet after the anchor text |[optional]|
**semantic_location** | **StrictStr** | indicates semantic element in HTML where the backlink is found<br>you can get the full list of semantic elements here<br>examples:<br>article, section, summary |[optional]|
**links_count** | **StrictInt** | number of identical backlinks found on the referring page |[optional]|
**group_count** | **StrictInt** | indicates total number of backlinks from this domain<br>for example, if mode is set to one_per_domain, this field will indicate the total number of backlinks coming from this domain |[optional]|
**is_broken** | **StrictBool** | indicates whether the backlink is broken<br>if true, the backlink is pointing to a page responding with a 4xx or 5xx status code |[optional]|
**url_to_status_code** | **StrictInt** | status code of the referenced page<br>if the value is null, our crawler hasn’t yet visited the webpage the link is pointing to<br>example:<br>200 |[optional]|
**url_to_spam_score** | **StrictInt** | spam score of the referenced page<br>if the value is null, our crawler hasn’t yet visited the webpage the link is pointing to<br>learn more about how the metric is calculated on this help center page |[optional]|
**url_to_redirect_target** | **StrictStr** | target url of the redirect<br>target page the redirect is pointing to |[optional]|
**is_indirect_link** | **StrictBool** | indicates whether the backlink is an indirect link<br>if true, the backlink is an indirect link pointing to a page that either redirects to url_to, or points to a canonical page |[optional]|
**indirect_link_path** | **List[Optional[Redirect]]** | indirect link path<br>indicates a URL or a sequence of URLs that lead to url_to |[optional]|
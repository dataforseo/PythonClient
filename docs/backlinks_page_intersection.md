# BacklinksPageIntersection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**domain_from** | **StrictStr** | <em>domain referring to the target domain or webpage</em> |[optional]|
**url_from** | **StrictStr** | <em>URL of the page where the backlink is found</em> |[optional]|
**url_from_https** | **StrictBool** | <em>indicates whether the referring URL is secured with HTTPS</em><br>if <code>true</code>, the referring URL is secured with HTTPS |[optional]|
**domain_to** | **StrictStr** | <em>domain the backlink is pointing to</em> |[optional]|
**url_to** | **StrictStr** | <em>URL the backlink is pointing to</em> |[optional]|
**url_to_https** | **StrictBool** | <em>indicates if the URL the backlink is pointing to is secured with HTTPS</em><br>if <code>true</code>, the URL is secured with HTTPS |[optional]|
**tld_from** | **StrictStr** | <em>top-level domain of the referring URL</em> |[optional]|
**is_new** | **StrictBool** | <em>indicates whether the backlink is new</em><br>if <code>true</code>, the backlink was found on the page last time our crawler visited it |[optional]|
**is_lost** | **StrictBool** | <em>indicates whether the backlink was removed</em><br>if <code>true</code>, the backlink or the entire page was removed |[optional]|
**backlink_spam_score** | **StrictInt** | <em>spam score of the backlink</em><br>learn more about how the metric is calculated on <a href='https://dataforseo.com/help-center/what-is-spam-score-and-how-is-it-calculated' rel='noopener noreferrer' target='_blank'>this help center page</a> |[optional]|
**rank** | **StrictInt** | <em>backlink rank</em><br><code>rank</code> is calculated based on the method for node ranking in a linked database - a principle used in the original Google PageRank algorithm<br>learn more about the metric and how it is calculated in <a href='https://dataforseo.com/help-center/what_is_rank_in_backlinks_api' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**page_from_rank** | **StrictInt** | <em>page rank of the referring page</em><br><code>page_from_rank</code> is calculated based on the method for node ranking in a linked database - a principle used in the original Google PageRank algorithm<br>learn more about the metric and how it is calculated in <a href='https://dataforseo.com/help-center/what_is_rank_in_backlinks_api' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**domain_from_rank** | **StrictInt** | <em>domain rank of the referring domain</em><br>indicates the rank of the domain at the time our crawler last saw the backlink;<br><code>domain_from_rank</code> is calculated based on the method for node ranking in a linked database - a principle used in the original Google PageRank algorithm<br>learn more about the metric and how it is calculated in <a href='https://dataforseo.com/help-center/what_is_rank_in_backlinks_api' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**domain_from_platform_type** | **List[Optional[StrictStr]]** | <em>platform types of the referring domain</em><p>possible values: <code>cms</code>, <code>blogs</code>, <code>ecommerce</code>, <code>message-boards</code>, <code>wikis</code>, <code>news</code>, <code>organization</code> |[optional]|
**domain_from_is_ip** | **StrictBool** | <em>indicates if the domain is IP</em><br>if <code>true</code>, the domain functions as an IP address and does not have a domain name |[optional]|
**domain_from_ip** | **StrictStr** | <em>IP address of the referring domain</em> |[optional]|
**domain_from_country** | **StrictStr** | <em>ISO country code of the referring domain</em> |[optional]|
**page_from_external_links** | **StrictInt** | <em>number of external links found on the referring page</em> |[optional]|
**page_from_internal_links** | **StrictInt** | <em>number of internal links found on the referring page</em> |[optional]|
**page_from_size** | **StrictInt** | <em>size of the referring page, in bytes</em><br>example:<br><code>63357</code> |[optional]|
**page_from_encoding** | **StrictStr** | <em>character encoding of the referring page</em><br>example:<br><code>utf-8</code> |[optional]|
**page_from_language** | **StrictStr** | <em>language of the referring page</em><br>in ISO 639-1 format<br>example:<br><code>en</code> |[optional]|
**page_from_title** | **StrictStr** | <em>title of the referring page</em> |[optional]|
**page_from_status_code** | **StrictInt** | <em>HTTP status code returned by the referring page</em><br>example:<br><code>200</code> |[optional]|
**first_seen** | **StrictStr** | <em>date and time when our crawler found the backlink for the first time</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**prev_seen** | **StrictStr** | <em>previous to the most recent date when our crawler visited the backlink</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**last_seen** | **StrictStr** | <em>most recent date when our crawler visited the backlink</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**item_type** | **StrictStr** | <em>link type</em><br>possible values:<br><code>anchor</code>, <code>image</code>, <code>link</code>, <code>meta</code>, <code>canonical</code>, <code>alternate</code>, <code>redirect</code> |[optional]|
**attributes** | **List[Optional[StrictStr]]** | <em>link attributes of the referring links</em><br>example:<br><code>nofollow</code> |[optional]|
**dofollow** | **StrictBool** | <em>indicates whether the backlink is dofollow</em><br>if <code>false</code>, the backlink is nofollow |[optional]|
**original** | **StrictBool** | <em>indicates whether the backlink was present on the referring page when our crawler first visited it</em> |[optional]|
**alt** | **StrictStr** | <em>alternative text of the image</em><br>this field will be <code>null</code> if backlink <code>type</code> is not image |[optional]|
**anchor** | **StrictStr** | <em>anchor text of the backlink</em> |[optional]|
**text_pre** | **StrictStr** | <em>text snippet before the anchor text</em> |[optional]|
**text_post** | **StrictStr** | <em>snippet after the anchor text</em> |[optional]|
**semantic_location** | **StrictStr** | <em>indicates semantic element in HTML where the backlink is found</em><br>you can get the full list of semantic elements <a href='https://www.w3schools.com/html/html5_semantic_elements.asp' target='_blank' rel='noopener noreferrer'>here</a><br>examples:<br><code>article</code>, <code>section</code>, <code>summary</code> |[optional]|
**links_count** | **StrictInt** | <em>number of identical backlinks found on the referring page</em> |[optional]|
**group_count** | **StrictInt** | <em>indicates total number of backlinks from this domain</em><br>for example, if <code>mode</code> is set to <code>one_per_domain</code>, this field will indicate the total number of backlinks coming from this domain |[optional]|
**is_broken** | **StrictBool** | <em>indicates whether the backlink is broken</em><br>if <code>true</code>, the backlink is pointing to a page responding with a 4xx or 5xx status code |[optional]|
**url_to_status_code** | **StrictInt** | <em>status code of the referenced page</em><br>if the value is <code>null</code>, our crawler hasn't yet visited the webpage the link is pointing to<br>example:<br><code>200</code> |[optional]|
**url_to_spam_score** | **StrictInt** | <em>spam score of the referenced page</em><br>if the value is <code>null</code>, our crawler hasn't yet visited the webpage the link is pointing to<br>learn more about how the metric is calculated on <a href='https://dataforseo.com/help-center/what-is-spam-score-and-how-is-it-calculated' rel='noopener noreferrer' target='_blank'>this help center page</a> |[optional]|
**url_to_redirect_target** | **StrictStr** | <em>target url of the redirect</em><br>target page the redirect is pointing to |[optional]|
**is_indirect_link** | **StrictBool** | <em>indicates whether the backlink is an indirect link</em><br>if <code>true</code>, the backlink is an indirect link pointing to a page that either redirects to <code>url_to</code>, or points to a canonical page |[optional]|
**indirect_link_path** | **List[Optional[BacklinksRedirectInfo]]** | <em>indirect link path</em><br>indicates a URL or a sequence of URLs that lead to <code>url_to</code> |[optional]|
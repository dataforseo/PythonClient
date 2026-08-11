# DomainInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**name** | **StrictStr** | <em>domain name</em> |[optional]|
**cms** | **StrictStr** | <em>content management system</em><br>content management system identified on a website<br>the content of_the <code>generator</code>_meta tag<br>the data is taken from the first random page that returns the 200 response code<br>if our crawler was unable to identify the cms, the value would be <code>null</code>n |[optional]|
**ip** | **StrictStr** | <em>domain ip address</em> |[optional]|
**server** | **StrictStr** | <em>website server</em><br>the version of the server detected on a website<br>the content of the <code class='prettyprint'>server</code> header<br>the information is taken from the first page which response code is 200 |[optional]|
**crawl_start** | **StrictStr** | <em>time when the crawling start</em><br>date and time when the website was sent for crawling<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**crawl_end** | **StrictStr** | <em>time when the crawling ended</em><br>date and time when the crawling was finished<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code><br><strong>Note:</strong> informative only if <code>'crawl_progress'</code> is <code>'finished'</code><br>if <code>'crawl_progress'</code> is <code>in_progress</code>, the value will be <code>null</code> |[optional]|
**extended_crawl_status** | **StrictStr** | <em>crawl status and errors</em><br>indicates the reason why a website was not crawled;<br>can take the following values:<br><code>no_errors</code> - no crawling errors were detected;<br><code>site_unreachable</code> - our crawler could not reach a website and thus was not able to obtain a status code;<br><code>invalid_page_status_code</code> - status code of the first crawled page &gt;= 400;<br><code>forbidden_meta_tag</code> - the first crawled page contains the &lt;meta robots='noindex'&gt; tag;<br><code>forbidden_robots</code> - robots.txt forbids crawling the page;<br><code>forbidden_http_header</code> - HTTP header of the page contains 'X-Robots-Tag: noindex' ;<br><code>too_many_redirects</code> - the first crawled page has more than 10 redirects;<br><code>unknown</code> - the reason is unknown |[optional]|
**ssl_info** | **SslInfo** | <em>ssl certificate info</em><br>information about the Secure Sockets Layer protocol detected on a website |[optional]|
**checks** | **Dict[str, Optional[StrictBool]]** | <em>website checks</em><br>other on-page check-ups related to the website |[optional]|
**total_pages** | **StrictInt** | <em>total crawled pages</em><br>the total number of crawled pages |[optional]|
**total_uncrawlable_resources** | **StrictInt** | <em>total uncrawlable resources</em><br>the total number of resources that could not be crawled;<br>the resource is considered uncrawlable when the actual content type of the resource doesn't match the content type expected by the crawler |[optional]|
**page_not_found_status_code** | **StrictInt** | <em>status code returned by a non-existent page</em><br>in most cases, it is recommended a server returns a 404 response code |[optional]|
**canonicalization_status_code** | **StrictInt** | <em>status code returned by a canonicalized page</em><br>the checkup of the server behavior when our crawler tries to access the website via IP;<br>in most cases, it is recommended that canonicalized pages respond with a <code>301</code> or <code>302</code> status code |[optional]|
**directory_browsing_status_code** | **StrictInt** | <em>status code returned by a directory</em><br>the status code returned by a directory page on a target website<br>in most cases, it is recommended that directories respond with a <code>403</code> or <code>401</code> status code |[optional]|
**www_redirect_status_code** | **StrictInt** | <em>redirect status code</em><br>the status code of the www to non-www redirect<br>in most cases, it is recommended that redirect returns a <code>301</code> status code |[optional]|
**main_domain** | **StrictStr** | <em>root domain name</em> |[optional]|
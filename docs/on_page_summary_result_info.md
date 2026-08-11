# OnPageSummaryResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | <em>status of the crawling session</em><br>possible values: <code>in_progress</code>, <code>finished</code> |[optional]|
**crawl_status** | **CrawlStatusInfo** | <em>details of the crawling session</em> |[optional]|
**crawl_gateway_address** | **StrictStr** | <em>crawler ip address</em><br>displays the IP address used by the crawler to initiate the current crawling session<br>you can find the full list of IPs used by our crawler in the <a href='/v3/on_page/overview' target='_blank' rel='noopener noreferrer'>Overview section</a> |[optional]|
**crawl_stop_reason** | **StrictStr** | <em>reason why the crawling stopped</em><br>information about the reason why the crawling process stopped;<br>possible values:<br><code>limit_exceeded</code> - the limit set in the <code>max_crawl_pages</code> was exceeded;<br><code>empty_queue</code> - all URLs in the queue were crawled;<br><code>force_stopped</code> - the crawling process was halted using the<a href='/v3/on_page/force_stop' target='_blank' rel='noopener noreferrer'> On Page API Force Stop</a> function;<br><code>unexpected_exception</code> - an internal error was encountered while crawling the <code>target</code>, contact support for more info |[optional]|
**domain_info** | **DomainInfo** | <em>domain-wide info</em><br>on-page information about the target domain and crawling process |[optional]|
**page_metrics** | **PageMetrics** | <em>page-specific info</em><br>metrics information on the target website pages |[optional]|
# OnPageSummaryResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | status of the crawling session<br>possible values: in_progress, finished |[optional]|
**crawl_status** | **CrawlStatusInfo** | details of the crawling session |[optional]|
**crawl_gateway_address** | **StrictStr** | crawler ip address<br>displays the IP address used by the crawler to initiate the current crawling session<br>you can find the full list of IPs used by our crawler in the Overview section |[optional]|
**crawl_stop_reason** | **StrictStr** | reason why the crawling stopped<br>information about the reason why the crawling process stopped;<br>possible values:<br>limit_exceeded – the limit set in the max_crawl_pages was exceeded;<br>empty_queue – all URLs in the queue were crawled;<br>force_stopped – the crawling process was halted using the On Page API Force Stop function;<br>unexpected_exception – an internal error was encountered while crawling the target, contact support for more info |[optional]|
**domain_info** | **DomainInfo** | domain-wide info<br>on-page information about the target domain and crawling process |[optional]|
**page_metrics** | **PageMetrics** | page-specific info<br>metrics information on the target website pages |[optional]|
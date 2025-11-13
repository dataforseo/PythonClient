# SerpApiStopCrawlOnMatchInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**match_value** | **StrictStr** | arget domain or wildcard value<br>required field if stop_crawl_on_match is specified;<br>specify a target domain or wildcard value;<br>Note: domain name must be specified without a request protocol;<br>example: dataforseo.com |[optional]|
**match_type** | **StrictStr** | target match type<br>required field if stop_crawl_on_match is specified;<br>type of match for the match_value<br>possible values: domain, with_subdomains, wildcard |[optional]|
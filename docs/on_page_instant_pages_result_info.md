# OnPageInstantPagesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | status of the crawling session<br>possible values: in_progress, finished |[optional]|
**crawl_status** | **CrawlStatusInfo** | details of the crawling session<br>in this case the value will be null |[optional]|
**crawl_gateway_address** | **StrictStr** | crawler ip address<br>displays the IP address used by the crawler to initiate the current crawling session<br>you can find the full list of IPs used by our crawler in the Overview section |[optional]|
**items_count** | **StrictInt** | number of items in the results array |[optional]|
**items** | **List[Optional[OnPageStylesheetResourceItem]]** | items array |[optional]|
# OnPageRawHtmlResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | status of the crawling session<br>possible values: in_progress, finished |[optional]|
**crawl_status** | **CrawlStatusInfo** | details of the crawling session |[optional]|
**items_count** | **StrictInt** | number of items in the results array |[optional]|
**items** | **List[Optional[OnPageRawHtmlItem]]** | items array |[optional]|
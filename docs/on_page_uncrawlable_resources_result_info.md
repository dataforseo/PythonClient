# OnPageUncrawlableResourcesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | status of the crawling sessionpossible values: in_progress, finished |[optional]|
**crawl_status** | **CrawlStatusInfo** | details of the crawling session |[optional]|
**current_offset** | **StrictInt** |  |[optional]|
**total_items_count** | **StrictInt** | total number of uncrawlable resources found total number of uncrawlable resources found during the crawl of the target domain |[optional]|
**items_count** | **StrictInt** | number of uncrawlable resources in the items array |[optional]|
**items** | **List[Optional[OnPageUncrawlableResourcesItem]]** | array of uncrawlable resources |[optional]|
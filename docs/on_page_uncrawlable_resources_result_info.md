# OnPageUncrawlableResourcesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | <em>status of the crawling session</em><br>possible values: <code>in_progress</code>, <code>finished</code> |[optional]|
**crawl_status** | **CrawlStatusInfo** | <em>details of the crawling session</em> |[optional]|
**current_offset** | **StrictInt** |  |[optional]|
**total_items_count** | **StrictInt** | <em>total number of uncrawlable resources found</em><br> total number of uncrawlable resources found during the crawl of the target domain |[optional]|
**items_count** | **StrictInt** | <em>number of uncrawlable resources in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[OnPageUncrawlableResourcesItem]]** | <em>array of uncrawlable resources</em> |[optional]|
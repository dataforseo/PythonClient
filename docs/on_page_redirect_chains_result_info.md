# OnPageRedirectChainsResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | <em>status of the crawling session</em><br>possible values: <code>in_progress</code>, <code>finished</code> |[optional]|
**crawl_status** | **CrawlStatusInfo** | <em>details of the crawling session</em> |[optional]|
**total_items_count** | **StrictInt** | <em>total number of relevant items in the database</em> |[optional]|
**items_count** | **StrictInt** | <em>number of items in the results array</em> |[optional]|
**items** | **List[Optional[OnPageRedirectChainsItem]]** | <em>items array</em> |[optional]|
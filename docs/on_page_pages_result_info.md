# OnPagePagesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | status of the crawling session<br>possible values: in_progress, finished |[optional]|
**crawl_status** | **CrawlStatusInfo** | details of the crawling session |[optional]|
**search_after_token** | **StrictStr** |  |[optional]|
**current_offset** | **StrictFloat** |  |[optional]|
**total_items_count** | **StrictFloat** | total number of relevant items in the database |[optional]|
**items_count** | **StrictFloat** | number of items in the results array |[optional]|
**items** | **List[Optional[BaseOnPageResourceItemInfo]]** | items array |[optional]|
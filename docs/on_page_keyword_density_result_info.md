# OnPageKeywordDensityResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | status of the crawling session<br>possible values: in_progress, finished |[optional]|
**crawl_status** | **CrawlStatus** | details of the crawling session |[optional]|
**total_items_count** | **StrictFloat** | total number of relevant items<br>total number of keywords on the specified website or web page matching the set keyword_length and filters |[optional]|
**items_count** | **StrictFloat** | number of items in the results array |[optional]|
**items** | **List[Optional[OnPageKeywordDensityItem]]** | items array |[optional]|
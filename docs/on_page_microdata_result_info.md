# OnPageMicrodataResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | <em>status of the crawling session</em><br>possible values: <code>in_progress</code>, <code>finished</code> |[optional]|
**crawl_status** | **CrawlStatusInfo** | <em>details of the crawling session</em> |[optional]|
**test_summary** | **TestSummary** | <em>microdata validation test results</em> |[optional]|
**items_count** | **StrictInt** | <em>number of items in the results array</em> |[optional]|
**items** | **List[Optional[OnPageMicrodataInfoItem]]** | <em>items array</em> |[optional]|
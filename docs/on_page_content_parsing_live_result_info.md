# OnPageContentParsingLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | <em>status of the crawling session</em><br>possible values: <code>in_progress</code>, <code>finished</code> |[optional]|
**crawl_status** | **CrawlStatusInfo** | <em>details of the crawling session</em> |[optional]|
**items_count** | **StrictInt** | <em>number of items in the results array</em> |[optional]|
**items** | **List[Optional[ContentParsingElement]]** | <em>items array</em> |[optional]|
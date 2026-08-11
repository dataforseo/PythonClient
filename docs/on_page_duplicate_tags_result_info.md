# OnPageDuplicateTagsResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | <em>status of the crawling session</em><br>possible values: <code>in_progress</code>, <code>finished</code> |[optional]|
**crawl_status** | **CrawlStatusInfo** | <em>details of the crawling session</em> |[optional]|
**total_pages_count** | **StrictInt** | <em>total number of pages with duplicate tags</em><br>displays the total number of pages with duplicate tags of the target website |[optional]|
**pages_count** | **StrictInt** | <em>number of pages with duplicate tags in the response</em><br>displays the number of pages with duplicate tags returned in the response |[optional]|
**items_count** | **StrictInt** | <em>number of items in the results array</em> |[optional]|
**items** | **List[Optional[OnPageDuplicateTagsItem]]** | <em>items array</em> |[optional]|
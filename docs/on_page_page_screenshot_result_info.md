# OnPagePageScreenshotResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | <em>status of the crawling session</em><br>possible values: <code>in_progress</code>, <code>finished</code> |[optional]|
**error_message** | **StrictStr** | <em>error message</em><br>if the <code>url</code> you indicated returns a 404 status code or is not a valid URL, you will obtain <code>'error_message':'Screenshot is empty'</code><br>if no error is encountered, the value will be <code>null</code> |[optional]|
**items_count** | **StrictInt** | <em>number of items in the results array</em> |[optional]|
**items** | **List[Optional[ScreenshotItem]]** | <em>items array</em> |[optional]|
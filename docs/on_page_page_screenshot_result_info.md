# OnPagePageScreenshotResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**crawl_progress** | **StrictStr** | status of the crawling session<br>possible values: in_progress, finished |[optional]|
**error_message** | **StrictStr** | error message<br>if the url you indicated returns a 404 status code or is not a valid URL, you will obtain 'error_message':'Screenshot is empty'<br>if no error is encountered, the value will be null |[optional]|
**items_count** | **StrictFloat** | number of items in the results array |[optional]|
**items** | **List[Optional[ScreenshotItem]]** | items array |[optional]|
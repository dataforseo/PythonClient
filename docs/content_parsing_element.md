# ContentParsingElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**fetch_time** | **StrictStr** | date and time when the content was fethced<br>example:<br>'2022-11-01 10:02:52 +00:00' |[optional]|
**status_code** | **StrictInt** | status code of the page |[optional]|
**page_content** | **PageContentInfo** | parsed content of the page |[optional]|
**page_as_markdown** | **StrictStr** | page content in the markdown format<br>page content in the text-to-HTML markdown format<br>specify markdown_view as true in the request to return the value |[optional]|
# KeywordsDataErrorsResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | id of the task |[optional]|
**datetime** | **StrictStr** | date and time when an error occurred<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**function** | **StrictStr** | corresponding API function |[optional]|
**error_code** | **StrictFloat** | error code |[optional]|
**error_message** | **StrictStr** | error message or error URL<br>error message (see full list) or URL that caused an error |[optional]|
**http_url** | **StrictStr** | URL that caused an error<br>URL you used for making an API call or pingback/postback URL |[optional]|
**http_method** | **StrictStr** | HTTP method |[optional]|
**http_code** | **StrictFloat** | HTTP status code |[optional]|
**http_time** | **StrictFloat** | time taken by HTTP request<br>for tasks set with a pingback/postback, this field will show the time it took your server to respond |[optional]|
**http_response** | **StrictStr** | HTTP response<br>server response |[optional]|
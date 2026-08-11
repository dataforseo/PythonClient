# OnPageErrorsResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | <em>task identifier</em><br><strong>unique task identifier in our system in the <a href='https://en.wikipedia.org/wiki/Universally_unique_identifier'>UUID</a> format</strong> |[optional]|
**datetime** | **StrictStr** | <em>date and time when an error occurred</em><br>in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**function** | **StrictStr** | <em>corresponding API function</em> |[optional]|
**error_code** | **StrictInt** | <em>error code</em> |[optional]|
**error_message** | **StrictStr** | <em>error message or error URL</em><br>error message <a href='https://docs.dataforseo.com/v3/appendix/errors/' rel='noopener noreferrer' target='_blank'>(see full list)</a> or URL that caused an error |[optional]|
**http_url** | **StrictStr** | <em>URL that caused an error</em><br>URL you used for making an API call or pingback/postback URL |[optional]|
**http_method** | **StrictStr** | <em>HTTP method</em> |[optional]|
**http_code** | **StrictInt** | <em>HTTP status code</em> |[optional]|
**http_time** | **StrictFloat** | <em>time taken by HTTP request</em><br>for tasks set with a pingback/postback, this field will show the time it took your server to respond |[optional]|
**http_response** | **StrictStr** | <em>HTTP response</em><br>server response |[optional]|
# OnPageWaterfallItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**page_url** | **StrictStr** | <em>URL of the page</em> |[optional]|
**time_to_interactive** | **StrictInt** | <em><a href='https://web.dev/interactive/'>Time To Interactive (TTI)</a> metric</em><br>the time it takes until the user can interact with a page (in milliseconds) |[optional]|
**dom_complete** | **StrictInt** | <em>time to load resources</em><br>the time it takes until the page and all of its subresources are downloaded (in milliseconds) |[optional]|
**connection_time** | **StrictInt** | <em>time to connect to a server</em><br>the time it takes until the connection with a server is established (in milliseconds) |[optional]|
**time_to_secure_connection** | **StrictInt** | <em>time to establish a secure connection</em><br>the time it takes until the secure connection with a server is established (in milliseconds) |[optional]|
**request_sent_time** | **StrictInt** | <em>time to send a request to a server</em><br>the time it takes until the request to a server is sent (in milliseconds) |[optional]|
**waiting_time** | **StrictInt** | <em>time to first byte <a href='https://en.wikipedia.org/wiki/Time_to_first_byte'>(TTFB)</a> in milliseconds</em> |[optional]|
**download_time** | **StrictInt** | <em>time it takes for a browser to receive a response (in milliseconds)</em> |[optional]|
**duration_time** | **StrictInt** | <em>total time it takes until a browser receives a complete response from a server (in milliseconds)</em> |[optional]|
**fetch_start** | **StrictInt** | <em>time to start downloading the HTML resource</em><br>the amount of time the browser needs to start downloading a page |[optional]|
**fetch_end** | **StrictInt** | <em>time to complete downloading the HTML resource</em><br>the amount of time the browser needs to complete downloading a page |[optional]|
**resources** | **List[Optional[WaterfallResourceInfo]]** | <em>resource-specific timing</em><br>contains separate arrays with timing for each resource found on the page |[optional]|
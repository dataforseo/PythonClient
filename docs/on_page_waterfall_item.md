# OnPageWaterfallItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**page_url** | **StrictStr** | URL of the page |[optional]|
**time_to_interactive** | **StrictInt** | Time To Interactive (TTI) metric<br>the time it takes until the user can interact with a page (in milliseconds) |[optional]|
**dom_complete** | **StrictInt** | time to load resources<br>the time it takes until the page and all of its subresources are downloaded (in milliseconds) |[optional]|
**connection_time** | **StrictInt** | time to connect to a server<br>the time it takes until the connection with a server is established (in milliseconds) |[optional]|
**time_to_secure_connection** | **StrictInt** | time to establish a secure connection<br>the time it takes until the secure connection with a server is established (in milliseconds) |[optional]|
**request_sent_time** | **StrictInt** | time to send a request to a server<br>the time it takes until the request to a server is sent (in milliseconds) |[optional]|
**waiting_time** | **StrictInt** | time to first byte (TTFB) in milliseconds |[optional]|
**download_time** | **StrictInt** | time it takes for a browser to receive a response (in milliseconds) |[optional]|
**duration_time** | **StrictInt** | total time it takes until a browser receives a complete response from a server (in milliseconds) |[optional]|
**fetch_start** | **StrictInt** | time to start downloading the HTML resource<br>the amount of time the browser needs to start downloading a page |[optional]|
**fetch_end** | **StrictInt** | time to complete downloading the HTML resource<br>the amount of time the browser needs to complete downloading a page |[optional]|
**resources** | **List[Optional[BaseOnPageResourceItemInfo]]** | resource-specific timing<br>contains separate arrays with timing for each resource found on the page |[optional]|
# PageTiming


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**time_to_interactive** | **StrictInt** | <em><a href='https://web.dev/interactive/'>Time To Interactive (TTI)</a> metric</em><br>the time it takes until the user can interact with a page (in milliseconds) |[optional]|
**dom_complete** | **StrictInt** | <em>time to load resources</em><br>the time it takes until the page and all of its subresources are downloaded (in milliseconds) |[optional]|
**largest_contentful_paint** | **StrictFloat** | <em>Core Web Vitals metric measuring how fast the largest above-the-fold content element is displayed</em><br>The amount of time (in milliseconds) to render the largest content element visible in the viewport, from when the user requests the URL. <a href='https://web.dev/lcp/'>Learn more</a>. |[optional]|
**first_input_delay** | **StrictFloat** | <em>Core Web Vitals metric indicating the responsiveness of a page</em><br>The time (in milliseconds) from when a user first interacts with your page to the time when the browser responds to that interaction. <a href='https://web.dev/fid/'>Learn more</a>. |[optional]|
**connection_time** | **StrictInt** | <em>time to connect to a server</em><br>the time it takes until the connection with a server is established (in milliseconds) |[optional]|
**time_to_secure_connection** | **StrictInt** | <em>time to establish a secure connection</em><br>the time it takes until the secure connection with a server is established (in milliseconds) |[optional]|
**request_sent_time** | **StrictInt** | <em>time to send a request to a server</em><br>the time it takes until the request to a server is sent (in milliseconds) |[optional]|
**waiting_time** | **StrictInt** | <em>time to first byte <a href='https://en.wikipedia.org/wiki/Time_to_first_byte'>(TTFB)</a> in milliseconds</em> |[optional]|
**download_time** | **StrictInt** | <em>time it takes for a browser to receive a response (in milliseconds)</em> |[optional]|
**duration_time** | **StrictInt** | <em>total time it takes until a browser receives a complete response from a server (in milliseconds)</em> |[optional]|
**fetch_start** | **StrictInt** | <em>time to start downloading the HTML resource</em><br>the amount of time the browser needs to start downloading a page |[optional]|
**fetch_end** | **StrictInt** | <em>time to complete downloading the HTML resource</em><br>the amount of time the browser needs to complete downloading a page |[optional]|
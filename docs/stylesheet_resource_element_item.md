# StylesheetResourceElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**meta** | **ResourceMetaInfo** | resource properties<br>the value depends on the resource_type<br>note that if you do not indicate a url when setting a task, resource’s meta is returned based on the data from the page where our crawler first saw the resource;<br>to obtain resource’s meta from a particular url, specify that URL when setting a task |[optional]|
**fetch_timing** | **FetchTiming** | resource fething time range |[optional]|
**accept_type** | **StrictStr** | indicates the expected type of resource<br>for example, if 'resource_type': 'broken', accept_type will indicate the type of the broken resource<br>possible values:<br>any, none, image, sitemap, robots, script, stylesheet, redirect, html, text, other, font |[optional]|
**initiator** | **StrictStr** | resource initiator |[optional]|
**duration_time** | **StrictInt** | total time it takes until a browser receives a complete response from a server (in milliseconds) |[optional]|
**fetch_start** | **StrictInt** | time to start downloading the resource<br>the amount of time the browser needs to start downloading a resource |[optional]|
**fetch_end** | **StrictInt** | time to complete downloading the resource<br>the amount of time the browser needs to complete downloading a resource |[optional]|
**is_render_blocking** | **StrictBool** | indicates whether the resource blocks rendering |[optional]|